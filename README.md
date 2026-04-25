![alt text](https://i.imgur.com/hHH2m0m.png)

# Summary
This tool enables the hidden level set in Rockford with correct level times, money collection amounts and point values, as well as gives the hidden themes reconstructed tile sets. The tool also features a trainer that allows playing in god mode.

# State of development
* Gambler, Scuba and Player themes are completed. Gambled and Scuba contain also all assets that are not required in their level sets (worms, taps etc.).
* The two remaining themes contain all tiles necessary to play the levels, but they will use animations from the original five themes on level completion, loss and running out of time.
* Music and Miner graphics will be reworked at some point.
* Note that the zipped Disk 2 does not contain the latest graphics yet! For them you need to use the ones in the gfx folder and use the patcher on your ```rockford.exe```

# Rockford and the history of the missing levels
[Rockford](https://en.wikipedia.org/wiki/Rockford_(video_game)) was a Boulder Dash clone published by Mastertronic ltd. in [1987 and 1988 on multiple platforms](https://pixelatedarcade.com/games/rockford-the-arcade-game/releases), including Amiga and MS-DOS. The game included 20 levels divided into five difficulty settings or "worlds", each using their own themes: hunter, cook, cowboy, space and doctor. 

Many did not know until the early 2000s that Rockford also included 20 **hidden levels** which were unplayable, but recoverable via hacking the game files (ROCKFORD.EXE and CELLMAPS.BIN). When I contacted in 2006 people involved with Mastertronic back in the days, I was told that the the extra levels were designed for a possible future add-on, which never materialized. Since the game sold only 4000-5000 copies and distributing extra content on disks was expensive, this decision is understandable. When I contacted Simon Plumbe from the Mastertronic collector's archive, he considered this also a possiblity, but he also mentioned that these hidden themes could have been the original five worlds for Rockford, which were later replaced by the ones we all know (perhaps because they were considered more interesting). What supports this view is, that these graphics are known to have existed on an early developer version of Amiga Rockford, but the actual published game had replaced them.

One reason for cutting this content off could have simply been that the developers wanted to fit the whole game into a single disk (Amiga release took the entire 880 kb floppy disk) to decrease the distribution costs. Simon Plumbe suggested that perhaps the developers simply forgot (or did not care) to delete the references to the removed content in the executable before distributing it.

The names of these lost worlds are recoverable from ROCKFORD.EXE with a hex editor, where they are referred to as SCUBA, PLAYER, MUSIC, LUCK and MINER. The Amiga version calls them SCUBA, PLAYER, COND, GAMB and MINER. From these we can deduce that these worlds featured a scuba diver, sports player, music conductor, gambler, and miner, who collected gems, cups, notes, clubs and jewels, respectively. The Amiga version refers to the jewels as diamonds. 

For the PC's EGA and VGA versions, all graphics that exist for these lost worlds are the player character sprites (one frame each), which are hidden in the .FIL files in the EGA version and in the .SCM files in the VGA version. Also the general color schemes can be recovered from ROCKFORD.EXE. The sprites for EGA version are shown below (with distorted palettes), including the classic Boulder Dash guy, which of purpose here is unknown. However, as there are placeholders for two classic Boulder Dash guys in different colored shirts, it cannot be excluded that the developers once planned on adding a two-player mode. These sprites confirm that the PLAYER was originally an American football player.

![alt text](https://www.mv.helsinki.fi/home/asahala/rockford/sprites.png)

Despite these are the only sprites that exist on PC, as said above, it is known that the tile sets and animations were fully created at least for SCUBA, PLAYER and LUCK on Amiga. This is proven by screenshots of these themes in the back cover of the Atari ST release of Rockford (funny enough, they used Amiga screenshots of unreleased graphics to promote an Atari ST game!). Unfortunately the screenshots are small and blurry, since they have been photographed from the screen. The pictures of this box are also generally a low quality and one cannot see clearly most of the tiles. In comparison to the colorful published themes, the hidden ones seem to use a very dark color space, which does not really correspond to the palette information shown in the PC executable (e.g. PLAYER should have a green background and SCUBA should have blue). It is likely that the MUSIC and MINER themes also fully existed, but no screenhots of them survive. Whether these tile sets were ever converted to PC fully remains unknown. Below is the best available photo of the hidden graphics.

![Screenshots](https://i.imgur.com/CExXQRn.png)

In terms of difficulty, the levels in the extra worlds are generally harder than the original one. In my subjective ranking between 1-5, I would say that the order from the easiest to the hardest is HUNTER (1.5), COOK (2.25), COWBOY (2.5), SCUBA (2.5), PLAYER (3.0), SPACE (3.25), MUSIC (3.25), DOCTOR (3.5), LUCK (4.0) and MINER (4.5). Concerning the last two worlds, LUCK is generally about as difficult as the DOCTOR, and the MINER is slightly harder in general. However, the final levels of these two worlds are out of the scale. Both levels are very long and involve frame perfect precision with no room for error. [The final level of LUCK](https://youtu.be/SSzL-h0l4fw) has an enemy dodging part that spans horizontally the whole map. The fact that Rockford's screen panning is a little bit jerky makes this extremely difficult. [The final level of MINER](https://www.youtube.com/watch?v=mD7d08dPesk) involves getting to a single jewel at the opposite side of the screen. Getting there is difficult, but getting back to the exit is nightmarish, since some of the enemies and fire/water taps you have to interact with will turn the whole level into a maze full of unpredictable chaos. Thus the journey back is different every time and cannot be practiced.

# Supported versions
This tool is tested with the ROCKFORD.EXE that is 29963 bytes in size. It has not been tested with the version with infinite lives, because I have not found this version myself. It does not work with the 18kb ROCKFORD.EXE due to file encryption.

The VGA "Arcade" version of Rockford is currently not supported, but I will perhaps add the support in the future.

## Enabling hidden levels
Either, copy all files from the folder ```gfx``` to your ROCKFORD directory. Then copy ```rockford_patcher.py``` into you your ROCKFORD directory and run it. You can just open it in Python's IDLE and hit F5. After this you can play the hidden levels by running ```ADDON.EXE```, but for this you'll need an old Dos machine or [DOSBox](https://www.dosbox.com/).

Alternatively, you can also just [download the ```addon.exe``` from here](https://www.mv.helsinki.fi/home/asahala/rockford/rockford-disk2.zip). This version allows only playing the hidden content and does not contain the original game files for copyright reasons.

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
If you find the game too difficult (Mastertronic purposefully made the extra levels significantly more difficult than the original game!), you can set on god-mode by setting ```god_mode = True``` in the ```main()``` function. After this, colliding with enemies, being crushed by falling stones or being in explosions will not kill you, but instead spawn money around you! You can abuse this feature by hitting the key ```R```. This explodes most tiles and objects around you and replaces them with money. Try not blow up the exit door.

![alt text](https://i.imgur.com/7kwGn2t.png)

## How was the hidden content recovered and reconstructed?

***Level data***: Extraction of the level data is easy, since all the hidden levels are in the CELLMAPS.BIN, which neatly interleaves the hidden content with the released levels ([see formatted CELLMAPS.BIN here](https://www.mv.helsinki.fi/home/asahala/rockford/cellmaps.html)). The relevant statistics for these levels can be extracted from ROCKFORD.EXE. Full description of the hex values are available [here](https://www.mv.helsinki.fi/home/asahala/rockford/). All level data is 100% accurate and fully preserved.

***Order of the themes:*** The order of the themes is based on the collectible names fround from the EXE from offset 7A0 - 7EF. It is not 100% certain which themes they refer to, but with a little reasoning all except jewels and gems are somewhat obvious. Clubs are for luck, notes for music and cups for the player. I have put scuba and miner in this order based on the palette definitions in the EXE. There is only one theme with a black background (offsets 9E3 - 9F2), and I assume that this belongs to the miner more likely than the blue background at offsets 95B - 95A, which logically seems more likely to be for the scuba.

The Amiga version provides more information on the themes, but is uses different names for a few of them. If the RF file is examined (offsets 5618-58B4), it lists them in the following order along with their collectibles: hunter (gold), scuba (gems), cook (apples), player (cups), cowboy (coins), conductor (notes), astronaut (suns), gambler (clubs), doctor (hearts) and miner (diamonds). It seems possible that the diamonds were changed into jewels in the PC version due to the lack of space for eight characters in the in the game's interface. I also seems very likely that my original interpretation of LUCK as a leprechaun on basis of the PC version is incorrect, and this theme shoul in fact be a gambler!

***Order of the levels:*** The levels have been extracted from CELLMAPS.BIN and aligned with the themes in their order of appearance. I am 100% certain that this is the correct order, since the themes and levels of the base game have ordered similarly. The levels are ordered as HUNTER, SCUBA, COOK, PLAYER, ... etc. In addition, level time limits and the amount of coins that has to be collected to open the exit door are 100% accurate, as are the point values that collecting coins contribute toward extra lifes. This amount is different in different levels, and the player gets bonus points for collecting coins after the exit door opens.

***Graphics:*** As for the lost graphics, the EXE only lists the tileset and animation file names (offsets 810 - 8DC). However, all tilesets except SPACE.FIL contain placeholder sprites for the player characters of all themes, including the hidden ones! These are ordered as follows: scuba diver, football player, musician, miner and leprechaun, which is contradictory to the ordering of level theme names in the EXE. But since the scuba sprite precedes the hunter in these tilesets, the order here must be arbitrary. 

Unfortunately, it is impossible to recover the exact colors used in the original character sprites. In many tilesets, the lazy Amiga OCS -> EGA conversion also renders some pixels that are supposed to be of different colors as the same color. However, these problem pixels can be recovered by looking at these extra sprites in all the available tilesets, as well as the rare VGA version of Rockford. Alas, the VGA version's SCM files actually use a 32 color dynamic palette, which is different for each theme. This also prevents one from reconstucting the exact colors of the original sprites.

Only one frame of each hidden character sprite is available in the tilesets. I have used them as the reference point to draw the character animations. All enemies, tiles, walls etc. are pure ad hoc drawings, except for the collectibles that are based on their respective names in the EXE. Thanks to palette definitions that can be found from in the EXE at offsets 929 - 9F3, I could grasp a general idea of the color schemes in each theme. For example, that the miner should be pretty dark and luck fairly saturated.

To make editing the graphics files easier, I have re-adjusted all the hidden theme EGA palettes from the lazily converted Amiga OCS palettes into full EGA (this prevents losing colors due to two similar Amiga colors converging into one EGA color). As Rockford does not allow changing the background color to any other palette index (represented in octal numbers) than what's in the first offset in the EXE for each theme, all palettes except miner consist only of 15 colors. To guaranteed that black is available in all palettes, I have replaced one unused color in some tilesets with it. The original color is shown in the tilesets, but the game re-maps them into black automatically. This is, why e.g. the Scuba tileset seems to have bright green shadows, although in the game they are actually rendered in black.

## What is exactly known about the hidden graphics sets?

Since I have now recovered some objective information on the lost graphics in the Amiga version. We know for sure the following:

**Scuba** collects diamond shaped yellow gems and the boulders are blue seashels. Magic walls feature star fishes. One enemy is probably a dark red anglerfish, but the screenshots are too blurry to say for certain.

**Player** collects golden cups, which are surprisingly similar to my original reconstruction. The boulders are black bowling balls and one of the worm's heads seems to be blue football helmet.

**Luck** is actually a gambler, not a leprechaun as I thought in 2023 in the initial version. He collects green four-leaf clovers. The boulders are black eight-balls. The good worm consists of red playing cards and the bad one of black ones. One of the enemies is probably a gold nugget, but it is impossible to say for certain.

## Want to collaborate?
I not a graphics artist. If you you are, and are interested in collaborating to finetune the tile sets and graphics in a way that they are more similar to the game's original style, reach me out. All the big animations for the hidden themes are still undone.

## Copyrights
Mastertronic / First Star Software still holds copyrights of the game, but it is available at many retro game sites and playable at Playold on browser. The [Rockford-addon.zip](https://www.mv.helsinki.fi/home/asahala/rockford/rockford-disk2.zip) containing ```addon.exe``` (that is, prepatched ```rockford.exe``` for those who don't want to do it with Python) allows you only play the hidden content and does not include original game data. Therefore, in order to play the original levels with the original graphics, you will have to get Rockford from somewhere else, but who knows [where](https://www.xtcabandonware.com/game/786/rockford)?

## Version history
* 2023 - Version 1.0: Initial release.
* 2026 - Version 2.0: Added correct point values for collectibles. I had completely overlooked these before!

## Future plans
Redraw the graphics using the Atari ST evidence.
