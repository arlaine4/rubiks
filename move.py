import numpy as np
from copy import deepcopy

# np.rot90(cube.cube[0], k=1, axes=(1, 0)) pour une rotation clockwise
# np.rot90(cube.cube[0], k=1, axes=(0, 1)) pour une rotation counter-clockwise
# if the order is F R U B L D
#                 0 1 2 3 4 5


# cube array colors reprensentation :
# Faces :	0		1		2		3		4		5
#		Blue		red             yellow          green           orange           white
#		front	        right           up              back            left            down

###
### Need to verify ta everthing work perfectly but it seems to be clean
### The only possible error I see atm is an inverted rotation of the targeted face for the move (in move_U it will be the U face) 
###

def move_F(c, clockwise):
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
    return(c)

def move_R(c, clockwise):
    # R rotate clockwise
    if clockwise:
        c.cube[1] = np.rot90(c.cube[1], k=1, axes=(1, 0))
        tmp = deepcopy(c.cube[5])
        # B to D
        c.cube[5][2][2] = c.cube[3][0][0]
        c.cube[5][1][2] = c.cube[3][1][0]
        c.cube[5][0][2] = c.cube[3][2][0]
        # U to B
        c.cube[3][0][0] = c.cube[2][2][2]
        c.cube[3][1][0] = c.cube[2][1][2]
        c.cube[3][2][0] = c.cube[2][0][2]
        # F to U
        c.cube[2][0][2] = c.cube[0][0][2]
        c.cube[2][1][2] = c.cube[0][1][2]
        c.cube[2][2][2] = c.cube[0][2][2]
        # D to F
        c.cube[0][0][2] = tmp[0][2]
        c.cube[0][1][2] = tmp[1][2]
        c.cube[0][2][2] = tmp[2][2]
    # R rotate counter-clockwise
    else:
        c.cube[1] = np.rot90(c.cube[1], k=1, axes=(0, 1))
        tmp = deepcopy(c.cube[5])
        # F to D
        c.cube[5][0][2] = c.cube[0][0][2] 
        c.cube[5][1][2] = c.cube[0][1][2] 
        c.cube[5][2][2] = c.cube[0][2][2] 
        # U to F
        c.cube[0][0][2] = c.cube[2][0][2]
        c.cube[0][1][2] = c.cube[2][1][2]
        c.cube[0][2][2] = c.cube[2][2][2]
        # B to U
        c.cube[2][2][2] = c.cube[3][0][0]  
        c.cube[2][1][2] = c.cube[3][1][0]  
        c.cube[2][0][2] = c.cube[3][2][0]  
        # D to B
        c.cube[3][2][0] = tmp[0][2]
        c.cube[3][1][0] = tmp[1][2]
        c.cube[3][0][0] = tmp[2][2]
    return(c)

def move_B(c, clockwise):
    # B rotate clockwise
    if clockwise:
        c.cube[3] = np.rot90(c.cube[3], k=1, axes=(1, 0))
        tmp = deepcopy(c.cube[5])
        # L to D
        c.cube[5][2][0] = c.cube[4][0][0]
        c.cube[5][2][1] = c.cube[4][1][0]
        c.cube[5][2][2] = c.cube[4][2][0]
        # U to L
        c.cube[4][2][0] = c.cube[2][0][0]
        c.cube[4][1][0] = c.cube[2][0][1]
        c.cube[4][0][0] = c.cube[2][0][2]
        # R to U
        c.cube[2][0][0] = c.cube[1][0][2]
        c.cube[2][0][1] = c.cube[1][1][2]
        c.cube[2][0][2] = c.cube[1][2][2]
        # D to R
        c.cube[1][0][2] = tmp[2][2]
        c.cube[1][1][2] = tmp[2][1]
        c.cube[1][2][2] = tmp[2][0]
    # B rotate counter-clockwise
    else:
        c.cube[3] = np.rot90(c.cube[3], k=1, axes=(0, 1))
        tmp = deepcopy(c.cube[4])
        # D to L
        c.cube[4][0][0] = c.cube[5][2][0] 
        c.cube[4][1][0] = c.cube[5][2][1] 
        c.cube[4][2][0] = c.cube[5][2][2] 
        # R to D
        c.cube[5][2][2] = c.cube[1][0][2]
        c.cube[5][2][1] = c.cube[1][1][2]
        c.cube[5][2][0] = c.cube[1][2][2]
        # U to R
        c.cube[1][0][2] = c.cube[2][0][0] 
        c.cube[1][1][2] = c.cube[2][0][1] 
        c.cube[1][2][2] = c.cube[2][0][2] 
        # L to U
        c.cube[2][0][2] = tmp[0][0]
        c.cube[2][0][1] = tmp[1][0]
        c.cube[2][0][0] = tmp[2][0]
    return(c)

def move_L(c, clockwise):
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
    # L rotate counter-clockwise
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
    return(c)

def move_U(c, clockwise):
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
    return(c)

def move_D(c, clockwise):
    # D rotate clockwise
    if clockwise:
        c.cube[5] = np.rot90(c.cube[5], k=1, axes=(1, 0))
        tmp = deepcopy(c.cube[0])
        # L to F
        c.cube[0][2][0] = c.cube[4][2][0]
        c.cube[0][2][1] = c.cube[4][2][1]
        c.cube[0][2][2] = c.cube[4][2][2]
        # B to L
        c.cube[4][2][0] = c.cube[3][2][0]
        c.cube[4][2][1] = c.cube[3][2][1] 
        c.cube[4][2][2] = c.cube[3][2][2]
        # R to B
        c.cube[3][2][0] = c.cube[1][2][0]
        c.cube[3][2][1] = c.cube[1][2][1]
        c.cube[3][2][2] = c.cube[1][2][2]
        # R to L
        c.cube[1][2][0] = tmp[2][0]
        c.cube[1][2][1] = tmp[2][1]
        c.cube[1][2][2] = tmp[2][2]
    # D rotate counter-clockwise
    else:
        c.cube[5] = np.rot90(c.cube[5], k=1, axes=(0, 1))
        tmp = deepcopy(c.cube[0])
        # R to F
        c.cube[0][2][0] = c.cube[1][2][0]
        c.cube[0][2][1] = c.cube[1][2][1]
        c.cube[0][2][2] = c.cube[1][2][2]
        # B to R
        c.cube[1][2][0] = c.cube[3][2][0]
        c.cube[1][2][1] = c.cube[3][2][1] 
        c.cube[1][2][2] = c.cube[3][2][2]
        # L to B
        c.cube[3][2][0] = c.cube[4][2][0]
        c.cube[3][2][1] = c.cube[4][2][1]
        c.cube[3][2][2] = c.cube[4][2][2]
        # F to L
        c.cube[4][2][0] = tmp[2][0]
        c.cube[4][2][1] = tmp[2][1]
        c.cube[4][2][2] = tmp[2][2]
    return(c)
