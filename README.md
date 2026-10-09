![alt text](https://i.imgur.com/hHH2m0m.png)

# Summary
This tool enables the hidden level set in Rockford with correct level times, money collection amounts and point values, as well as gives the hidden themes reconstructed tile sets. The tool also features a trainer that allows playing in god mode.

Download [Rockford Lost Worlds Version 3.0](https://www.mv.helsinki.fi/home/asahala/rockford/Rockford-Disk2-Version3.zip) and run it in DosBox. This version comes with two executables, ```ADDON.EXE``` runs the game with reconstructed graphics based on the Amiga screenshots. ```ORIGINAL.EXE``` runs the game with the EGA tilesets and animations for SCUBA and PLAYER that are 100% faithful to the original EGA graphics. However, these graphics look somewhat unfinished.

# State of development
* SCUBA, PLAYER and LUCK are fully completed with title cards, tilesets and animations.
* MUSIC and MINER contain all tiles to play the levels, but contain no animations that play upon level completion, loss and running out of time.
  
# Rockford and the (ambiguous) history of the missing levels
[Rockford](https://en.wikipedia.org/wiki/Rockford_(video_game)) was a Boulder Dash clone published by Mastertronic ltd. in [1987 and 1988 on multiple platforms](https://pixelatedarcade.com/games/rockford-the-arcade-game/releases), including Amiga and MS-DOS. The game included 20 levels divided into five difficulty settings or "worlds", each using their own themes: hunter, cook, cowboy, space and doctor.

Many did not know until the early 2000s that Rockford also included 20 **hidden levels** which were unplayable, but recoverable via [hacking the game files](https://www.mv.helsinki.fi/home/asahala/rockford/). The levels were included in ```CELLMAPS.BIN``` and the information on their names, time limits, collectibles and palettes in  ```ROCKFORD.EXE```. 

Using a hex editor, one could see references to these five hidden themes as SCUBA, PLAYER, MUSIC, LUCK and MINER on PC. From these I deduced in 2006 that these worlds featured a scuba diver, sports player, music conductor, some sort of a leprechaun, and a miner, who collected gems, cups, notes, clubs and jewels, respectively. After looking into the Amiga version's executable, which referred to the MUSIC as COND and to LUCK as GAMB, it was possible to deduce that these feature a music conductor and a gambler. One difference in the Amiga version also was that it referred to the jewels as diamonds. 

Since Adam Nielsen had created the [Camoto Studio](https://github.com/Malvineous/camoto-studio), which was able to open Rockford's planar EGA graphics files, it was discovered that the existing tilesets of the game contained placeholders for the player sprites for each of these themes. Since the EGA Rockford's palettes were apparently converted from the Amiga (which used dynamic 16 color palettes), the tilesets in the PC version contained less than 16 colors each. This was, because some Amiga colors converged into a single RGB value in case they existed too close to each other in the color space. The image below shows an example of the placeholder sprites with the palette from BODY.

![alt text](https://www.mv.helsinki.fi/home/asahala/rockford/sprites.png)

The same sprites exist in the VGA version as well, which of graphics files were parsed by Michael Eberlein. Unfortunately the VGA graphics format used in Rockford uses a dynamic 32 color palette, which means that we can only view the hidden themes' character sprites using the palettes from the existing five themes, which corrupts the color space. Therefore, the true colors of the sprites remain unknown.

Regardless, it were these sprites that confirmed for the first time that the ambiguous PLAYER theme was actually an American football player. As an interesting side note, the tilesets also contained the original Boulder Dash guy "Rockford" in two different colored shirts for an unknown reason. It is possible that the developers once planned on including a two-player mode, and the sprites for the player characters were transferred from version to another, ending up in the PC and the Amiga tilesets. However, I have never received an official confirmation on this.

## What happened to the hidden themes?
Now, it is a good question why the game files contain remnants of levels and graphics that never existed in the official releases. This is where everything gets ambiguous.

In 2006, when I contacted the people involved with Mastertronic (but not Rockford) in the 80s and the 90s, I was told that the the extra levels were designed for a possible future add-on, which never materialized. Since the game sold only 4000-5000 copies and distributing extra content on disks was expensive, this decision is understandable and makes perfect sense. Later in 2025 when I contacted Simon Plumbe from the Mastertronic collector's archive, he considered this also a remote possiblity, but was skeptical about it. He suggested that the hidden themes could have been the original five worlds for Rockford, which were later replaced by the ones we all know (perhaps because they were considered more interesting). What supports this view is, that some of these graphics are known to have existed in an early developer version of the Amiga Rockford, but the actual published game had them replaced with the five themes we all know.

Another of his suggestions was that the game was originally planned to include ten themes and 40 levels, but half of them were cut off as Mastertronic wanted to distribute the exactly same game on 8-bit and 16-bit platforms, the former not really supporting large amounts of files. Thus, the developers perhaps only preserved the themes they considered the best.

It is unknown whether the MINER and MUSIC themes were ever created for the Amiga version either, but the Atari ST version's box contains screenshots of the Amiga version's SCUBA, PLAYER and GAMBLER (LUCK) themes (see below). It is fairly funny that the Atari ST version actually came with the traditional five themes instead of the ones shown in the back of the box, and with graphics that were completely different from the Amiga version. Quite misleading marketing.

![Screenshots](https://i.imgur.com/CExXQRn.png)

Some of the screenshots are from the tileset showrooms that introduce player how all the objects look in the given theme. These rooms also play the introductory animation for the theme, which is never shown in the PC version, although they exist in the .CAR files. The introductory animations were replaced with the title cards in the 1988 PC release, shown in the world selection menu. Below is a screenshot of the HUNTER showroom on Amiga (right) and the reconstructed LUCK showroom on PC (left). 

![showroom](https://www.mv.helsinki.fi/home/asahala/rockford/addon_033.png)

In September 2026, Daniel Grimes, the developer of a [browser-executable version of Rockford](https://rockford.dbhq.uk) informed me that an early PC version of Rockford published in December 1987 contained two of the hidden level sets and their graphics. This was a 5.25" floppy disk version that comprised two disks, one containing the HUNTER, SCUBA and COOK themes, and the other containing the PLAYER and the COWBOY themes. This version had been available on Archive.org since 2014, but completely overlooked by me and other people involved in exploring and hacking this game. The tile sets are shown below, followed by in-game screenshots:

![Screenshots87](https://www.mv.helsinki.fi/home/asahala/rockford/screenshots1987.png)

![Game87](https://www.mv.helsinki.fi/home/asahala/rockford/game1987.png)

It appears that these graphic sets on PC are subpar compared to the original five themes. The color spaces are rather ugly and some of the tiles seem poorly drawn. Also at least some of animations seem worse in quality compared to those in HUNTER, COOK, COWBOY, SPACE and BODY. It can be also said that at least on the basis of the screenshots, the hidden themes look much less colorful on the Amiga version than the released five themes.

The lower quality and the fact that the 1987 5.25" floppy disk version contained two "hidden themes" and three original themes support Simon Plumbe's theory on the hidden themes having been cut off at some point. They may have been planned for an early release, but later simply replaced with the classic five themes since they were seen as more interesting. The reason why the references to the hidden themes exist in the game files might be as simple as the developers simply forgetting (or not caring about) to delete them from the executable. This seems more reasonable option than a planned future add-on.

One interesting feature in the 1987 5.25" floppy disk version is that it does not contain lives or the character selection menu. Instead it lets the player to skip from world to world using the W key. This suggests that this version is some kind of a prototype or a beta version. The world selection prompt string still exists in the 1988 Rockford executable, but it is never shown in the screen since the W key was disabled.

Since the ```CELLMAPS.BIN``` and ```ROCKFORD.EXE``` contains information on the hidden themes interleaved with the original five themes (the order is HUNTER, SCUBA, COOK, PLAYER, COWBOY, MUSIC, SPACE, LUCK, BODY, MINER), and because the 1987 PC version contains the first five of the aforementioned list, it seems possible that this was the original planned progression of the themes. This weird interleaving ordering might also explain why the unused levels were not removed from the ```CELLMAPS.BIN```: if the original plan was to first release five themes and later add five more, it would have been more reasonable to just order the levels accordingly. 

Progression-wise the levels in the hidden worlds are generally harder than the original one. In my subjective ranking between 1-5, I would say that the order from the easiest to the hardest is HUNTER (1.5), COOK (2.25), COWBOY (2.5), SCUBA (2.5), PLAYER (3.0), SPACE (3.25), MUSIC (3.25), DOCTOR (3.5), LUCK (4.0) and MINER (4.5). Concerning the last two worlds, LUCK is about as difficult as the DOCTOR, and the MINER is slightly harder in general. However, the final levels of these two worlds are out of the scale. Both levels are very long and involve frame perfect precision with no room for error. [The final level of LUCK](https://youtu.be/SSzL-h0l4fw) has an enemy dodging part that spans horizontally the whole map. The fact that Rockford's screen panning is a little bit jerky makes this extremely difficult. [The final level of MINER](https://www.youtube.com/watch?v=mD7d08dPesk) involves getting to a single jewel at the opposite side of the screen. Getting there is difficult, but getting back to the exit is nightmarish, since some of the enemies and fire/water taps you have to interact with will turn the whole level into a maze full of unpredictable chaos. Thus the journey back is different every time and difficult to practice.

As a side note, it seems that the developers recycled some ideas from the scrapped content. For example, the released BODY level two seems to be closely based on the PLAYER level one. See the screenshots below (thanks to Michael Eberlein for creating these). The PLAYER uses the COOK graphics set here.

![Compare](https://www.mv.helsinki.fi/home/asahala/rockford/comparison.png)

## Conclusions
It seems likely that the hidden themes were some kind of "Proto-Rockford" content, and that they were dropped out for better progression and visually more appealing tilesets. One question that remains is, whether the graphics for MUSIC and MINER were ever even created. Screenshots of them do not exist in the back of the Atari ST box, and thus there is no proof that they existed on the early Amiga versions either.

# Supported versions
This tool is tested with the ROCKFORD.EXE that is 29963 bytes in size. It has not been tested with the version with infinite lives, because I have not found this version myself. It does not work with the 18kb ROCKFORD.EXE due to file encryption.

The VGA "Arcade" version of Rockford is currently not supported, but I will perhaps add the support in the future.

## Enabling hidden levels
Either, copy all files from the folder ```gfx``` to your ROCKFORD directory. Then copy ```rockford_patcher.py``` into you your ROCKFORD directory and run it. You can just open it in Python's IDLE and hit F5. After this you can play the hidden levels by running ```ADDON.EXE```, but for this you'll need an old Dos machine or [DOSBox](https://www.dosbox.com/).

Alternatively, you can also just download the latest version (see the beginning of this readme). This version allows only playing the hidden content and does not contain the original game files for copyright reasons.

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
If you find the game too difficult, you can set a god-mode on by setting ```god_mode = True``` in the ```main()``` function. After this, colliding with enemies, being crushed by falling stones or being in explosions will not kill you, but instead spawn money around you! You can abuse this feature by hitting the key ```R```. This explodes most tiles and objects around you and replaces them with money. Try not blow up the exit door.

# How was the hidden content recovered and reconstructed?

This section briefly explains the history of this reconstruction.

![alt text](https://www.mv.helsinki.fi/home/asahala/rockford/preview.png)

***Level data***: Extraction of the level data is easy, since all the hidden levels are in the ```CELLMAPS.BIN```, which neatly interleaves the hidden content with the released levels ([see formatted CELLMAPS.BIN here](https://www.mv.helsinki.fi/home/asahala/rockford/cellmaps.html)). The relevant statistics for these levels can be extracted from ```ROCKFORD.EXE```. Full description of the hex values are available [here](https://www.mv.helsinki.fi/home/asahala/rockford/). All level data is 100% accurate and fully preserved.

***Order of the themes:*** The order of the themes is based on the collectible names found from the EXE from offset 7A0 - 7EF. It is not 100% certain which themes they refer to, but with a little reasoning all except jewels and gems are somewhat obvious. Clubs are for luck, notes for music and cups for the player. I have put scuba and miner in this order based on the palette definitions in the EXE. There is only one theme with a black background (offsets 9E3 - 9F2), and I assume that this belongs to the miner more likely than the blue background at offsets 95B - 95A, which logically seems more likely to be for the scuba.

The Amiga version provides more information on the themes, but is uses different names for a few of them. If the ```RF``` file is examined (offsets 5618-58B4), it lists them in the following order along with their collectibles: hunter (gold), scuba (gems), cook (apples), player (cups), cowboy (coins), conductor (notes), astronaut (suns), gambler (clubs), doctor (hearts) and miner (diamonds). It seems possible that the diamonds were changed into jewels in the PC version due to the lack of space for eight characters in the in the game's interface. 

In my first reconstruction I interpreted LUCK as a leprechaun, but in 2023 after digging into the Amiga files it was confirmed to be a gambler. This was later confirmed by the screenshots in the Atari ST back cover.

***Order of the levels:*** The levels have been extracted from CELLMAPS.BIN and aligned with the themes in their order of appearance. I am 100% certain that this is the correct order, since the themes and levels of the base game have ordered similarly, and the Atari ST back cover screenshots confirm them. In addition, level time limits, the amount of coins that has to be collected to open the exit door are 100% accurate, as are the point values that collecting coins contribute toward extra lives. This amount is different in different levels, and the player gets bonus points for collecting coins after the exit door opens.

***Graphics:*** The ```ROCKFORD.EXE``` only lists the tileset and animation file names (offsets 810 - 8DC). However, all tilesets except SPACE.FIL contain placeholder sprites for the player characters of all themes, including the hidden ones! These are ordered as follows: scuba diver, football player, musician, miner and gambler, which is contradictory to the ordering of level theme names in the EXE. But since the scuba sprite precedes the hunter in these tilesets, the order here must be arbitrary. 

Unfortunately, it is impossible to recover the exact colors used in the original character sprites, except for SCUBA and PLAYER thanks to the 1987 5.25" floppy disk version. In many tilesets, the lazy Amiga OCS -> EGA conversion also renders some pixels that are supposed to be of different colors as the same color. However, these problem pixels can be recovered by looking at these extra sprites in all the available tilesets.

Only one frame of each hidden character sprite is available in the tilesets. I have used them as the reference point to draw the character animations. All enemies, tiles, walls etc. are pure ad hoc drawings unless they are evidenced by the Atari ST back cover or the 1987 floppy disk version. Thanks to palette definitions that can be found in the EXE at offsets 929 - 9F3, I could grasp a general idea of the color schemes in each theme. For example, that the miner should be pretty dark.

To make editing the graphics files easier, I have re-adjusted all the hidden theme EGA palettes from the lazily converted Amiga OCS palettes into full EGA (this prevents losing colors due to two similar Amiga colors converging into a single EGA RGB value). As Rockford does not allow changing the background color to any other palette index (represented in octal numbers) than what's in the first offset in the EXE for each theme, all palettes except miner consist only of 15 colors. To guarantee that black is available in all palettes, I have replaced one unused color in some tilesets with it. The original color is shown in the tilesets, but the game re-maps them into black automatically. This is, why e.g. the SCUBA tileset seems to have bright green shadows, although in the game they are actually rendered in black.

## What is exactly known about the hidden graphics sets?
Since I have now recovered some objective information on the lost graphics in the Atari ST box and the 1987 EGA version. The following is known for sure:

**Scuba** and **Player** graphics are fully recovered as of October 2026 thanks to the discovered 1987 EGA version. The Patcher comes now with the exact tilesets and animations and the reconstructed ones, since the original graphics look fairly dull and unfinished.

**Luck** is actually a gambler, not a leprechaun as I thought in 2023 in the initial version. He collects green four-leaf clovers. The boulders are black eight-balls. The good worm consists of red playing cards and the bad one of black ones. One of the enemies is probably a gold nugget, but it is impossible to say for certain. Yet this theme is about 75% accurate to the Amiga screenshots.

**Music** and **Miner** are fully reconstructed. Only a single frame of the player sprites are original, but with guessed color palette. It remains unknown if these graphics sets ever existed.

## Want to collaborate?
I not a graphics artist. If you you are, and are interested in collaborating to finetune the tile sets and graphics in a way that they are more similar to the game's original style, reach me out. Also the animation screens for Music and Miner are still undone. 

# Copyrights
Mastertronic / First Star Software still holds copyrights of the game, but it is available at many retro game sites and playable at Playold on browser. For copyright reasons the Original game graphics (HUNTER, COOK, COWBOY, SPACE, BODY) are not included in this Github. In case you want to use the Patcher yourself, you will have to get Rockford from somewhere, but who knows [where](https://www.xtcabandonware.com/game/786/rockford).

# Credits
* Michael Eberlein: information on the VGA graphics format
* Daniel Grimes: informing me about the 1987 release with Scuba and Player tilesets
* Simon Plumbe: some details on the history of Mastertronic and Rockford
* Adam Nielsen: Camoto Studio and the first access into the planar EGA files
* Atari Legend: Atari ST box scans in a reasonable resolution

# Version history
* 2023 - Version 1.0: Initial release.
* April 2026 - Version 2.0: Added correct point values for collectibles. I had completely overlooked these before! You may still download the old [Rockford-addon.zip](https://www.mv.helsinki.fi/home/asahala/rockford/rockford-disk2.zip)
* October 2026 - Version 3.0: Improved accuracy of the Scuba and Player tilesets.

