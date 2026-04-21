![alt text](https://www.mv.helsinki.fi/home/asahala/rockford/banner3.png)

# Summary
This tool enables the hidden level set in Rockford with correct level times, money collection amounts and point values, as well as gives the hidden themes reconstructed tile sets.

# Rockford patcher and trainer
[Rockford](https://en.wikipedia.org/wiki/Rockford_(video_game)) was a Boulder Dash clone published by Mastertronic ltd. in 1988 for DOS. The game included 20 levels divided into five difficulty settings or "worlds", each using their own themes: hunter, cook, cowboy, space and doctor. 

Many did not know that Rockford also included 20 **hidden levels** which were unplayable, but recoverable via hacking the game files. When I contacted Mastertronic in 2006, I was told that they were designed for a possible future add-on, which was never released because they decided to release Rockford II instead. These levels were about feature five additional graphic sets called scuba, miner, player (sports), luck (leprechaun) and music. The graphics have been reconstructed by using the information on some of the sprites and palettes found in the game's planar EGA files and the EXE. In the current version, big animation portraits are not included, only the tile sets and menu graphics.

This patcher/trainer allows you to play the hidden level set, as well as turn on some cheats.

This tool is tested with the [ROCKFORD.EXE that is 29963 bytes in size](https://www.xtcabandonware.com/game/786/rockford). It has not been tested with the version with infinite lives, since I have not found this version myself. It also does not work with the 18kb ROCKFORD.EXE due to encryption.

The VGA "Arcade" version of Rockford is currently not supported, since it is fairly rare.

## Enabling hidden levels
Either, copy all files from the folder ```gfx``` to your ROCKFORD directory. Then copy ```rockford_patcher.py``` into you your ROCKFROD directory and run it. You can just open it in Python's IDLE and hit F5. After this you can play the hidden levels by running ```ADDON.EXE```, but for this you'll need an old Dos machine or [DOSBox](https://www.dosbox.com/).

Alternatively, you can also just [download the ```addon.exe``` from here](https://www.mv.helsinki.fi/home/asahala/rockford/rockford-disk2.zip).

## For modders: Converting planar EGA to PNG and back
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
If you find the game too difficult (Mastertronic purposefully made it significantly more difficult than the original game!), you can set on god-mode by setting ```god_mode = True``` in the ```main()``` function. After this, colliding with enemies, being crushed by falling stones or being in explosions will not kill you, but instead spawn money around you! You can abuse this feature by hitting the key ```R```. This explodes most tiles and objects around you and replaces them with money. Try not blow up the exit door.

![alt text](https://www.mv.helsinki.fi/home/asahala/rockford/screenshots.png)

## How was the hidden content reconstructed?

***Order of the themes:*** The order of the themes is based on the collectible names fround from the EXE from offset 7A0 - 7EF. It is not 100% certain which themes they refer to, but with a little reasoning all except jewels and gems are somewhat obvious. Clubs are for luck, notes for music and cups for the player. I have put scuba and miner in this order based on the palette definitions in the EXE. There is only one theme with a black background (offsets 9E3 - 9F2), and I assume that this belongs to the miner more likely than the blue background at offsets 95B - 95A, which logically seems more likely to be for the scuba.

***Order of the levels:*** The levels have been extracted from CELLMAPS.BIN and aligned with the themes in their order of appearance. I am 100% certain that this is the correct order, since the themes and levels of the base game have ordered similarly. The levels are ordered as HUNTER, THEME6, COOK, THEME7 etc. In addition, level time limits and the amount of coins that has to be collected to open the exit door are 100% accurate, as are the point values that collecting coins contribute toward extra lifes. This amount is different in different levels, and the player gets bonus points for collecting coins after the exit door opens.

***Graphics:*** As for the lost graphics, the EXE only lists the tileset and animation file names (offsets 810 - 8DC). However, all tilesets except SPACE.FIL contain placeholder sprites for the player characters of all themes, including the hidden ones! These are ordered as follows: scuba diver, football player, musician, miner and leprechaun, which is contradictory to the ordering of level theme names in the EXE. But since the scuba sprite precedes the hunter in these tilesets, the order here must be arbitrary.

Unfortunately, it is impossible to recover the exact colors used in the original character sprites. In many tilesets, the lazy Amiga OCS -> EGA conversion also renders some pixels that are supposed to be of different colors as the same color. However, these problem pixels can be recovered by looking at these extra sprites in all the available tilesets, as well as the rare VGA version of Rockford. Alas, the VGA version's SCM files actually use a 16 color dynamic palette, which is different for each theme. This also prevents one from reconstucting the exact colors of the original sprites.

Only one frame of each hidden character sprite is available in the tilesets. I have used them as the reference point to draw the character animations. All enemies, tiles, walls etc. are pure ad hoc drawings, except for the collectibles that are based on their respective names in the EXE. Thanks to palette definitions that can be found from in the EXE at offsets 929 - 9F3, I could grasp a general idea of the color schemes in each theme. For example, that the miner should be pretty dark and luck fairly saturated.

Some tilesets have unused assets, such as the steam locomotive for Cowboy. I've reused these assets for the hidden themes, e.g. the miner uses this steam locomotive as the worm sprite.

To make editing the graphics files easier, I have re-adjusted all the hidden theme EGA palettes from the lazily converted Amiga OCS palettes into full EGA (this prevents losing colors due to two similar Amiga colors converging into one EGA color). As Rockford does not allow changing the background color to any other palette index (represented in octal numbers) than what's in the first offset in the EXE for each theme, all palettes except miner consist only of 15 colors. To guaranteed that black is available in all palettes, I have replaced one unused color in some tilesets with it. The original color is shown in the tilesets, but the game re-maps them into black automatically. This is, why e.g. the Scuba tileset seems to have bright green shadows, although in the game they are actually rendered in black.

## Want to collaborate?
I not a graphics artist. If you you are, and are interested in collaborating to finetune the tile sets and graphics in a way that they are more similar to the game's original style, reach me out. All the big animations for the hidden themes are still undone.

## Copyrights
Mastertronic still holds copyrights to the game, but it is generally considered abandonware and available to play at Playold and several other sites. [Rrockford-addon.zip](https://www.mv.helsinki.fi/home/asahala/rockford/rockford-disk2.zip) containing ```addon.exe``` (that is, prepatched ```rockford.exe``` for those who don't want to do it with Python) allows you only play the hidden content and does not include original game data. Therefore, in order to play the original levels with the original graphics, you will have to get Rockford from somewhere else, but who knows [where](https://www.xtcabandonware.com/game/786/rockford)?

## Version history
* 2023 - Version 1.0: Initial release.
* 2026 - Version 2.0: Added correct point values for collectibles.

