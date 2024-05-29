from battleground import BattleGround
import random
import copy
# from ship import Ship
import time

class CPU_Placement(BattleGround):
    def __init__(self,col = 9, row = 9):
        super().__init__(col,row)
        self.player_battleground_ = copy.deepcopy(self.environment_)
        self.hit_last_turn_ = False
        self.ship_sunk_last_turn_ = False
        self.last_hit_coords = list([0,0])
        self.surrounding_options_= []
        
    def detValidLocations(self, ship):
        self.ship_copy_ = ship.ship_
        self.hor_or_vert_ = random.randint(1,2)
        self.tempbattleground = copy.deepcopy(self.environment_)
        # self.tempbattleground = copy.deepcopy(self.battlegroundCPY)
        if self.hor_or_vert_ == 1:
            for rowIT, row in enumerate(self.tempbattleground):
                for elementIT, element in enumerate(row):
                    # if elementIT + len(ship.ship_) > len(row) and elementIT != 0 or element == "#":
                    if elementIT + len(ship.ship_) > len(row) or element == "#":
                        self.tempbattleground[rowIT][elementIT] = "X"
            
        elif self.hor_or_vert_ == 2:
            for rowIT, row in enumerate(self.tempbattleground):
                for elementIT, element in enumerate(row):
                    # if rowIT + len(ship.ship_) > len(self.tempbattleground) and rowIT != 0 or element == "#":
                    if rowIT + len(ship.ship_) > len(self.tempbattleground) or element == "#":    
                        self.tempbattleground[rowIT][elementIT] = "X"
                
    def checkValidLocPlaceShip(self):
        self.valid_coords_ = list([0,0])
        while True:
            try:
                head_coords = [random.randint(0,len(self.tempbattleground)-1),random.randint(0,len(self.tempbattleground[0])-1)]
                if self.tempbattleground[head_coords[0]][head_coords[1]] != "X" or self.tempbattleground[head_coords[0]][head_coords[1]] !="#":
                    self.valid_coords = head_coords
                    break         
            except ValueError:
                print("No location found")
        return self.valid_coords        
                    
    def placeShipCPU(self):
        # temp = copy.deepcopy(self.battlegroundCPY)
        temp = copy.deepcopy(self.environment_)
        
        invalid_loc = False
        if self.hor_or_vert_== 1:
            for i in range(len(self.ship_copy_)):
                if not self.tempbattleground[self.valid_coords[0]][self.valid_coords[1]+i] == "X":
                    temp[self.valid_coords[0]][self.valid_coords[1]+i] = self.ship_copy_[0]                        
                elif self.tempbattleground[self.valid_coords[0]][self.valid_coords[1]+i] == "X":
                    invalid_loc = True
                    break
                        
        elif self.hor_or_vert_ == 2:
            for i in range(len(self.ship_copy_)):
                if not self.tempbattleground[self.valid_coords[0]+i][self.valid_coords[1]] == "X":
                    temp[self.valid_coords[0]+i][self.valid_coords[1]] = self.ship_copy_[0]
                elif self.tempbattleground[self.valid_coords[0]+i][self.valid_coords[1]] == "X":
                    invalid_loc = True
                    break
                
        if invalid_loc == False:  
            # self.printMap(temp)  
            self.ship_list_.append([len(self.ship_copy_),self.valid_coords,self.hor_or_vert_])
            self.environment_ = copy.deepcopy(temp)
            # self.battlegroundCPY = copy.deepcopy(temp)
                
        return invalid_loc

    def attack(self, opposition):
        # print("restarting attack")            
        # print("boolean check to hit last turn ",self.hit_last_turn_) 
          
        if self.hit_last_turn_ == False:
            while True:
                self.attacked_ = [random.randint(0,8),random.randint(0,8)]
                # print("random shooting: ",self.attacked_)
                if self.player_battleground_[self.attacked_[0]][self.attacked_[1]] != ('X' or '/'):
                    if opposition.environment_[self.attacked_[0]][self.attacked_[1]] == '#':
                        self.player_battleground_[self.attacked_[0]][self.attacked_[1]] = 'X'
                        opposition.environment_[self.attacked_[0]][self.attacked_[1]] = 'X'
                        time.sleep(0.5)
                        print("THE ENEMY HAS FIRED A TORPEDO AT ",self.attacked_)
                        time.sleep(1)
                        print("CONFIRMED HIT\n")
                        time.sleep(0.5)
                        self.last_hit_coords = copy.copy(self.attacked_)
                        self.first_place_hit = copy.copy(self.attacked_)
                        self.hit_last_turn_ = True
                        break
                    elif opposition.environment_[self.attacked_[0]][self.attacked_[1]] == '~':
                        self.player_battleground_[self.attacked_[0]][self.attacked_[1]] = '/'
                        time.sleep(0.5)
                        print("THE ENEMY HAS FIRED A TORPEDO AT ",self.attacked_)
                        time.sleep(1)
                        print("MISS!\n")
                        time.sleep(0.5)
                        break
                    else:
                        print("choosing another location")
        
        # elif self.hit_last_turn_ == True and not opposition.checkForSunkenShip():
        elif self.hit_last_turn_ == True:  
            print("trueeeee")  
            placed = False
            while not placed:
                self.checkAroundHit()
                for element in self.surrounding_options_:
                    if self.player_battleground_[element[0]][element[1]] != 'X' and self.player_battleground_[element[0]][element[1]] != '/' and opposition.environment_[element[0]][element[1]] == '#':
                        self.player_battleground_[element[0]][element[1]] = 'X'
                        opposition.environment_[element[0]][element[1]] = 'X'
                        time.sleep(0.5)
                        print("THE ENEMY HAS FIRED A TORPEDO AT ",self.attacked_)
                        time.sleep(1)
                        print("CONFIRMED HIT\n")
                        time.sleep(0.5)
                        self.last_hit_coords = copy.copy(element)
                        placed = True
                        break
                    elif self.player_battleground_[element[0]][element[1]] != 'X' and self.player_battleground_[element[0]][element[1]] != '/' and opposition.environment_[element[0]][element[1]] == '~':
                        self.player_battleground_[element[0]][element[1]] = '/'
                        print("THE ENEMY HAS FIRED A TORPEDO AT ",self.attacked_)
                        time.sleep(1)
                        print("MISS!\n")
                        time.sleep(0.5)
                        placed = True
                        # self.hit_last_turn_ = False
                        break
                    elif element == self.surrounding_options_[-1]:
                        print("in the else statement")
                        self.last_hit_coords = copy.copy(self.first_place_hit) #fix this`
                        placed = True
                        time.sleep(0.5)
                        
        if opposition.checkForSunkenShip():
            # print("inside sunken ship check")
            self.hit_last_turn_ = False
            # self.first_place_hit.clear()        
                
    
    def checkAroundHit(self):
        self.surrounding_options_.clear()
        # print("last hit coords ",self.last_hit_coords)
        if self.player_battleground_[self.last_hit_coords[0]-1][self.last_hit_coords[1]] == 'X': 
            self.surrounding_options_.insert(0,[self.last_hit_coords[0]+1,self.last_hit_coords[1]])
        else:          
            self.surrounding_options_.append([self.last_hit_coords[0]-1,self.last_hit_coords[1]])
            
        if self.player_battleground_[self.last_hit_coords[0]][self.last_hit_coords[1]-1] == 'X':
            self.surrounding_options_.insert(0,[self.last_hit_coords[0],self.last_hit_coords[1]+1])
        else:                      
            self.surrounding_options_.append([self.last_hit_coords[0],self.last_hit_coords[1]-1])
        
        if self.player_battleground_[self.last_hit_coords[0]+1][self.last_hit_coords[1]] == 'X':
            self.surrounding_options_.insert(0,[self.last_hit_coords[0]-1,self.last_hit_coords[1]])
        else:                     
            self.surrounding_options_.append([self.last_hit_coords[0]+1,self.last_hit_coords[1]])
            
        if self.player_battleground_[self.last_hit_coords[0]][self.last_hit_coords[1]+1] == 'X':   
            self.surrounding_options_.insert(0,[self.last_hit_coords[0],self.last_hit_coords[1]-1])
        else:                   
            self.surrounding_options_.append([self.last_hit_coords[0],self.last_hit_coords[1]+1])