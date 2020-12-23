import cube as c
import utils
import move as m
import visual as visu
import edge_two_four as edge_t_f

groups = [['U', 'D', 'L', 'R', 'F2', 'B2'], ['U', 'D', 'L2', 'R2', 'F2', 'B2'],
	['U2', 'D2', 'L2', 'R2', 'F2', 'B2']]

def	main_algo(cube):
	cube = step_one(cube)
	return cube

#----------------------------------------------------#
# 			First step, edge orientation

def	step_one(cube):
	cube = edge_orientation(cube)
	return cube

def	edge_orientation(cube):
	#Pour edge orientation on vas first compter le nb
	#de edge qui sont mal orientees
	pos_bad_edges = edge_o_detection(cube)
	c.print_cube(cube)
	print("Number of bad edges \033[33mbefore\033[0m : {}".format(len(pos_bad_edges)))
	for elem in pos_bad_edges:
		print(elem)
	cube = edge_orientation_strategy(cube, pos_bad_edges)
	pos_bad_edges = edge_o_detection(cube)
	print("Number of bad edges \033[35mafter\033[0m: {}".format(len(pos_bad_edges)))
	for elem in pos_bad_edges:
		print(elem)
	return cube

def	edge_orientation_strategy(cube, pos):
	nb_bad_e = len(pos)
	if nb_bad_e == 2: #F R U F R2
		cube = edge_t_f.edge_o_two(cube, pos)
	elif nb_bad_e == 4: #F R U R B L2 B'  D R F
		cube = edge_t_f.edge_o_four(cube, pos)
	return cube		

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
