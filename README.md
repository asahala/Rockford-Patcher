![alt text](https://www.mv.helsinki.fi/home/asahala/rockford/banner2.png)

# Rockford patcher and trainer
[Rockford](https://en.wikipedia.org/wiki/Rockford_(video_game)) was a Boulder Dash clone published by Mastertronic ltd. in 1988 for DOS. The game included 20 levels divided into five difficulty settings, each using their own themes: hunter, cook, cowboy, space and doctor. 

Rockford also included 20 **hidden levels** which were unplayable. When I contacted Mastertronic in 2006, I was told that they were designed for a possible future add-on, which was never released because they recided to do Rockford II instead. These levels were about feature five additional graphic sets called scuba, miner, player (sports), luck (leprechaun) and music. The graphics have been reconstructed by using the information on some of the sprites and palettes found in the game's planar EGA files and the EXE. In the current version, big animations are not included, only the tile sets and menu graphics.

This patcher/trainer allows you to play the hidden level set, as well as turn on some cheats.

Tested with the [ROCKFORD.EXE that is 29963 bytes in size](https://www.xtcabandonware.com/game/786/rockford). Has not been tested with the version with infinite lives. Does not work witht the 18kb ROCKFORD.EXE due to encryption.

## Enabling hidden levels
Copy all files from the folder ```gfx``` to your ROCKFORD directory. Then copy ```rockford_patcher.py``` into you your ROCKFROD directory and run it. After this you can play the hidden levels by running ```ADDON.EXE```.

## Converting planar EGA to PNG and back
Converting graphics requires [PIL](https://pypi.org/project/Pillow/) (tested on version 8.1.0).

Script ```planar_extractor.py``` can be used in your ROCKFORD directory to convert the planar EGA files into PNG and back. Use ```extract_png()``` to convert tilesets into PNG and ```save_planar()``` to convert them into the planar format. If you want to convert the original graphics sets into PNG, you can do it as follows:

```
img = EGAImage()
img.read_planar('body.fil')
img.write_png('yourfile.png', ega_palette, mapping=themes['body'])
```
Due to the fact that Rockford themes do not use standard EGA palette, you must always use the mapping of the theme in question when extracting files. To convert it back to planar:

```
img = EGAImage()
img.read_png('tmp.png', ega_palette, mapping=themes['body'])
img.write_planar('body.fil')
```
Works also with the animation files (with extension CAR). 

Note that you must only use EGA palette with the graphics. If you use any non EGA colors, my conversion script will quantize them into EGA and it can look ugly. The safest option is to use mspaint and color picker, or you can use my tool [Bitcrush](https://github.com/asahala/Bitcrush) to convert tiles into EGA more elegantly. 

## Trainer
If you find the game too difficult, you can set on god-mode by setting ```god_mode = True``` in the ```main()``` function. After this, colliding with enemies, falling stones or being in explosions will not kill you, but instead spawn money around you. You can abuse this feature by hitting the key ```R```. This explodes whatever is around you and replaces them with money. Try not blow up the exit door.

![alt text](https://www.mv.helsinki.fi/home/asahala/rockford/screenshot.png)

## What is reconstructed and what is not?
Short answer: everything except the levels, their gold counts and times, general idea of the themes, their color space and one frame of each player character. Long answer below:

***Order of the themes:*** The order of the themes is based on the collectible names fround from the EXE from offset 7A0 - 7EF. It is not 100% certain which themes they refer to, but with a little reasoning all except jewels and gems are somewhat obvious. Clubs are for luck, notes for music and cups for the player. I have put scuba and miner in this order based on the palette definitions. There's only one theme with black background in the EXE (offsets 9E3 - 9F2), and I assume that this belongs to the miner more likely than the blue background at offsets 95B - 95A.

***Order of the levels:*** The levels have been extracted from CELLMAPS.BIN and aligned with the themes in their order of appearance. I assume that it is the correct one, since the themes and levels of the base game have aligned similarly. The levels are ordered as HUNTER, THEME6, COOK, THEME7 etc.

***Graphics:*** As for the lost graphics, the EXE only lists the tileset and animation file names (offsets 810 - 8DC). However, all tilesets except SPACE.FIL contain placeholder sprites for the player characters of all themes, including the hidden ones. These are in the order scuba diver, football player, musician, miner and leprechaun. Unfortunately their original colors are not shown and due to Amiga OCS --> EGA conversion, it is not possible to figure out using a single tileset even which pixels should be the same color. However, using all the tilesets this infromation can be reconstructed. 

Thus, only one tile is available for each hidden graphics set. I have used those as a reference point to draw the character animations. All enemies, tiles, walls etc. are pure ad hoc drawings my be that could fit the theme, except for the collectibles. Thanks to palette definitions that can be found from the exe at offsets 929 - 9F3, I could have some kind of idea of the general color scheme. For example, that the miner should be pretty dark and luck fairly saturated.

Some tilesets have unused assets, such as the steam locomotive for Cowboy. I've modified some of these for the hidden themes.

To make editing graphics easier, I have re-adjusted all the hidden theme EGA palettes from Amiga OCS converted limited palettes to full EGA. As Rockford does not allow changing the background color to any other palette index (represented in octal numbers) than what's on the first offset, all palettes except miner consist only of 15 colors. This is, because the background color must exist twice in the palette, at the first offset and at its normal place in octal notation. Because black is more useful color than many others, I have replaced some unused color with black (e.g. with light magenta or light green). Keep this in mind if you play with the graphics files.

## Want to collaborate?
I not a graphics artist. If you you are, and are interested in collaborating to finetune the tile sets and graphics in a way that they are more similar to the game's original style, reach me out. All the big animations for the hidden themes are still undone.


