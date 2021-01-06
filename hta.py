import cube as c
import utils
import move as m
import visual as visu
import edge_orientation as edge_t_f
import edge_placement as edge_p
import corners_orientation as corners

groups = [['U', 'D', 'L', 'R', 'F2', 'B2'], ['U', 'D', 'L2', 'R2', 'F2', 'B2'],
	['U2', 'D2', 'L2', 'R2', 'F2', 'B2']]

def	main_algo(cube):
        cube, lst_moves = edge_orientation(cube)
        cube, lst_moves = placement_ud_edges(cube, lst_moves)
        return cube, lst_moves

#----------------------------------------------------#
# 			First step, edge orientation

def	edge_orientation(cube):
	#Pour edge orientation on vas first compter le nb
	#de edge qui sont mal orientees
	pos_bad_edges = edge_o_detection(cube)
	print("Number of bad edges \033[33mbefore\033[0m : {}".format(len(pos_bad_edges)))
	c.print_cube(cube)
	# for elem in pos_bad_edges:	# DEBUG
	# 	print(elem)					# DEBUG
	cube, lst_moves = edge_orientation_strategy(cube, pos_bad_edges)
	pos_bad_edges = edge_o_detection(cube)
	print("Number of bad edges \033[35mafter\033[0m: {}".format(len(pos_bad_edges)))
	c.print_cube(cube)
	# for elem in pos_bad_edges:	# DEBUG
	# 	print(elem)					# DEBUG
	return cube, lst_moves

def     placement_ud_edges(cube, lst_moves):
        good_edges = []
        bad_edges = []
        good_edges = utils.check_good_ud_edges_positions(cube)
        bad_edges = utils.check_bad_ud_edges_positions(cube)
        cube, lst_moves = edge_p.edges_placement(cube, bad_edges, good_edges, lst_moves) 
        return cube, lst_moves

def	edge_orientation_strategy(cube, pos):
	nb_bad_e = len(pos)
	lst_move = []
	if nb_bad_e == 2: # F R U F R2
		cube, lst_move = edge_t_f.edge_o_two(cube, pos, lst_move)
	elif nb_bad_e == 4: # F R U R B L2 B' # DEJA TOUS SUR LA FACE "B" : F2 U2 D B
		cube, lst_move = edge_t_f.edge_o_four(cube, pos, lst_move)
	elif nb_bad_e == 6: # R F2 B' D' L U2 L2 D2 B # F2 U2 D B U' F2 U' R' L' D2 U2 F2 F2 B' L
		cube, lst_move = edge_t_f.edge_o_four(cube, pos, lst_move)
		pos = edge_o_detection(cube)
		cube, lst_move = edge_t_f.edge_o_two(cube, pos, lst_move)
	elif nb_bad_e == 8: # R' D F2 R B' U F' D' F2 # F U2 D2 B2 U' F U' R' L' D U F B2 # F2 U2 D B F2 U' R' L' D2 U2 F2 F2 B' L D U2 F'
		cube, lst_move = edge_t_f.edge_o_four(cube, pos, lst_move)
		pos = edge_o_detection(cube)
		cube, lst_move = edge_t_f.edge_o_four(cube, pos, lst_move)
	elif nb_bad_e == 10:
		cube, lst_move = edge_t_f.edge_o_four(cube, pos, lst_move)
		pos = edge_o_detection(cube)
		cube, lst_move = edge_t_f.edge_o_four(cube, pos, lst_move)
		pos = edge_o_detection(cube)
		cube, lst_move = edge_t_f.edge_o_two(cube, pos, lst_move)
	elif nb_bad_e == 12:
		cube, lst_move = edge_t_f.edge_o_four(cube, pos, lst_move)
		pos = edge_o_detection(cube)
		cube, lst_move = edge_t_f.edge_o_four(cube, pos, lst_move)
		pos = edge_o_detection(cube)
		cube, lst_move = edge_t_f.edge_o_four(cube, pos, lst_move)
	return cube, lst_move

def	edge_o_detection(cube):
	#calcul en deux etapes du nb de edges mal orientees
	pos_u_d = []
	pos_f_b = []
	pos = []
	pos_u_d = o_detection_u_d(cube)
	pos_f_b = o_detection_f_b(cube)
	pos = pos_u_d + pos_f_b
	return pos

