import move as m
import cube as c
import visual as visu
import utils
import hta

def     edges_placement(cube, bad_edges, good_edges, lst_moves):
        t_p_u = [[2, 0, 1, 3, 0, 1], [2, 1, 0, 4, 0, 1], [2, 2, 1, 0, 0, 1], [2, 1, 2, 1, 0, 1]]
        t_p_d = [[5, 0, 1, 0, 2, 1], [5, 1, 0, 4, 2, 1], [5, 2, 1, 3, 2, 1], [5, 1, 2, 1, 2, 1]]
        value_pos_up = [[2, 3], [2, 4], [2, 0], [2, 1]]
        value_pos_down = [[5, 0], [5, 4], [5, 3], [5, 1]]
        lst_order_edges = []
        lst_order_values = []
        id_current = 0
        if len(good_edges) > 0:
            lst_order_edges.append(good_edges[0])
            lst_order_values.append([good_edges[0][0], cube.cube[good_edges[0]][good_edges[1]][good_edges[2]])
        elif len(good_edges) == 0:
            #TO DO
        

        #------------------------------------#
        #            Up                      #
        if len(good_edges) > 0:
            
        return cube, lst_moves


"""def     edges_placement(cube, bad_edges, good_edges, lst_moves):

	#----------------------------------------------------#
	#                   Left cubie                       #

	# if cube.cube[0][1][0] == 2 or cube.cube[0][1][0] == 5:
	# 	if cube.cube[4][1][2] == 4 and cube.cube[0][1][2] == 2:
	# 		cube = m.move_L(cube, False) ; lst_moves.append("L'")
	# 	elif cube.cube[4][1][2] == 4 and cube.cube[0][1][2] == 5:
	# 		cube = m.move_L(cube, True) ; lst_moves.append("L")
	# 	elif cube.cube[4][1][2] != 4 and cube.cube[0][1][2] == 2:
	# 		if cube.cube[4][1][2] == 4:
	# 			cube = m.move_L(cube, True) ; lst_moves.append("L")
	# 			cube = m.move_U(cube, True) ; lst_moves.append("U")
	# if cube.cube[1][1][0] == 2 or cube.cube[1][1][0] == 5:
	# if cube.cube[3][1][0] == 2 or cube.cube[3][1][0] == 5:
	# if cube.cube[4][1][0] == 2 or cube.cube[4][1][0] == 5:

	# #----------------------------------------------------#
	# #                   Right cubie                      #

	# if cube.cube[0][1][2] == 2 or cube.cube[0][1][2] == 5:
	# if cube.cube[1][1][2] == 2 or cube.cube[1][1][2] == 5:
	# if cube.cube[3][1][2] == 2 or cube.cube[3][1][2] == 5:
	# if cube.cube[4][1][2] == 2 or cube.cube[4][1][2] == 5:

	return cube, lst_moves"""
