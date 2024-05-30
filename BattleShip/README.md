# BATTLESHIP
This is my first project I undertook in python. I wanted to create my own Battleship as I thoroughly enjoyed the game when I was younger and I believed it would be a good place to start to learn python and specifically object orientated programming in python

This game plays out in the terminal window as of now, I have not yet written a way for it to play in a seperate window as the main focus of this project was to learn the python syntax and language.

Compiling and running **main.py** will begin the game in the terminal window.

## How to Play
You will be playing against the computer and will place three battleships down. The Battleships will be 3, 4 and 5 elements long.
On the battle field, the characters:

__#__ : denotes a location that a ship is occupying

__X__ : denotes a location where a ship has been hit with a missile

__~__ : denotes an empty space on the battlefield not occupied by a ship (open sea)

## Toggles
Near the top of the **main.py** file, there is a toggle ```cpu_ships_visible = False```. This toggle can be set to ```True``` to display the CPU's battleships positions in between each round of play.
