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
After 
### The Player:
When placing the battleships at the beginning of the battle, the program checks that all the elements within the range of the size of the ship are 'free', in otherwords the element of the array is ```~```.
when the ship is placed, the location of the ship is added into a list ```ship_list_```. The same is done for the CPU when it has placed three battleships down on its "board".

The battlefield is a multidimensional array. When the player enters coordinates to fire a missile, the class converts that user input into a location on the array. The program checks if there is a ship there and then changes the element accordingly.

### The CPU:
When attacking, a random location is chosen within range of the array row and column size using the ```random``` library. This is then checked against the players battleground whether it hits a ship, hits a location that has already been fired at or misses. If the generated location is one that has already been fired at, another location is randomly generated. If it misses and hits open water, that location is marked as _ _checked_ _ (aka. '''/''') and next turn another random _ _free_ _ location is chosen in the array.

If the location chosen is occupied by the players ship, that Missile hits and on the next computers turn, several things happen:
1. That hit location is saved in a variable ```last_hit_coords```
2. Locations in the array adjacent to the ```last_hit_coords``` location are checked with the ```checkAroundHit()``` function to see if they have been fired upon already, if not, they are added to a list of locations ```surrounding_options_``` to test firing upon. If the chosen location is a miss, on the next turn, another location is chosen. If the location is a hit and adjacent to the last hit, the next location chosen will be adjecent again, following a straight line. This is done by inserting that next potential location at the beginning of the ```surrounding_options_``` list of potential ship locations.
3. This keeps going in the same direction until a ship has been sunk. If a ship is sunk, the ship is deleted from the ```ship_list_``` list (this happens for the player as well) and a flag is raised to the CPU and on it's next go it generates another random _ _free_ _ location to fire upon. If a ship wasnt sunk, then the ```last_hit_cords``` location is once again checked for potential ship locations with ```checkAroundHit()```. This is done incase the first location hit on a ship is its centre, the ```attack()``` function for the CPU will go down the length of the ship in one direction until it misses, then it will check on the otherside and around that _ _first_ _ hit location until a ship is sunk.

### The End of the Game
A function ```checkEndOfGame()``` is called after every attack made by either player or CPU. It checks the size of the ```ship_list``` list, if it is empty, then all ships have been sunk, a winner is announced and the program is terminated.
