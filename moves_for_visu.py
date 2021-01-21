import numpy as np
from copy import deepcopy

# np.rot90(cube.cube[0], k=1, axes=(1, 0)) pour une rotation clockwise
# np.rot90(cube.cube[0], k=1, axes=(0, 1)) pour une rotation unter-clockwise
# if the order is F R U B L D
#                 0 1 2 3 4 5


# cube array lors reprensentation :
# Fas :	0		1		2		3		4		5
#		Blue		red             yellow          green           orange           white
#		front	        right           up              ba            left            down

###
### Need to verify ta everthing work perfely but it seems to cube ean
### The only possible error I see atm is an inverted rotation of the targeted fa for the move (in move_U it will cube the U fa) 
###

def move_F(cube, clockwise):
    # F rotate clockwise
    if clockwise:
        cube[0] = np.rot90(cube[0], k=1, axes=(1, 0))
        tmp = deepcopy(cube[5][0])
        # R to D
        cube[5][0][2] = cube[1][0][0]
        cube[5][0][1] = cube[1][1][0]
        cube[5][0][0] = cube[1][2][0]
        # U to R
        cube[1][0][0] = cube[2][2][0]
        cube[1][1][0] = cube[2][2][1]
        cube[1][2][0] = cube[2][2][2]
        # L to U
        cube[2][2][2] = cube[4][0][2]
        cube[2][2][1] = cube[4][1][2]
        cube[2][2][0] = cube[4][2][2]
        # D to L
        cube[4][0][2] = tmp[0]
        cube[4][1][2] = tmp[1]
        cube[4][2][2] = tmp[2]
    # F rotate unter-clockwise
    else:
        cube[0] = np.rot90(cube[0], k=1, axes=(0, 1))
        tmp = deepcopy(cube[1])
        # D to R
        cube[1][2][0] = cube[5][0][0] 
        cube[1][1][0] = cube[5][0][1] 
        cube[1][0][0] = cube[5][0][2] 
        # L to D
        cube[5][0][0] = cube[4][0][2]
        cube[5][0][1] = cube[4][1][2]
        cube[5][0][2] = cube[4][2][2]
        # U to L
        cube[4][2][2] = cube[2][2][0] 
        cube[4][1][2] = cube[2][2][1] 
        cube[4][0][2] = cube[2][2][2] 
        # R to U
        cube[2][2][0] = tmp[0][0]
        cube[2][2][1] = tmp[1][0]
        cube[2][2][2] = tmp[2][0]
    return cube

def move_R(cube, clockwise):
    # R rotate clockwise
    if clockwise:
        cube[1] = np.rot90(cube[1], k=1, axes=(1, 0))
        tmp = deepcopy(cube[5])
        # B to D
        cube[5][2][2] = cube[3][0][0]
        cube[5][1][2] = cube[3][1][0]
        cube[5][0][2] = cube[3][2][0]
        # U to B
        cube[3][0][0] = cube[2][2][2]
        cube[3][1][0] = cube[2][1][2]
        cube[3][2][0] = cube[2][0][2]
        # F to U
        cube[2][0][2] = cube[0][0][2]
        cube[2][1][2] = cube[0][1][2]
        cube[2][2][2] = cube[0][2][2]
        # D to F
        cube[0][0][2] = tmp[0][2]
        cube[0][1][2] = tmp[1][2]
        cube[0][2][2] = tmp[2][2]
    # R rotate unter-clockwise
    else:
        cube[1] = np.rot90(cube[1], k=1, axes=(0, 1))
        tmp = deepcopy(cube[5])
        # F to D
        cube[5][0][2] = cube[0][0][2] 
        cube[5][1][2] = cube[0][1][2] 
        cube[5][2][2] = cube[0][2][2] 
        # U to F
        cube[0][0][2] = cube[2][0][2]
        cube[0][1][2] = cube[2][1][2]
        cube[0][2][2] = cube[2][2][2]
        # B to U
        cube[2][2][2] = cube[3][0][0]  
        cube[2][1][2] = cube[3][1][0]  
        cube[2][0][2] = cube[3][2][0]  
        # D to B
        cube[3][2][0] = tmp[0][2]
        cube[3][1][0] = tmp[1][2]
        cube[3][0][0] = tmp[2][2]
    return cube

def move_B(cube, clockwise):
    # B rotate clockwise
    if clockwise:
        cube[3] = np.rot90(cube[3], k=1, axes=(1, 0))
        tmp = deepcopy(cube[5])
        # L to D
        cube[5][2][0] = cube[4][0][0]
        cube[5][2][1] = cube[4][1][0]
        cube[5][2][2] = cube[4][2][0]
        # U to L
        cube[4][2][0] = cube[2][0][0]
        cube[4][1][0] = cube[2][0][1]
        cube[4][0][0] = cube[2][0][2]
        # R to U
        cube[2][0][0] = cube[1][0][2]
        cube[2][0][1] = cube[1][1][2]
        cube[2][0][2] = cube[1][2][2]
        # D to R
        cube[1][0][2] = tmp[2][2]
        cube[1][1][2] = tmp[2][1]
        cube[1][2][2] = tmp[2][0]
    # B rotate unter-clockwise
    else:
        cube[3] = np.rot90(cube[3], k=1, axes=(0, 1))
        tmp = deepcopy(cube[4])
        # D to L
        cube[4][0][0] = cube[5][2][0] 
        cube[4][1][0] = cube[5][2][1] 
        cube[4][2][0] = cube[5][2][2] 
        # R to D
        cube[5][2][2] = cube[1][0][2]
        cube[5][2][1] = cube[1][1][2]
        cube[5][2][0] = cube[1][2][2]
        # U to R
        cube[1][0][2] = cube[2][0][0] 
        cube[1][1][2] = cube[2][0][1] 
        cube[1][2][2] = cube[2][0][2] 
        # L to U
        cube[2][0][2] = tmp[0][0]
        cube[2][0][1] = tmp[1][0]
        cube[2][0][0] = tmp[2][0]
    return cube

