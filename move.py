import numpy as np
from copy import deepcopy

# np.rot90(cube.cube[0], k=1, axes=(1, 0)) pour une rotation clockwise
# np.rot90(cube.cube[0], k=1, axes=(0, 1)) pour une rotation counter-clockwise
# if the order is F R U B L D
#                 0 1 2 3 4 5

def print_cube(c): 
    list_move = ['F', 'R', 'U', 'B', 'L', 'D']
    for i in range(len(c.cube)):
        print(list_move[i], ":")
        print(c.cube[i])

def move_F(c, clockwise):
    c.cube[0][0][0] = 9
    print_cube(c)
    # F rotate clockwise
    if clockwise:
        c.cube[0] = np.rot90(c.cube[0], k=1, axes=(1, 0))
        tmp = deepcopy(c.cube[5][0])
        # R to D
        c.cube[5][0][2] = c.cube[1][0][0]
        c.cube[5][0][1] = c.cube[1][1][0]
        c.cube[5][0][0] = c.cube[1][2][0]
        # U to R
        c.cube[1][0][0] = c.cube[2][2][0]
        c.cube[1][1][0] = c.cube[2][2][1]
        c.cube[1][2][0] = c.cube[2][2][2]
        # L to U
        c.cube[2][2][2] = c.cube[4][0][2]
        c.cube[2][2][1] = c.cube[4][1][2]
        c.cube[2][2][0] = c.cube[4][2][2]
        # D to L
        c.cube[4][0][2] = tmp[0]
        c.cube[4][1][2] = tmp[1]
        c.cube[4][2][2] = tmp[2]
    # F rotate counter-clockwise
    else:
        c.cube[0] = np.rot90(c.cube[0], k=1, axes=(0, 1))
        tmp = deepcopy(c.cube[1])
        # D to R
        c.cube[1][2][0] = c.cube[5][0][0] 
        c.cube[1][1][0] = c.cube[5][0][1] 
        c.cube[1][0][0] = c.cube[5][0][2] 
        # L to D
        c.cube[5][0][0] = c.cube[4][0][2]
        c.cube[5][0][1] = c.cube[4][1][2]
        c.cube[5][0][2] = c.cube[4][2][2]
        # U to L
        c.cube[4][2][2] = c.cube[2][2][0] 
        c.cube[4][1][2] = c.cube[2][2][1] 
        c.cube[4][0][2] = c.cube[2][2][2] 
        # R to U
        c.cube[2][2][0] = tmp[0][0]
        c.cube[2][2][1] = tmp[1][0]
        c.cube[2][2][2] = tmp[2][0]

    print("AFTER MOVE_F")
    print_cube(c)
    return(c)

def move_R(c, clockwise):
    c.cube[1][0][0] = 9
    print_cube(c)
    # R rotate clockwise
    if clockwise:
        c.cube[1] = np.rot90(c.cube[1], k=1, axes=(1, 0))
        tmp = deepcopy(c.cube[5][2])
        # B to D
        c.cube[5][2][2] = c.cube[3][0][0]
        c.cube[5][1][2] = c.cube[3][1][0]
        c.cube[5][0][2] = c.cube[3][2][0]
        # U to B
        c.cube[3][0][0] = c.cube[2][2][2]
        c.cube[3][1][0] = c.cube[2][1][2]
        c.cube[3][2][0] = c.cube[2][0][2]
        # F to U
        c.cube[2][2][2] = c.cube[0][2][2]
        c.cube[2][1][2] = c.cube[0][2][1]
        c.cube[2][0][2] = c.cube[0][2][0]
        # D to F
        c.cube[0][0][2] = tmp[0]
        c.cube[0][1][2] = tmp[1]
        c.cube[0][2][2] = tmp[2]
    # R rotate counter-clockwise
    else:
        c.cube[1] = np.rot90(c.cube[1], k=1, axes=(0, 1))
        tmp = deepcopy(c.cube[5][2])
        # F to D
        c.cube[5][2][2] = c.cube[0][2][2] 
        c.cube[5][1][2] = c.cube[0][2][1] 
        c.cube[5][0][2] = c.cube[0][2][0] 
        # U to F
        c.cube[0][2][2] = c.cube[2][2][2]
        c.cube[0][1][2] = c.cube[2][1][2]
        c.cube[0][0][2] = c.cube[2][0][2]
        # B to U
        c.cube[2][2][2] = c.cube[3][0][0]  
        c.cube[2][1][2] = c.cube[3][1][0]  
        c.cube[2][0][2] = c.cube[3][2][0]  
        # D to B
        c.cube[3][2][0] = tmp[0]
        c.cube[3][1][0] = tmp[1]
        c.cube[3][0][0] = tmp[2]

    print("AFTER MOVE_R")
    print_cube(c)
    return(c)

