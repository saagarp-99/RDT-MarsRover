
""""Defining classes and global dictionaries"""

#directionToNum and numToDirection used to switch from direction to number and vice versa
directionToNum = {
    'N' : 0,
    'E' : 1,
    'S' : 2,
    'W' : 3,
    }
numToDirection = {
    0 : 'N',
    1 : 'E',
    2 : 'S',
    3 : 'W'
    }

#define Rover class
class Rover:
    def  __init__(self, x, y, d, inst):
        self.x = x
        self.y = y
        self.d = d
        self.inst = inst

#Define execute instruction command for Rover class
    def execute_instructions(self):
        Rover_dir_num  = directionToNum.get(self.d) #convert direction to number 
        
        #for loop to check each character of command for action to take
        for i in range(0, len(self.inst)):
            if (self.inst[i] == 'R'):
                Rover_dir_num += 1
            elif (self.inst[i] == 'L'):
                Rover_dir_num -= 1 
            
            #ensures that Rover_dir_num stays between 0 and 3 inclusive
            if Rover_dir_num == 4:
                Rover_dir_num = 0
            elif Rover_dir_num == -1:
                Rover_dir_num = 3
      
            #moves roverin correct direcion
            #if move would lead rover off plateau rover stops commands
            if (self.inst[i] == 'M'):
                if (Rover_dir_num == 0):
                    if self.y == plat_size[1]:
                        print('Rover stopped to prevent it from leaving plateau!')
                        break
                    else:
                        self.y += 1
                elif (Rover_dir_num == 1):
                    if self.x == plat_size[0]:
                        print('Rover stopped to prevent it from leaving plateau!')
                        break
                    else:
                        self.x += 1
                elif (Rover_dir_num == 2):
                    if self.y == 0:
                        print('Rover stopped to prevent it from leaving plateau!')
                        break
                    else:
                        self.y -= 1
                elif (Rover_dir_num == 3):
                    if self.x == 0:
                        print('Rover stopped to prevent it from leaving plateau!')
                        break
                    else:
                        self.x -= 1
            #reassigns final rover direction based on Rover_dir_num
            self.d = numToDirection.get(Rover_dir_num)

#Define print location function  
    def print_status(self):
        status = ' '.join(str(self.x) + str(self.y) + self.d)
        print(status)
        return None
            
        
"""Read in user inputs"""

#initialising booleans for checks and strings and arrays of valid inputs
plat_size_valid = False
valid_directions = 'NESW'
valid_instructions = ['L', 'R', 'M']
R1_pos_valid = False
R1_inst_valid = False
R2_pos_valid = False
R2_inst_valid = False

#while loops that ensure inputs are valid
while plat_size_valid == False:
    try:
        plat_size = list(map(int,input("Enter plateau size: ").strip().split()))[:2]
        plat_size_valid = True
    except ValueError:
        print('Please input 2 integer values!')
    except IndexError:
        print('Please input only 2 integer values!')

while R1_pos_valid == False:
    try:
        Rover1_pos = list(map(str,input("Enter Rover 1 position and orientation: ").strip().split()))[:3]        
        Rover1_pos[0] = int(Rover1_pos[0])
        Rover1_pos[1] = int(Rover1_pos[1])
        if Rover1_pos[2] not in valid_directions:
            raise ValueError
        for i in range(0, len(plat_size)):
            if (Rover1_pos[i]>plat_size[i]):
                raise ValueError
        R1_pos_valid = True
    except ValueError:
        print('Please input 2 integer values inside plateau size and a valid direction!')
    except IndexError:
        print('Please input only 2 integer values inside plateau size and a valid direction!')


while R1_inst_valid == False:
    try:    
        Rover1_instrct = input("Enter Instructions for Rover 1: ")
        for i in range(0, len(Rover1_instrct)):
            if Rover1_instrct[i] not in valid_instructions:
                raise ValueError
        R1_inst_valid = True
    except ValueError:
        print('Please input valid instruction commands!')
        
Rover1 = Rover(Rover1_pos[0], Rover1_pos[1], Rover1_pos[2], Rover1_instrct)

while R2_pos_valid == False:
    try:
        Rover2_pos = list(map(str,input("Enter Rover 2 position and orientation: ").strip().split()))[:3]
        Rover2_pos[0] = int(Rover2_pos[0])
        Rover2_pos[1] = int(Rover2_pos[1])
        for i in range(0, len(plat_size)):
            if (Rover2_pos[i]>plat_size[i]):
                raise ValueError
        R2_pos_valid = True
    except ValueError:
        print('Please input 2 integer values inside plateau size and a valid direction!')
    except IndexError:
        print('Please input only 2 integer values inside plateau size and a valid direction!')

while R2_inst_valid == False:
    try:
        Rover2_instrct = input("Enter Instructions for Rover 2: ")
        for i in range(0, len(Rover2_instrct)):
            if Rover2_instrct[i] not in valid_instructions:
                raise ValueError
        R2_inst_valid = True
    except ValueError:
        print('Please input valid instruction commands!')

Rover2 = Rover(Rover2_pos[0], Rover2_pos[1], Rover2_pos[2], Rover2_instrct)

#execute rover1 command and print final location
Rover1.execute_instructions()
Rover1.print_status()

#execute rover2 command and print final location
Rover2.execute_instructions()
Rover2.print_status()