def move_L(cube, clockwise):
    # L rotate clockwise
    if clockwise:
        cube[4] = np.rot90(cube[4], k=1, axes=(1, 0))
        tmp = deepcopy(cube[5])
        # F to D
        cube[5][0][0] = cube[0][0][0] 
        cube[5][1][0] = cube[0][1][0] 
        cube[5][2][0] = cube[0][2][0] 
        # U to F
        cube[0][0][0] = cube[2][0][0]
        cube[0][1][0] = cube[2][1][0]
        cube[0][2][0] = cube[2][2][0]
        # B to U
        cube[2][2][0] = cube[3][0][2]
        cube[2][1][0] = cube[3][1][2] 
        cube[2][0][0] = cube[3][2][2]
        # D to B
        cube[3][2][2] = tmp[0][0]
        cube[3][1][2] = tmp[1][0]
        cube[3][0][2] = tmp[2][0]
    # L rotate unter-clockwise
    else:
        cube[4] = np.rot90(cube[4], k=1, axes=(0, 1))
        tmp = deepcopy(cube[5])
        # B to D
        cube[5][0][0] = cube[3][2][2]
        cube[5][1][0] = cube[3][1][2]
        cube[5][2][0] = cube[3][0][2]
        # U to B
        cube[3][2][2] = cube[2][0][0]
        cube[3][1][2] = cube[2][1][0]
        cube[3][0][2] = cube[2][2][0]
        # F to U
        cube[2][0][0] = cube[0][0][0]
        cube[2][1][0] = cube[0][1][0]
        cube[2][2][0] = cube[0][2][0]
        # D to F
        cube[0][0][0] = tmp[0][0]
        cube[0][1][0] = tmp[1][0]
        cube[0][2][0] = tmp[2][0]
    return cube

def move_U(cube, clockwise):
    # U rotate clockwise
    if clockwise:
        cube[2] = np.rot90(cube[2], k=1, axes=(1, 0))
        tmp = deepcopy(cube[0])
        # R to F
        cube[0][0][0] = cube[1][0][0]
        cube[0][0][1] = cube[1][0][1]
        cube[0][0][2] = cube[1][0][2]
        # B to R
        cube[1][0][0] = cube[3][0][0]
        cube[1][0][1] = cube[3][0][1] 
        cube[1][0][2] = cube[3][0][2]
        # L to B
        cube[3][0][0] = cube[4][0][0]
        cube[3][0][1] = cube[4][0][1]
        cube[3][0][2] = cube[4][0][2]
        # F to L
        cube[4][0][0] = tmp[0][0]
        cube[4][0][1] = tmp[0][1]
        cube[4][0][2] = tmp[0][2]
    # U rotate unter-clockwise
    else:
        cube[2] = np.rot90(cube[2], k=1, axes=(0, 1))
        tmp = deepcopy(cube[0])
        # L to F
        cube[0][0][0] = cube[4][0][0]
        cube[0][0][1] = cube[4][0][1]
        cube[0][0][2] = cube[4][0][2]
        # B to L
        cube[4][0][0] = cube[3][0][0]
        cube[4][0][1] = cube[3][0][1] 
        cube[4][0][2] = cube[3][0][2]
        # R to B
        cube[3][0][0] = cube[1][0][0]
        cube[3][0][1] = cube[1][0][1]
        cube[3][0][2] = cube[1][0][2]
        # R to L
        cube[1][0][0] = tmp[0][0]
        cube[1][0][1] = tmp[0][1]
        cube[1][0][2] = tmp[0][2]
    return cube

def move_D(cube, clockwise):
    # D rotate clockwise
    if clockwise:
        cube[5] = np.rot90(cube[5], k=1, axes=(1, 0))
        tmp = deepcopy(cube[0])
        # L to F
        cube[0][2][0] = cube[4][2][0]
        cube[0][2][1] = cube[4][2][1]
        cube[0][2][2] = cube[4][2][2]
        # B to L
        cube[4][2][0] = cube[3][2][0]
        cube[4][2][1] = cube[3][2][1] 
        cube[4][2][2] = cube[3][2][2]
        # R to B
        cube[3][2][0] = cube[1][2][0]
        cube[3][2][1] = cube[1][2][1]
        cube[3][2][2] = cube[1][2][2]
        # R to L
        cube[1][2][0] = tmp[2][0]
        cube[1][2][1] = tmp[2][1]
        cube[1][2][2] = tmp[2][2]
    # D rotate unter-clockwise
    else:
        cube[5] = np.rot90(cube[5], k=1, axes=(0, 1))
        tmp = deepcopy(cube[0])
        # R to F
        cube[0][2][0] = cube[1][2][0]
        cube[0][2][1] = cube[1][2][1]
        cube[0][2][2] = cube[1][2][2]
        # B to R
        cube[1][2][0] = cube[3][2][0]
        cube[1][2][1] = cube[3][2][1] 
        cube[1][2][2] = cube[3][2][2]
        # L to B
        cube[3][2][0] = cube[4][2][0]
        cube[3][2][1] = cube[4][2][1]
        cube[3][2][2] = cube[4][2][2]
        # F to L
        cube[4][2][0] = tmp[2][0]
        cube[4][2][1] = tmp[2][1]
        cube[4][2][2] = tmp[2][2]
    return cube
