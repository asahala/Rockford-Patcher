import os
import sys
import binascii
import argparse

""" ======================================================
Rockford Patcher and trainer -- Aleksi Sahala 2023

                                github.com/asahala


This is a simple patcher for Rockford by Mastertronic.

Running this script patches your ROCKFORD.EXE and
creates a new ADDON.EXE that allows you to play the
unreleased level set (so-called DISK 2).

Copy MENU.ADD into your ROCKFORD directory and run this
script. Set path in main() or simply put this script in
your ROCKFORD directory.

Enable god-mode in main() by setting god_mode = True

==================================================== """

## Hardcoded hex-values (there are at least two different
## versions of ROCKFORD.EXE where the offsets differ.

## Collectible namespace
EXE_COLL = '2020474f4c440000202047454d530000'\
           '4150504c455300002020435550530000'\
           '20434f494e530000204e4f5445530000'\
           '202053554e53000020434c5542530000'\
           '48454152545300004a4557454c530000'

ADD_COLL = '202047454d530000202047454d530000'\
           '20204355505300002020435550530000'\
           '204e4f5445530000204e4f5445530000'\
           '20434c554253000020434c5542530000'\
           '4a4557454c5300004a4557454c530000'

## Graphic set references, FIL --> EGA
GRAPHICS = {
    'hunter': ['48554e5445522e46494c','48554e5445522e454741'],
    'cook': ['434f4f4b2e46494c','434f4f4b2e454741'],
    'cowboy': ['434f57424f592e46494c','434f57424f592e454741'],
    'space': ['53504143452e46494c','53504143452e454741'],
    'body': ['424f44592e46494c','424f44592e454741']}

## Palettes. Normalizes palettes converted from Amiga OCS to EGA,
## Curiously, these are represented as octal number
PALETTES = {
    'hunter': ['10110207040616151501140000061417','01010203040506071011001314151617'],
    'cook': ['00170716040214160406161411111717','02010203040506071011121314001617'],
    'cowboy': ['01120604141016140711120010070717','10010203040506071011001314151617'],
    'space': ['10111603110517141604061316001617','01010203040506071011121314151617'],
    'body': ['00070403140717171010141414151517','00010203040506071011121314151617']}


## Money to be collected
BYTES_MONEY = [
    '2800280050009600',
    '1400410082003700',
    '3200230019002d00',
    '140023001e002100',
    '1e007d0016003700',
    '32001e001e002800',
    '1a0037003c003c00',
    '0f000b001e004100',
    '120046004b001200',
    '1000180039000100']

## Level times
BYTES_TIME = [
    '6e006e0082006e00',
    '50008c0064006e00',
    '6e006e005a008200',
    '5a0064006e006400',
    '6e00730078007300',
    '82005a006e006e00',
    '6e006e008c006e00',
    '820082008c009100',
    '8200a000aa008c00',
    '8c008c006e00b400']

## Menu graphics and level set
FIL_NAMES = '43454c4c4d4150532e42494e004d454e552e46494c'
ADD_NAMES = '43454c4c4d4150532e414444004d454e552e414444'

def patch_file(path, god_mode):

    """ Patches ROCKFORD.EXE by a simple replacement operation """
    
    with open(os.path.join(path, 'ROCKFORD.EXE'), 'rb') as exe,\
         open(os.path.join(path, 'CELLMAPS.BIN'), 'rb') as maps,\
         open(os.path.join(path,'ADDON.EXE'), 'wb') as exe2,\
         open(os.path.join(path,'CELLMAPS.ADD'), 'wb') as maps2:
        
        hex_data = binascii.hexlify(exe.read()).decode('ascii').lower()
        map_data = binascii.hexlify(maps.read()).decode('ascii')

        for values in (BYTES_MONEY, BYTES_TIME):
            if ''.join(values) not in hex_data:
                print('Unknown ROCKFORD.EXE version.')
                sys.exit()
                
            source = ''.join(values[0:-1])
            target = ''.join(values[1:])
            old = hex_data
            hex_data = hex_data.replace(source, target)

        for name, pair in GRAPHICS.items():
            if pair[0] not in hex_data:
                print(f'> ERROR! Unable to find graphic refs to {name}')
            else:
                print(f'> Updated: {name} graphic set')
                hex_data = hex_data.replace(pair[0], pair[1])

        for name, pair in PALETTES.items():
            if pair[0] not in hex_data:
                print(f'> ERROR! Unable to find palette for {name}')
            else:
                print(f'> Updated: {name} palette')
                hex_data = hex_data.replace(pair[0], pair[1])

        if EXE_COLL in hex_data:
            hex_data = hex_data.replace(EXE_COLL, ADD_COLL)
            print(f'> Updated: collectible names')
        else:
            print(f'> ERROR! Unable to find collectible data')
        
        hex_data = hex_data.replace(FIL_NAMES, ADD_NAMES)

        if god_mode:
            if len(hex_data) != 59926:
                print('> WARNING! Your ROCKFORD.EXE is not 29963 bytes in size.',\
                      'God-mode might crash your game')
            hex_data = hex_data[:5937] + '1' + hex_data[5938:]
            print('> God-mode enabled. Press R to explode walls around you.')
        else:
            hex_data = hex_data[:5937] + '2' + hex_data[5938:]
            
        bytes_ = binascii.unhexlify(str.encode(hex_data.upper()))
        exe2.write(bytes_)
        print('> Patched EXE')

        """ Update CELLMAPS.BIN """
        map_data = map_data[7040:] + map_data[:7040]
        maps2.write(binascii.unhexlify(str.encode(map_data)))
        print('> Patched cellmaps')

    print('> Run ADDON.EXE in DOSBox to play') 


def main():
    
    god_mode = False
    path = '.'
    patch_file(path, god_mode)
    

if __name__ == "__main__":
    main()
    
    
