# HEADERS #####################################
import random
import copy
import time
# import tkinter as tk
from battleground import BattleGround
from ship import Ship
from CPUBattlePlacement import CPU_Placement
# from GUI import MyGUI

#GLOBAL VALS###################################
# ship_size = 5   #for testing

###TOGGLES FOR GAMEPLAY########################
cpu_ships_visible = False  #Set True to print CPU's ship locations on map

###############################################
# """
# A GAME OF BATTLESHIP.
#     There are 3 ships of lengths 3, 4 and 5 that you will need to place in your battlefield. 
#     The CPU will place the same amount of ships
    
#     On the battlefield the characters:
#     `#` denotes a location that a ship is occupying
#     'X' denotes a location where a ship has been hit with a Missile
#     '~' denotes an empty space on the battlefield not occupied by a ship (open sea)
    
#     Have Fun!
# """


def main():
    player = BattleGround()
    enemy = CPU_Placement()
    
    printMap(player.environment_,True)

    for i in range(3): 
        print("SIZE OF SHIP: ",i+3)
        createAndPlaceShip(player,i)
        printMap(player.environment_,True)
        cpuCreateAndPlaceShip(enemy,i)

        if cpu_ships_visible:
            print("CPU map:")    
            printMap(enemy.environment_,cpu_ships_visible)

    while True:
        player.attack(enemy)
        print("CPU Map:")
        printMap(enemy.environment_,cpu_ships_visible)
        time.sleep(0.5)
        if enemy.checkEndOfGame():
            print("BATTLE WON! YOU HAVE SUNK ALL ENEMY SHIPS!")
            break
        print("enemy attack?")
        enemy.attack(player)
        
        print("YOUR BATTLEFIELD:")
        printMap(player.environment_,True)
        if player.checkEndOfGame():
            print("BATTLE LOST! ALL YOUR SHIPS HAVE BEEN SUNK BY THE ENEMY!")
            break
    

def cpuCreateAndPlaceShip(enemy,ship_num):
    # enemy.detValidLocations(ship = Ship(ship_size))
    enemy.detValidLocations(ship = Ship(ship_num+3))
    while True:
        try:
            ship_coords = enemy.checkValidLocPlaceShip()
            if not enemy.placeShipCPU():
                break            
        except ValueError:
            print("Ship unable to be placed")
    
                    
def createAndPlaceShip(player,ship_num):
    while True:
            ship = Ship(ship_num+3)
            # ship = Ship(int(input("Size of Ship: ")))
            # detValidLocations(area,ship)
            player.chooseDirAndCoords(ship)
            break
            
            
def printMap(battlegroundArray,show_ships):
    abc = list("ABCDEFGHI")
    nums = list(" 123456789 ")
    printableArray = copy.deepcopy(battlegroundArray)
    printableArray.insert(0,abc)
    for i in range(len(printableArray)):
        printableArray[i].insert(0,nums[i])
        
    if not show_ships:
        for rowIT, row in enumerate(printableArray):
            for eleIT, ele in enumerate(row):
                if ele == '#':
                    printableArray[rowIT][eleIT] = '~'
    
    for row in printableArray:
        print(" ".join(row))
    print()


if __name__ == "__main__":
    main()
        
    