![alt text](https://www.mv.helsinki.fi/home/asahala/rockford/themes.gif)

# Rockford patcher and trainer
Rockford was a Boulder Dash clone published by Mastertronic ltd. in 1987. The game included 20 levels divided into five difficulty levels each using their own graphical themes: hunter, cook, cowboy, space and doctor. 

Rockford also included 20 hidden levels which were unplayable. When I contacted Mastertronic in 2006, I was told that the were designed for a future add-on, which never released because they recided to do Rockford II instead. These levels were about to use five additional graphic sets called scuba, miner, player, luck and music.

This patcher/trainer allows you to play the hidden level set, as well as turn on some cheats. Unfortunately, as the graphics for these additional themes were never created, the additional levels are rendered using the base graphics set. Tested with the ROCKFORD.EXE that is 29963 bytes in size. Should work with other versions as well.

## How to use
Copy ```MENU.ADD``` to your ROCKFORD directory with the ```rockford_patcher.py```. Then simply run the script. It create patched copies of the ```CELLMAPS.BIN``` and ```ROCKFORD.EXE```. You can play the hidden levels by running ```ADDON.EXE```. I recommend using DOSBox for playing.

If you find the game too difficult, you can set on god-mode by setting the variable ```enable_godmode = True``` in the ```main()``` function. After this, colliding with enemies, falling stones or being in explosions will not kill you, but instead spawn money around you. You can abuse this feature by hitting the key ```R```. This explodes whatever is around you and replaces them with money. 

Just note, that if you use this hack next to the the exit door, you cannot finish the level and have to quit the game to proceed.

## Future stuff
Perhaps find a couple of people to design the hidden graphic sets. They are encoded in planar EGA.