def move_B(c, clockwise):
    c.cube[3][0][0] = 9
    print_cube(c)
    # B rotate clockwise
    if clockwise:
        c.cube[3] = np.rot90(c.cube[3], k=1, axes=(1, 0))
        tmp = deepcopy(c.cube[5][0])
        # L to D
        c.cube[5][2][2] = c.cube[4][0][0]
        c.cube[5][2][1] = c.cube[4][1][0]
        c.cube[5][2][0] = c.cube[4][2][0]
        # U to L
        c.cube[4][0][0] = c.cube[2][2][0]
        c.cube[4][1][0] = c.cube[2][2][1]
        c.cube[4][2][0] = c.cube[2][2][2]
        # R to U
        c.cube[2][0][2] = c.cube[1][0][2]
        c.cube[2][0][1] = c.cube[1][1][2]
        c.cube[2][0][0] = c.cube[1][2][2]
        # D to R
        c.cube[1][0][2] = tmp[0]
        c.cube[1][1][2] = tmp[1]
        c.cube[1][2][2] = tmp[2]
    # B rotate counter-clockwise
    else:
        c.cube[3] = np.rot90(c.cube[3], k=1, axes=(0, 1))
        tmp = deepcopy(c.cube[4])
        # D to L
        c.cube[4][2][0] = c.cube[5][0][0] 
        c.cube[4][1][0] = c.cube[5][0][1] 
        c.cube[4][0][0] = c.cube[5][0][2] 
        # R to D
        c.cube[5][2][0] = c.cube[1][0][2]
        c.cube[5][2][1] = c.cube[1][1][2]
        c.cube[5][2][2] = c.cube[1][2][2]
        # U to R
        c.cube[1][2][2] = c.cube[2][2][0] 
        c.cube[1][1][2] = c.cube[2][2][1] 
        c.cube[1][0][2] = c.cube[2][2][2] 
        # L to U
        c.cube[2][0][0] = tmp[0][0]
        c.cube[2][0][1] = tmp[1][0]
        c.cube[2][0][2] = tmp[2][0]

    print("AFTER MOVE_B")
    print_cube(c)
    return(c)

def move_L(c, clockwise):
    c.cube[4][0][0] = 9
    print_cube(c)
    # L rotate clockwise
    if clockwise:
        c.cube[4] = np.rot90(c.cube[4], k=1, axes=(1, 0))
        tmp = deepcopy(c.cube[5])
        # F to D
        c.cube[5][0][0] = c.cube[0][0][0] 
        c.cube[5][1][0] = c.cube[0][1][0] 
        c.cube[5][2][0] = c.cube[0][2][0] 
        # U to F
        c.cube[0][0][0] = c.cube[2][0][0]
        c.cube[0][1][0] = c.cube[2][1][0]
        c.cube[0][2][0] = c.cube[2][2][0]
        # B to U
        c.cube[2][2][0] = c.cube[3][0][2]
        c.cube[2][1][0] = c.cube[3][1][2] 
        c.cube[2][0][0] = c.cube[3][2][2]
        # D to B
        c.cube[3][2][2] = tmp[0][0]
        c.cube[3][1][2] = tmp[1][0]
        c.cube[3][0][2] = tmp[2][0]
    # R rotate counter-clockwise
    else:
        c.cube[4] = np.rot90(c.cube[4], k=1, axes=(0, 1))
        tmp = deepcopy(c.cube[5])
        # B to D
        c.cube[5][0][0] = c.cube[3][2][2]
        c.cube[5][1][0] = c.cube[3][1][2]
        c.cube[5][2][0] = c.cube[3][0][2]
        # U to B
        c.cube[3][2][2] = c.cube[2][0][0]
        c.cube[3][1][2] = c.cube[2][1][0]
        c.cube[3][0][2] = c.cube[2][2][0]
        # F to U
        c.cube[2][0][0] = c.cube[0][0][0]
        c.cube[2][1][0] = c.cube[0][1][0]
        c.cube[2][2][0] = c.cube[0][2][0]
        # D to F
        c.cube[0][0][0] = tmp[0][0]
        c.cube[0][1][0] = tmp[1][0]
        c.cube[0][2][0] = tmp[2][0]
    print("AFTER MOVE_L")
    print_cube(c)
    return(c)

def move_U(c, clockwise):
    c.cube[2][0][0] = 9
    print_cube(c)
    # U rotate clockwise
    if clockwise:
        c.cube[2] = np.rot90(c.cube[2], k=1, axes=(1, 0))
        tmp = deepcopy(c.cube[0])
        # R to F
        c.cube[0][0][0] = c.cube[1][0][0]
        c.cube[0][0][1] = c.cube[1][0][1]
        c.cube[0][0][2] = c.cube[1][0][2]
        # B to R
        c.cube[1][0][0] = c.cube[3][0][0]
        c.cube[1][0][1] = c.cube[3][0][1] 
        c.cube[1][0][2] = c.cube[3][0][2]
        # L to B
        c.cube[3][0][0] = c.cube[4][0][0]
        c.cube[3][0][1] = c.cube[4][0][1]
        c.cube[3][0][2] = c.cube[4][0][2]
        # F to L
        c.cube[4][0][0] = tmp[0][0]
        c.cube[4][0][1] = tmp[0][1]
        c.cube[4][0][2] = tmp[0][2]
    # U rotate counter-clockwise
    else:
        c.cube[2] = np.rot90(c.cube[2], k=1, axes=(0, 1))
        tmp = deepcopy(c.cube[0])
        # L to F
        c.cube[0][0][0] = c.cube[4][0][0]
        c.cube[0][0][1] = c.cube[4][0][1]
        c.cube[0][0][2] = c.cube[4][0][2]
        # B to L
        c.cube[4][0][0] = c.cube[3][0][0]
        c.cube[4][0][1] = c.cube[3][0][1] 
        c.cube[4][0][2] = c.cube[3][0][2]
        # R to B
        c.cube[3][0][0] = c.cube[1][0][0]
        c.cube[3][0][1] = c.cube[1][0][1]
        c.cube[3][0][2] = c.cube[1][0][2]
        # R to L
        c.cube[1][0][0] = tmp[0][0]
        c.cube[1][0][1] = tmp[0][1]
        c.cube[1][0][2] = tmp[0][2]
    print("AFTER MOVE_U")
    print_cube(c)
    return(c)