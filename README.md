![alt text](https://www.mv.helsinki.fi/home/asahala/rockford/banner3.png)

# Summary
This tool enables the hidden level set in Rockford with correct level times, money collection amounts and point values, as well as gives the hidden themes reconstructed tile sets. In addition the tools features a trainer that allows playing in god mode.

# Rockford and the history of the missing levels
[Rockford](https://en.wikipedia.org/wiki/Rockford_(video_game)) was a Boulder Dash clone published by Mastertronic ltd. in [1987 and 1988 on multiple platforms](https://pixelatedarcade.com/games/rockford-the-arcade-game/releases), including Amiga and MS-DOS. The game included 20 levels divided into five difficulty settings or "worlds", each using their own themes: hunter, cook, cowboy, space and doctor. 

Many did not know until the early 2000s that Rockford also included 20 **hidden levels** which were unplayable, but recoverable via hacking the game files. When I contacted the people involved with Mastertronic in 2006, I was told that "they [the extra levels] were designed for a possible future add-on, which was never released as the developers decided to focus on releasing Rockford II instead" (which was never released to my knowledge). The original Amiga version contains a hidden message (aimed for crackers who intended to remove the copy protection) that implies that the Amiga version was rushed. It remains unclear whether the original plan was to release all the themes at once for the Amiga version: "I must apologise for the use of amigados file format, but we were in a bit of rush and we needed to get it out on time, so we couldn't be bothered to use Trackdisk or do our own disk format. Never fear though! I have nearly perfected my mega-hard-to-hack disk format that I may use on future Melbourne House/Mastertronic games, to add a little spice to your lives!"

These days the existence of this hidden content is [well-acknowledged](https://moddingwiki.shikadi.net/wiki/Rockford), and it is present in both PC versions of the game, EGA and VGA, as well as the original Amiga OCS version (cf. MAPS file that is exactly the same as the CELLMAPS.BIN on PC).

The game files suggest that these levels were supposed to feature five additional graphic sets called scuba, miner, player (sports), luck (leprechaun/gambler) and music. Although the levels, names of the worlds and their collectibles are fully recoverable, only a small fraction of the actual graphics can be found in the game files: namely the general palettes and the player character sprites. 

Interestingly, the Atari ST version of Rockford features three of these hidden themes in its [back cover](https://www.atarimania.com/game-atari-st-rockford-the-arcade-game_10427.html), but the box states that they are from the Amiga version. This still proves that the graphic sets were fully made for some versions of the game, at least for Amiga, but for some reason they were left for a future release that never materialized.

Below is an example of the hidden sprites found in the PC EGA version's BODY.FIL (the palette is correct only for the doctor sprite). The classic "Rockford" sprite with the striped shirt occurs in all tilesets, but its purpose is unknown. Since it replaces the "PLAYER" sprite in some tilesets, it is possible that the football player was originally supposed to use the classic Boulder Dash tileset, but ultimately it was replaced by a new theme.

![alt text](https://www.mv.helsinki.fi/home/asahala/rockford/sprites.png)

Since the "Rockford" sprite also occurs in two different color variations elsewhere in the tileset, it is possible that there were plans to add a two-player mode. Unfortunately, I did not ask about this in 2006 when I was in conctact with the publisher, as I was still unable to parse the planar EGA files. However, this is probably something only the programmers of the game could answer.

# Supported versions
This tool is tested with the [ROCKFORD.EXE that is 29963 bytes in size](https://www.xtcabandonware.com/game/786/rockford). It has not been tested with the version with infinite lives, since I have not found this version myself. It also does not work with the 18kb ROCKFORD.EXE due to encryption.

The VGA "Arcade" version of Rockford is currently not supported, since it is fairly rare.

## Enabling hidden levels
Either, copy all files from the folder ```gfx``` to your ROCKFORD directory. Then copy ```rockford_patcher.py``` into you your ROCKFORD directory and run it. You can just open it in Python's IDLE and hit F5. After this you can play the hidden levels by running ```ADDON.EXE```, but for this you'll need an old Dos machine or [DOSBox](https://www.dosbox.com/).

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

## How was the hidden content recovered and reconstructed?

***Level data***: Extraction of the level data is easy, since all the hidden levels are in the CELLMAPS.BIN, which neatly interleaves the hidden content with the released levels ([see formatted CELLMAPS.BIN here](https://www.mv.helsinki.fi/home/asahala/rockford/cellmaps.html)). The relevant statistics for these levels can be extracted from ROCKFORD.EXE. Full description of the hex values are available [here](https://www.mv.helsinki.fi/home/asahala/rockford/). All level data is 100% accurate and fully preserved.

***Order of the themes:*** The order of the themes is based on the collectible names fround from the EXE from offset 7A0 - 7EF. It is not 100% certain which themes they refer to, but with a little reasoning all except jewels and gems are somewhat obvious. Clubs are for luck, notes for music and cups for the player. I have put scuba and miner in this order based on the palette definitions in the EXE. There is only one theme with a black background (offsets 9E3 - 9F2), and I assume that this belongs to the miner more likely than the blue background at offsets 95B - 95A, which logically seems more likely to be for the scuba.

The Amiga version provides more information on the themes, but is uses different names for a few of them. If the RF file is examined (offsets 5618-58B4), it lists them in the following order along with their collectibles: hunter (gold), scuba (gems), cook (apples), player (cups), cowboy (coins), conductor (notes), astronaut (suns), gambler (clubs), doctor (hearts) and miner (diamonds). It seems possible that the diamonds were changed into jewels in the PC version due to the lack of space for eight characters in the in the game's interface. I also seems very likely that my original interpretation of LUCK as a leprechaun on basis of the PC version is incorrect, and this theme shoul in fact be a gambler!

***Order of the levels:*** The levels have been extracted from CELLMAPS.BIN and aligned with the themes in their order of appearance. I am 100% certain that this is the correct order, since the themes and levels of the base game have ordered similarly. The levels are ordered as HUNTER, THEME6, COOK, THEME7 etc. In addition, level time limits and the amount of coins that has to be collected to open the exit door are 100% accurate, as are the point values that collecting coins contribute toward extra lifes. This amount is different in different levels, and the player gets bonus points for collecting coins after the exit door opens.

***Graphics:*** As for the lost graphics, the EXE only lists the tileset and animation file names (offsets 810 - 8DC). However, all tilesets except SPACE.FIL contain placeholder sprites for the player characters of all themes, including the hidden ones! These are ordered as follows: scuba diver, football player, musician, miner and leprechaun, which is contradictory to the ordering of level theme names in the EXE. But since the scuba sprite precedes the hunter in these tilesets, the order here must be arbitrary. 

Unfortunately, it is impossible to recover the exact colors used in the original character sprites. In many tilesets, the lazy Amiga OCS -> EGA conversion also renders some pixels that are supposed to be of different colors as the same color. However, these problem pixels can be recovered by looking at these extra sprites in all the available tilesets, as well as the rare VGA version of Rockford. Alas, the VGA version's SCM files actually use a 32 color dynamic palette, which is different for each theme. This also prevents one from reconstucting the exact colors of the original sprites.

Only one frame of each hidden character sprite is available in the tilesets. I have used them as the reference point to draw the character animations. All enemies, tiles, walls etc. are pure ad hoc drawings, except for the collectibles that are based on their respective names in the EXE. Thanks to palette definitions that can be found from in the EXE at offsets 929 - 9F3, I could grasp a general idea of the color schemes in each theme. For example, that the miner should be pretty dark and luck fairly saturated.

To make editing the graphics files easier, I have re-adjusted all the hidden theme EGA palettes from the lazily converted Amiga OCS palettes into full EGA (this prevents losing colors due to two similar Amiga colors converging into one EGA color). As Rockford does not allow changing the background color to any other palette index (represented in octal numbers) than what's in the first offset in the EXE for each theme, all palettes except miner consist only of 15 colors. To guaranteed that black is available in all palettes, I have replaced one unused color in some tilesets with it. The original color is shown in the tilesets, but the game re-maps them into black automatically. This is, why e.g. the Scuba tileset seems to have bright green shadows, although in the game they are actually rendered in black.

## What is exactly known about the hidden graphics sets?

Since I have now recovered some objective information on the lost graphics in the Amiga version, the reconstructions in this patcher are outdated. We know for sure the following:

**Scuba** collects diamond shaped yellow gems and the boulders are blue seashels. Magic walls feature star fishes. One enemy is probably a dark red anglerfish.

**Player** collects golden cups, which are surprisingly similar to my original reconstruction. The boulders are black bowling balls and the the worms' head seem to be blue footbal helmets.

**Luck** is actually a gambler, not a leprechaun. He collects green four-leaf clovers. The boulders are black eight-balls. The good worm consists of red playing cards and the bad one of black ones. One of the enemies is probably a gold nugget.

## Want to collaborate?
I not a graphics artist. If you you are, and are interested in collaborating to finetune the tile sets and graphics in a way that they are more similar to the game's original style, reach me out. All the big animations for the hidden themes are still undone.

## Copyrights
Mastertronic / First Star Software still holds copyrights of the game, but it is generally considered abandonware and available to play at Playold and several other sites. [Rrockford-addon.zip](https://www.mv.helsinki.fi/home/asahala/rockford/rockford-disk2.zip) containing ```addon.exe``` (that is, prepatched ```rockford.exe``` for those who don't want to do it with Python) allows you only play the hidden content and does not include original game data. Therefore, in order to play the original levels with the original graphics, you will have to get Rockford from somewhere else, but who knows [where](https://www.xtcabandonware.com/game/786/rockford)?

## Version history
* 2023 - Version 1.0: Initial release.
* 2026 - Version 2.0: Added correct point values for collectibles. I had completely overlooked these before!

## Future plans
Redraw the graphics using the Atari ST evidence.
