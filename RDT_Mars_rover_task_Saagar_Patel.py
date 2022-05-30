"""Read in user inputs"""
plat_size_valid = False
valid_directions = 'NESW'
valid_instructions = ['L', 'R', 'M']
R1_pos_valid = False
R1_inst_valid = False
R2_pos_valid = False
R2_inst_valid = False

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

""""Perform Rover instructions"""

#dictionaries to convert facing direction to a number and vice versa
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
    3 : 'W'}

#Rover 1 travel
Rover1_dir_num  = directionToNum.get(Rover1_pos[2])
Rover1_newPos = Rover1_pos
for i in range(0, len(Rover1_instrct)):
    if (Rover1_instrct[i] == 'R'):
        Rover1_dir_num += 1
    elif (Rover1_instrct[i] == 'L'):
        Rover1_dir_num -= 1
        
    if Rover1_dir_num == 4:
        Rover1_dir_num = 0
    elif Rover1_dir_num == -1:
        Rover1_dir_num = 3
    
    if (Rover1_instrct[i] == 'M'):
        if (Rover1_dir_num == 0):
            if Rover1_newPos[1] == plat_size[1]:
                print('Rover1 stopped to prevent it from leaving plateau!')
                break
            else:
                Rover1_newPos[1] += 1
        elif (Rover1_dir_num == 1):
            if Rover1_newPos[0] == plat_size[0]:
                print('Rover1 stopped to prevent it from leaving plateau!')
                break
            else:
                Rover1_newPos[0] += 1
        elif (Rover1_dir_num == 2):
            if Rover1_newPos[1] == 0:
                print('Rover1 stopped to prevent it from leaving plateau!')
                break
            else:
                Rover1_newPos[1] -= 1
        elif (Rover1_dir_num == 3):
            if Rover1_newPos[0] == 0:
                print('Rover1 stopped to prevent it from leaving plateau!')
                break
            else:
                Rover1_newPos[0] -= 1

Rover1_newPos[2] = numToDirection.get(Rover1_dir_num)
print(' '.join(str(x) for x in Rover1_newPos))
 
#Rover 2 travel
Rover2_newPos = Rover2_pos   
Rover2_dir_num  = directionToNum.get(Rover2_pos[2])
for i in range(0, len(Rover2_instrct)):
    if (Rover2_instrct[i] == 'R'):
        Rover2_dir_num += 1
    elif (Rover2_instrct[i] == 'L'):
        Rover2_dir_num -= 1
        
    if Rover2_dir_num == 4:
        Rover2_dir_num = 0
    elif Rover2_dir_num == -1:
        Rover2_dir_num = 3
    
    if (Rover2_instrct[i] == 'M'):
        if (Rover2_dir_num == 0):
            if Rover2_newPos[1] == plat_size[1]:
                print('Rover2 stopped to prevent it from leaving plateau!')
                break
            else:
                Rover2_newPos[1] += 1
        elif (Rover2_dir_num == 1):
            if Rover2_newPos[0] == plat_size[1]:
                print('Rover2 stopped to prevent it from leaving plateau!')
                break
            else:
                Rover2_newPos[0] += 1
        elif (Rover2_dir_num == 2):
            if Rover2_newPos[1] == 0:
                print('Rover2 stopped to prevent it from leaving plateau!')
                break
            else:
                Rover2_newPos[1] -= 1
        elif (Rover2_dir_num == 3):
            if Rover2_newPos[0] == 0:
                print('Rover2 stopped to prevent it from leaving plateau!')
                break
            else:
                Rover2_newPos[0] -= 1

Rover2_newPos[2] = numToDirection.get(Rover2_dir_num)
print(' '.join(str(x) for x in Rover2_newPos))
