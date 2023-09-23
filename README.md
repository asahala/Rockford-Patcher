![alt text](https://www.mv.helsinki.fi/home/asahala/rockford/banner2.png)

# Rockford patcher and trainer
[Rockford](https://en.wikipedia.org/wiki/Rockford_(video_game)) was a Boulder Dash clone published by Mastertronic ltd. in 1988 for DOS. The game included 20 levels divided into five difficulty settings, each using their own themes: hunter, cook, cowboy, space and doctor. 

Rockford also included 20 **hidden levels** which were unplayable. When I contacted Mastertronic in 2006, I was told that they were designed for a possible future add-on, which was never released because they recided to do Rockford II instead. These levels were about feature five additional graphic sets called scuba, miner, player (sports), luck (leprechaun) and music.

This patcher/trainer allows you to play the hidden level set, as well as turn on some cheats. Unfortunately, as the graphics for these additional themes were never created, the additional levels are rendered using the base graphics set. 

Tested with the ROCKFORD.EXE that is 29963 bytes in size. Should work with other versions as well (except for the god-mode). This is the version that has four lives instead of infinite lives.

## Enabling hidden levels
Copy all files from the folder ```gfx``` to your ROCKFORD directory. Then copy ```rockford_patcher.py``` into you your ROCKFROD directory and run it. After this you can play the hidden levels by running ```ADDON.EXE```.

## Trainer
If you find the game too difficult, you can set on god-mode by setting ```god_mode = True``` in the ```main()``` function. After this, colliding with enemies, falling stones or being in explosions will not kill you, but instead spawn money around you. You can abuse this feature by hitting the key ```R```. This explodes whatever is around you and replaces them with money. Try not blow up the exit door.

![alt text](https://www.mv.helsinki.fi/home/asahala/rockford/screenshots.png)

