# BATTLESHIP
This is my first project I undertook in python. I wanted to create my own Battleship as I thoroughly enjoyed the game when I was younger and I believed it would be a good place to start to learn python and specifically object orientated programming in python

This game plays out in the terminal window as of now, I have not yet written a way for it to play in a seperate window as the main focus of this project was to learn the python syntax and language.

Compiling and running **main.py** will begin the game in the terminal window.

## How to Play
You will be playing against the computer and will place three battleships down. The Battleships will be 3, 4 and 5 elements long.
On the battle field, the characters:

__#__ : denotes a location that a ship is occupying

__X__ : denotes a location where a ship has been hit with a missile

__~__ : denotes an empty space on the battlefield not occupied by a ship (_ _free_ _ open sea location)

__/__ : denotes a location where a missile has been fired, but missed (_ _checked_ _ location

## Toggles
Near the top of the **main.py** file, there is a toggle ```cpu_ships_visible = False```. This toggle can be set to ```True``` to display the CPU's battleships positions in between each round of play.

## Functionality
### The Player:
The battlefield is obviously a multidimensional array. When the player enters coordinates to fire a missile, the class converts that user input into a location on the array. The program checks if there is a ship there and then changes the element accordingly.

When placing the battleships at the beginning of the battle, the program checks that all the elements within the range of the size of the ship are 'free', in otherwords the element of the array is **~**.

### The CPU:
When attacking, a random location is chosen within range of the array row and column size using the ```random``` library. This is then checked against the players battleground whether it hits a ship, hits a location that has already been fired at or misses. If the generated location is one that has already been fired at, another location is randomly generated. If it misses and hits open water, that location is marked as _ _checked_ _ (aka. **/**) and next turn another random _ _free_ _ location is chosen on the board
