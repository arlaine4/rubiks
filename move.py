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
    c.cube[0][0][0] = 5
    print_cube(c)
    # F rotate clockwise
    if clockwise:
        c.cube[0] = np.rot90(c.cube[0], k=1, axes=(1, 0))
        tmp = deepcopy(c.cube[5][0])
        # R to D
        c.cube[5][0][0] = c.cube[1][0][0]
        c.cube[5][0][1] = c.cube[1][1][0]
        c.cube[5][0][2] = c.cube[1][2][0]
        # U to R
        c.cube[1][0][0] = c.cube[2][2][0]
        c.cube[1][1][0] = c.cube[2][2][1]
        c.cube[1][2][0] = c.cube[2][2][2]
        # L to U
        c.cube[2][2][0] = c.cube[4][0][2]
        c.cube[2][2][1] = c.cube[4][1][2]
        c.cube[2][2][2] = c.cube[4][2][2]
        # D to L
        c.cube[4][0][2] = tmp[0]
        c.cube[4][1][2] = tmp[1]
        c.cube[4][2][2] = tmp[2]
    else:
        c.cube[0] = np.rot90(c.cube[0], k=1, axes=(0, 1))
        tmp = deepcopy(c.cube[1])
        # D to R
        c.cube[1][0][0] = c.cube[5][0][0] 
        c.cube[1][1][0] = c.cube[5][0][1] 
        c.cube[1][2][0] = c.cube[5][0][2] 
        # L to D
        c.cube[5][0][0] = c.cube[4][0][2]
        c.cube[5][0][1] = c.cube[4][1][2]
        c.cube[5][0][2] = c.cube[4][2][2]
        # U to L
        c.cube[4][0][2] = c.cube[2][2][0] 
        c.cube[4][1][2] = c.cube[2][2][1] 
        c.cube[4][2][2] = c.cube[2][2][2] 
        # R to U
        c.cube[2][2][0] = tmp[0][0]
        c.cube[2][2][1] = tmp[1][0]
        c.cube[2][2][2] = tmp[2][0]

    print("AFTER MOVE_F")
    print_cube(c)
