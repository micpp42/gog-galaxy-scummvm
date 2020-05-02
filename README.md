# GOG Galaxy ScummVM Integration Plugin
This is a plugin for GOG Galaxy 2.0 that will let you launch whatever games you have set up in ScummVM through GOG Galaxy
## How do I install it

Download the ZIP file from the Releases tab

Make a folder named "scummvm" (or really whatever you like) in the folder `C:\Users\<your username>\AppData\Local\GOG.com\Galaxy\plugins\installed`

Unzip into this new folder

Fire up GOG Galaxy, go to the Integrations screen, and this one will be listed under "Amiga"

## How does it work?

The plugin relies on you having already set the games up and got them working through the ScummVM launcher. Essentially I am reading your scummvm.ini file for games, and passing the game names etc to GOG. I'm basing things on the default ScummVM naming pattern, where things are like "Game Name (Platform/Language)", essentially I split off the name before the brackets and that's what I pass. Then for running the games I just call the ScummVM exe and pass it the game ID and everything should work!

## Known issues
### Default locations of ScummVM and the config file
By default, I'm assuming that your ScummVM is installed in `C:\Program Files\ScummVM\` and that your scummvm.ini file is  `%APPDATA%\ScummVM\scummvm.ini`. This should be how things come out by default if you're not changing the settings and such when you install (please let me know if I'm wrong about this). If you need to change it, at the moment it's hardcoded into plugin.py but should be easy enough for you to find and edit if you need to. Future change would be adding a config file so you can customise it
### The platform shows up as "Amiga"
Unfortunately, GOG don't have a ScummVM platform listed, and don't have any ability to set custom platforms. I've gone with Amiga on the loose logic that some of the games ScummVM can run are Amiga versions.
### Games not matching, showing up as Unknown game etc
This one is a bit out of my hands, sadly. All I send to GOG is the name of the game that I got out of the scummvm.ini file, and it's then up to GOG Galaxy to match this up with the metadata they've got in their database. This is subject to some flaws (e.g. games named slightly differently, like is it King's Quest or King's Quest 1), and relies on their database being complete (would you believe that at the time I'm writing this they seem to be missing Monkey Island). The only advice I can offer here is that if you change the name of the game in the ScummVM launcher to match what GOG expects then you may have some luck in getting it to match properly - and failing that, if something is showing up missing artwork or as "unknown game" it is possible to fix the name, set artwork etc manually through GOG.
