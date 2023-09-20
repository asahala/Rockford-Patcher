import binascii
import os
from PIL import Image

""" Converter for graphic-planar EGA graphics =================

                                             Aleksi Sahala 2023
                                             github.com/asahala

=========================================================== """

ega_palette = [
    (0,0,0),     (0,0,170),    (0,170,0),    (0,170,170),
    (170,0,0),   (170,0,170),  (170,85,0),   (170,170,170),
    (85,85,85),  (85,85,255),  (85,255,85),  (85,255,255),
    (255,85,85), (255,85,255), (255,255,85), (255,255,255)]


""" In case the game uses custom orders for palette, they
can be defined here. Each map has 16 pointers that refer
to the standard EGA palette, e.g. mapping [0, 0, ...] has
two black colors. These mappings refer to Rockford's
theme palettes found in the EXE file. """

themes = {
    'title': [0,1,12,9,12,14,4,5,6,6,0,8,7,7,15,15],
    'menu': [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],
    'hunter': [8,9,2,7,4,6,14,13,13,1,12,0,0,6,12,15],
    'scuba': [1,4,2,3,4,14,6,4,12,6,0,11,8,7,15,13],
    'cook': [0,15,7,14,4,2,12,14,4,6,14,12,9,9,15,15],
    'player': [2,14,8,1,6,4,12,0,0,0,8,7,7,15,14,15],
    'cowboy': [1,10,6,4,12,8,14,12,7,9,10,0,8,7,7,15],
    'music': [8,6,2,9,4,4,12,12,15,0,0,5,12,14,0,15],
    'space': [8,9,14,3,9,5,15,12,14,4,6,11,14,0,14,15],
    'luck': [1,7,11,15,14,12,0,0,7,15,10,2,0,13,14,15],
    'body': [0,7,4,3,12,7,15,15,8,8,12,12,12,13,13,15],
    'miner': [0,7,2,1,4,14,6,13,8,10,8,12,12,14,12,6]}


def binary_to_hex(binary):
    """ Convert binary numbers into hex

    :param binary         input binary
    :type binary          tuple of integers

    """
    
    b = ''.join(binary)#str(i) for i in binary)
    h = format(int(b, 2), 'x').zfill(2)
    return h


class EGAImage:

    def __init__(self):
        self.EGA = []

    def convert_to_default(self):
        converted = []
        for value in self.EGA:
            x = int(''.join(value), 2)

            if x == 0: # if background color
                true_index = 0 # keep it and refer to the same index as usual
            #elif x in (11, 12):
            #    true_index = 10
            else:
                true_index = themes['hunter'][x]

            a = str(format(true_index, '04b'))
            converted.append(list(a))
        self.EGA = converted
            
    
    def read_planar(self, filename):
        """ Read raw graphic-planar EGA. In this format
        the image is stored fully in four planes as it is """

        print(f"> Reading {filename}")

        plane_size = os.path.getsize(filename) / 4
        planes = [[],[],[],[]]
        
        with open(filename, 'rb') as f:
            i = 1
            plane = 0
            while True:

                byte = binascii.hexlify(f.read(1))
                
                if not byte:
                    break
                
                binary = bin(int(byte, 16))[2:].zfill(8)
                planes[plane].extend((list(binary)))

                """ Switch to next plane """
                if i == plane_size:
                    plane += 1
                    i = 0
                i += 1

        ## Temporary: Rockford has inverted planes
        planes = planes[::-1]

        """ Combine planes into EGA palette values in binary """   
        for p in zip(*planes):
            self.EGA.append([x for x in p])


    def write_planar(self, filename):
        """ Write EGA data into planar format """

        """ Reformat binary EGA palette into planes """
        bins = [[],[],[],[]]
        for plane in self.EGA:
            for e, p in enumerate(plane):
                bins[e].append(p)

        bins = bins[::-1]

        """ Transform planes into 8-bit binaries and write """
        with open(filename, 'wb') as output:
            for plane in bins:
                hex_values = (binary_to_hex(plane[i:i+8]) for i
                              in range(0, len(plane), 8))
                for x in hex_values:
                    output.write(binascii.unhexlify(str.encode(x)))


    def write_png(self, filename, palette, mapping=None):
        """ Writes EGA data into PNG format. Use mapping
        in case the game uses odd combinations off EGA colors
        like Rockford.

        :param filename           output file name
        :param palette            palette in RGB
        :param mapping            palette mapper

        :type filename            str
        :type palette             [(r,g,b), (r,g,b), ...]
        :type mapping             dict

        """

        if mapping is None:
            pal = palette
        else:
            pal = [palette[color] for color in mapping]
            
        canvas = Image.new('RGB', (320, 200))
        raw_data = [pal[int(''.join(value), 2)] for value in self.EGA]
        canvas.putdata(raw_data[0:64000])
        canvas.show()
        canvas.save(filename, 'png')


    def read_png(self, filename, palette, mapping=None):
        """ Reads PNG file into raw EGA data """

        if mapping is None:
            palette = palette
        else:
            palette = [palette[color] for color in mapping]

        new = Image.new("RGB", (len(palette), 1))
        new.putdata(palette)
        pal = new.convert('P', palette=1, colors=16)
        
        image = Image.open(filename)
        x = image.convert('RGB').quantize(colors=16, method=2, kmeans=0, palette=pal) 
        resolution = (image.width, image.height)

        #cols = set()
        for pixel in x.convert('RGB').getdata():
            
            index = palette.index(pixel)
            
            binary = list("{0:04b}".format(index))
            #print(pixel, index, binary)
            #print(binary)

            self.EGA.append(binary)
        #rint(cols)
            
            
            
        
    
img = EGAImage()
#img.read_planar('cowboy.ega')
#img.convert_to_default()
#print(img.EGA[0:100])
#img.write_planar('hunter.add')
#img.write_png('hunter2.png', ega_palette)
#img.read_png('menu2.png', ega_palette)
#img.write_planar('menu.ega')
#img.write_png('x', ega_palette, mapping=themes['menu'])
#img.write_planar('hunter.add')
#img.write_planar('menu.add')



