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

## Trainer
If you find the game too difficult, you can set on god-mode by setting ```god_mode = True``` in the ```main()``` function. After this, colliding with enemies, falling stones or being in explosions will not kill you, but instead spawn money around you. You can abuse this feature by hitting the key ```R```. This explodes whatever is around you and replaces them with money. Try not blow up the exit door.

![alt text](https://www.mv.helsinki.fi/home/asahala/rockford/screenshot.png)

## Want to collaborate?
I not a graphics artist. If you you are, and are interested in collaborating to finetune the tile sets and graphics in a way that they are more similar to the game's original style, reach me out. All the big animations for the hidden themes are still undone.

