![alt text](https://www.mv.helsinki.fi/home/asahala/rockford/themes.gif)

# Rockford patcher and trainer
[Rockford](https://en.wikipedia.org/wiki/Rockford_(video_game)) was a Boulder Dash clone published by Mastertronic ltd. in 1988 for DOS. The game included 20 levels divided into five difficulty settingsm, each using their own themes: hunter, cook, cowboy, space and doctor. 

Rockford also included 20 hidden levels which were unplayable. When I contacted Mastertronic in 2006, I was told that they were designed for a possible future add-on, which was never released because they recided to do Rockford II instead. These levels were about feature five additional graphic sets called scuba, miner, player (sports), luck (leprechaun) and music.

This patcher/trainer allows you to play the hidden level set, as well as turn on some cheats. Unfortunately, as the graphics for these additional themes were never created, the additional levels are rendered using the base graphics set. 

Tested with the ROCKFORD.EXE that is 29963 bytes in size. Should work with other versions as well (except for the godmode).

## Enabling hidden levels
Copy ```MENU.ADD``` to your ROCKFORD directory with the ```rockford_patcher.py```. Then simply run the script. After this you can play the hidden levels by running ```ADDON.EXE```.

## Trainer
If you find the game too difficult, you can set on godmode by setting ```enable_godmode = True``` in the ```main()``` function. After this, colliding with enemies, falling stones or being in explosions will not kill you, but instead spawn money around you. You can abuse this feature by hitting the key ```R```. This explodes whatever is around you and replaces them with money. If you use this hack next to the the exit door, you cannot finish the level and have to quit the game to proceed.

## Future stuff
Perhaps find a couple of people to design the hidden graphic sets. They are encoded in planar EGA.