def	o_detection_u_d(c):
	#detection Up et Down faces
	pos = []
	if c.cube[2][0][1] == 4 or c.cube[2][0][1] == 1:
		pos.append([2, 0, 1])
	if c.cube[2][1][0] == 4 or c.cube[2][1][0] == 1:
		pos.append([2, 1, 0])
	if c.cube[2][1][2] == 4 or c.cube[2][1][2] == 1:
		pos.append([2, 1, 2])
	if c.cube[2][2][1] == 4 or c.cube[2][2][1] == 1:
		pos.append([2, 2, 1])
	if c.cube[2][0][1] == 0 or c.cube[2][0][1] == 3:
		if c.cube[3][0][1] == 2 or c.cube[3][0][1] == 5:
			pos.append([3, 0, 1])
	if c.cube[2][1][0] == 0 or c.cube[2][1][0] == 3:
		if c.cube[4][0][1] == 2 or c.cube[4][0][1] == 5:
			pos.append([4, 0, 1])
	if c.cube[2][1][2] == 0 or c.cube[2][1][2] == 3:
		if c.cube[1][0][1] == 2 or c.cube[1][0][1] == 5:
			pos.append([1, 0, 1])
	if c.cube[2][2][1] == 0 or c.cube[2][2][1] == 3:
		if c.cube[0][0][1] == 2 or c.cube[0][0][1] == 5:
			pos.append([0, 0, 1])
	# Down
	if c.cube[5][0][1] == 4 or c.cube[5][0][1] == 1:
		pos.append([5, 0, 1])
	if c.cube[5][1][0] == 4 or c.cube[5][1][0] == 1:
		pos.append([5, 1, 0])
	if c.cube[5][1][2] == 4 or c.cube[5][1][2] == 1:
		pos.append([5, 1, 2])
	if c.cube[5][2][1] == 4 or c.cube[5][2][1] == 1:
		pos.append([5, 2, 1])
	if c.cube[5][0][1] == 0 or c.cube[5][0][1] == 3:
		if c.cube[0][2][1] == 2 or c.cube[0][2][1] == 5:
			pos.append([0, 2, 1])
	if c.cube[5][1][0] == 0 or c.cube[5][1][0] == 3:
		if c.cube[4][2][1] == 2 or c.cube[4][2][1] == 5:
			pos.append([4, 2, 1])
	if c.cube[5][1][2] == 0 or c.cube[5][1][2] == 3:
		if c.cube[1][2][1] == 2 or c.cube[1][2][1] == 5:
			pos.append([1, 2, 1])
	if c.cube[5][2][1] == 0 or c.cube[5][2][1] == 3:
		if c.cube[3][2][1] == 2 or c.cube[3][2][1] == 5:
			pos.append([5, 2, 1])
	return pos

def	o_detection_f_b(c):
	#detection Front et Back faces
	pos = []
	# Front
	if c.cube[0][1][0] == 4 or c.cube[0][1][0] == 1:
		pos.append([0, 1, 0])
	if c.cube[0][1][2] == 4 or c.cube[0][1][2] == 1:
		pos.append([0, 1, 2])
	if c.cube[0][1][0] == 0 or c.cube[0][1][0] == 3:
		if c.cube[4][1][2] == 5 or c.cube[4][1][2] == 2:
			pos.append([4, 1, 2])
	if c.cube[0][1][2] == 0 or c.cube[0][1][2] == 3:
		if c.cube[1][1][0] == 2 or c.cube[1][1][0] == 5:
			pos.append([1, 1, 0])
	# Back
	if c.cube[3][1][0] == 4 or c.cube[3][1][0] == 1:
		pos.append([3, 1, 0])
	if c.cube[3][1][2] == 4 or c.cube[3][1][2] == 1:
		pos.append([3, 1, 2])
	if c.cube[3][1][0] == 0 or c.cube[3][1][0] == 3:
		if c.cube[1][1][2] == 5 or c.cube[1][1][2] == 2:
			pos.append([1, 1, 2])
	if c.cube[3][1][2] == 0 or c.cube[3][1][2] == 3:
		if c.cube[4][1][0] == 2 or c.cube[4][1][0] == 5:
			pos.append([4, 1, 0])
	return pos
