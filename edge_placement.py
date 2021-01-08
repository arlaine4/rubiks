import move as m
import cube as c
import visual as visu
import utils
import hta

def		edges_placement(cube, bad_edges, good_edges_up, good_edges_down, lst_moves):
	t_p_u = [[2, 0, 1, 3, 0, 1], [2, 1, 0, 4, 0, 1], [2, 2, 1, 0, 0, 1], [2, 1, 2, 1, 0, 1]]
	t_p_d = [[5, 0, 1, 0, 2, 1], [5, 1, 0, 4, 2, 1], [5, 2, 1, 3, 2, 1], [5, 1, 2, 1, 2, 1]]
	value_pos_up = [[2, 3], [2, 4], [2, 0], [2, 1]]
	value_pos_down = [[5, 0], [5, 4], [5, 3], [5, 1]]
	lst_order_edges = []
	lst_order_values = []
	id_current = 0
	pos_starting_point = []
	value_starting_point = []
	#separer good edge en up et down
	#-----------------------------------------------------------#
	#                       Partie Up                           #
	#--------------------------#
	# Selection starting point #
	if len(good_edges_up) > 0:
			lst_order_edges.append(good_edges_up[0])
			lst_order_values.append([good_edges_up[0][0], cube.cube[good_edges_up[0][0]][good_edges_up[0][1]][good_edges_up[0][2]]])
	elif len(good_edges_up) == 0:
			lst_moves, cube = utils.check_ud_slice_edge(cube, "U", lst_moves) #call avec bad_edges ou avec good_edges_down ?
	print("order edges : ", lst_order_edges, "order values : ", lst_order_values)
	return cube, lst_moves
			"""if len(good_edges) > 0:
					lst_order_edges.append(good_edges[0])
		lst_order_values.append([good_edges[0][0], cube.cube[good_edges[0]][good_edges[1]][good_edges[2]]])
		#check les good_edges suivantes si elles sont deja sur la bonne face et dans le bon ordre
		#meme si elle sont pas a la bonne place
		#si elle sont bonnes, append a order_edge et order_values
	elif len(good_edges) == 0:
		pass
		#chercher edge en ud_slice, prendre la premiere que on trouve
			#move un edge ud_slice sur la face up sur l'edge la plus proche, qui coute le moins de coups
		##chercher une edge de up qui serait sur down
			#move un edge down sur la face up sur l'edge la plus proche, qui coute le moins de coups
		#re assigner lst_order_edges et lst_order_values
	#-------------------------#

	#deplacer une a une les edge a la suite de lst_order[i] en checkant lst_order_values[i] pour savoir
	#de quel edge de la face on part

	#on passe pas a l'edge suivante tant que la courrante n'est pas a la suite de la precedente

	#forbid F and B moves
	#append every move to lst_moves
	#ne pas faire de move de la face ou on se situe si ca nique l'ordre ni qui niquerai le placement
	#d'une edge deja dans lst_order_edges
	return cube, lst_moves"""


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
