import move as m
import cube as c
import visual as visu
import utils
import hta

def     edges_placement(cube, bad_edges, good_edges, lst_moves):

    #----------------------------------------------------#
    #                   Left cubie                       #

    if cube.cube[0][1][0] == 2 or cube.cube[0][1][0] == 5:
        if cube.cube[4][1][2] == 4 and cube.cube[0][1][2] == 2:
            cube = m.move_L(cube, False) ; lst_moves.append("L'")
        elif cube.cube[4][1][2] == 4 and cube.cube[0][1][2] == 5:
            cube = m.move_L(cube, True) ; lst_moves.append("L")
        elif cube.cube[4][1][2] != 4 and cube.cube[0][1][2] == 2:
            if cube.cube[4][1][2] == 
            cube = m.move_L(cube, True) ; lst_moves.append("L")
            cube = m.move_U(cube, True) ; lst_moves.append("U")
    if cube.cube[1][1][0] == 2 or cube.cube[1][1][0] == 5:
    if cube.cube[3][1][0] == 2 or cube.cube[3][1][0] == 5:
    if cube.cube[4][1][0] == 2 or cube.cube[4][1][0] == 5:

    #----------------------------------------------------#
    #                   Right cubie                      #

    if cube.cube[0][1][2] == 2 or cube.cube[0][1][2] == 5:
    if cube.cube[1][1][2] == 2 or cube.cube[1][1][2] == 5:
    if cube.cube[3][1][2] == 2 or cube.cube[3][1][2] == 5:
    if cube.cube[4][1][2] == 2 or cube.cube[4][1][2] == 5:

    return cube, lst_moves
