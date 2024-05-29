from ship import Ship
import copy
import time

class BattleGround:
    def __init__(self,col=9,row=9):
        self.environment_ = [["~"]*col for _ in range(row)]
        self.last_confirmed_hit = [0,0]
        self.ship_list_ = []
        self.abc_vals = 'ABCDEFGHI'
        self.num_vals = '123456789'
            
    def convertInputToCoords(self,input_str):
        coords = list([0,0])
        abc = "ABCDEFGHI"
        nums = "123456789"
        for x in range(len(abc)):
            if input_str[0] == abc[x]:
                coords[1] = x
                break
        for y in range(len(nums)):
            if input_str[1] == nums[y]:
                coords[0] = y
                break    
        return coords
    
    def attack(self,opposition):
        while True:
            atk_loc_input = input("Where would you like to fire your torpedo: ").upper()
            if self.checkCoordsAreValid(atk_loc_input):
                break
            else:
                print("Invalid Coordinates for Torpedo.\nTry again.\n")
            
        atk_coords = self.convertInputToCoords(atk_loc_input)
        print("TORPEDO LAUNCHED!")
        time.sleep(1)
        if opposition.environment_[atk_coords[0]][atk_coords[1]] == '#':
            opposition.environment_[atk_coords[0]][atk_coords[1]] = 'X'
            self.last_confirmed_hit = atk_coords
            print("\nCONFIRMED HIT\n")
        else:
            opposition.environment_[atk_coords[0]][atk_coords[1]] = '/'
            print("\nMISS\n")
        time.sleep(1)    
        opposition.checkForSunkenShip()        
        
    def chooseDirAndCoords(self,ship):
        # loop_break = True
        # temp_environment_ = copy.deepcopy(self.environment_)
        while True:
            try:
                temp_environment_ = copy.deepcopy(self.environment_)
                ship_detected = False
                while True:
                    head_location = input("Where would you like to place the bow (front) of the Ship?: ").upper()
                    print()
                    if self.checkCoordsAreValid(head_location):
                        break
                    else:
                        print("Invalid Coordinates for Battleship.\nTry again.\n")
                head_coords = self.convertInputToCoords(head_location)
                ver_or_hor = input("Choose the Orientation of the ship:\n1 = Horizontal\n2 = Vertical\nOrientation: ")
                print()

                if ver_or_hor == '1':
                    for i in range(len(ship.ship_)):
                        if not temp_environment_[head_coords[0]][head_coords[1]+i] == ship.ship_[0]:
                            temp_environment_[head_coords[0]][head_coords[1]+i] = ship.ship_[0]                        
                        elif temp_environment_[head_coords[0]][head_coords[1]+i] == ship.ship_[0]:
                            print("Ship cannot manoeuvre there! There is another ship in the way!\nChoose another location for the bow or orientation of the ship.\n")
                            ship_detected = True
                            break
                        
                elif ver_or_hor == '2':
                    for i in range(len(ship.ship_)):
                        if not temp_environment_[head_coords[0]+i][head_coords[1]] == ship.ship_[0]:
                            temp_environment_[head_coords[0]+i][head_coords[1]] = ship.ship_[0]
                        elif temp_environment_[head_coords[0]+i][head_coords[1]] == ship.ship_[0]:
                            print("Ship cannot manoeuvre there! There is another ship in the way!\nChoose another location for the bow or orientation of the ship.\n")
                            ship_detected = True
                            break
                        
                else:
                    print("Invalid Direction Chosen")
                    ship_detected = True
                
                if ship_detected == False:
                    self.environment_ = copy.deepcopy(temp_environment_)
                    self.ship_list_.append([len(ship.ship_),head_coords,ver_or_hor])
                    print("BATTLESHIP HAS MOVED TO POSITION\n")
                    break
                
            except ValueError:
                print("Restarting..")
            
    def checkForSunkenShip(self):
        sunken_ship = False
        for ship_IT, element in enumerate(self.ship_list_):
            ship_val = 0
            ship_head_coords = element[1]
            for i in range(element[0]):
                if element[2] == '1' or element[2] == 1:
                    if self.environment_[ship_head_coords[0]][ship_head_coords[1]+i] == 'X':
                        ship_val += 1
                elif element[2] == '2' or element[2] == 2:
                    if self.environment_[ship_head_coords[0]+i][ship_head_coords[1]] == 'X':
                        ship_val += 1
            
            if ship_val == element[0]:
                print("A BATTLESHIP HAS BEEN SUNK!\n")
                time.sleep(0.5)
                del self.ship_list_[ship_IT]
                sunken_ship = True 
       
        return sunken_ship
    
    def checkCoordsAreValid(self,attack_coords):
        if len(attack_coords)!= 2:
            return False
        for i, ele in enumerate(self.abc_vals):
            if attack_coords[0] == self.abc_vals[i]:
                for j, ele in enumerate(self.num_vals):
                    if attack_coords[1] == self.num_vals[j]:
                        return True    
        return False    
    
            
    def checkEndOfGame(self):
        if not self.ship_list_:
            return True
                
    #FUNCTION NOT USED FOR TESTING ONLY           
    def placeShip(self):
        for j in range(2):
                for i in range(5):
                        self.environment_[2+(j*2)][2+i] = '#'
                self.ship_list_.append([5,[2+(j*2),2],'1'])                