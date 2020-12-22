import cube as c
import utils
import visual as visu

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
	nb_bad_edges, pos_bad_edges = edge_o_detection(cube)
	c.print_cube(cube)
	print("Number of bad edges : {}".format(nb_bad_edges))
	for elem in pos_bad_edges:
		print(elem)
	cube = edge_orientation_strategy(cube, nb_bad_edges, pos_bad_edges)
	return cube

def	edge_orientation_strategy(cube, nb_bad_e, pos):
	print(utils.front_or_back(pos))
	if nb_bad_e == 2: #F R U F R2
		edge_o_two(cube, pos)
	elif nb_bad_e == 4: #F R U R B L2 B'  D R F
		pass
	return cube		

def	edge_o_two(cube, pos):
	lst_move = []
	nb_mooves = []
	#for p in pos:
		#select_move_lst, nb_moove = utils.select_best_move_f_b(cube, p)
		#lst_move.append(select_move_lst) ; nb_mooves.append(nb_moove)
	return cube

def	edge_o_detection(cube):
	#calcul en deux etapes du nb de edges mal orientees
	bad_edges_u_d = 0
	bad_edges_f_b = 0
	pos_u_d = []
	pos_f_b = []
	pos = []
	bad_edges_u_d, pos_u_d = o_detection_u_d(cube)
	bad_edges_f_b, pos_f_b = o_detection_f_b(cube)
	pos = pos_u_d + pos_f_b
	return (bad_edges_u_d + bad_edges_f_b), pos 

def	o_detection_u_d(c):
	#detection Up et Down faces
	bad = 0
	pos = []
	if c.cube[2][0][1] == 4 or c.cube[2][0][1] == 1:
		bad += 1 ; pos.append([2, 0, 1])
	if c.cube[2][1][0] == 4 or c.cube[2][1][0] == 1:
		bad += 1 ; pos.append([2, 1, 0])
	if c.cube[2][1][2] == 4 or c.cube[2][1][2] == 1:
		bad += 1 ; pos.append([2, 1, 2])
	if c.cube[2][2][1] == 4 or c.cube[2][2][1] == 1:
		bad += 1 ; pos.append([2, 2, 1])
	if c.cube[2][0][1] == 0 or c.cube[2][0][1] == 3:
		if c.cube[3][0][1] == 2 or c.cube[3][0][1] == 5:
			bad += 1 ; pos.append([3, 0, 1])
	if c.cube[2][1][0] == 0 or c.cube[2][1][0] == 3:
		if c.cube[4][0][1] == 2 or c.cube[4][0][1] == 5:
			bad += 1 ; pos.append([4, 0, 1])
	if c.cube[2][1][2] == 0 or c.cube[2][1][2] == 3:
		if c.cube[1][0][1] == 2 or c.cube[1][0][1] == 5:
			bad += 1 ; pos.append([1, 0, 1])
	if c.cube[2][2][1] == 0 or c.cube[2][2][1] == 3:
		if c.cube[0][0][1] == 2 or c.cube[0][0][1] == 5:
			bad += 1 ; pos.append([0, 0, 1])
	# Down
	if c.cube[5][0][1] == 4 or c.cube[5][0][1] == 1:
		bad += 1 ; pos.append([5, 0, 1])
	if c.cube[5][1][0] == 4 or c.cube[5][1][0] == 1:
		bad += 1 ; pos.append([5, 1, 0])
	if c.cube[5][1][2] == 4 or c.cube[5][1][2] == 1:
		bad += 1 ; pos.append([5, 1, 2])
	if c.cube[5][2][1] == 4 or c.cube[5][2][1] == 1:
		bad += 1 ; pos.append([5, 2, 1])
	if c.cube[5][0][1] == 0 or c.cube[5][0][1] == 3:
		if c.cube[0][2][1] == 2 or c.cube[0][2][1] == 5:
			bad += 1 ; pos.append([0, 2, 1])
	if c.cube[5][1][0] == 0 or c.cube[5][1][0] == 3:
		if c.cube[4][2][1] == 2 or c.cube[4][2][1] == 5:
			bad += 1 ; pos.append([4, 2, 1])
	if c.cube[5][1][2] == 0 or c.cube[5][1][2] == 3:
		if c.cube[1][2][1] == 2 or c.cube[1][2][1] == 5:
			bad += 1 ; pos.append([1, 2, 1])
	if c.cube[5][2][1] == 0 or c.cube[5][2][1] == 3:
		if c.cube[3][2][1] == 2 or c.cube[3][2][1] == 5:
			bad += 1 ; pos.append([5, 2, 1])
	#print("Bad after U_D : ", bad)
	return bad, pos

def	o_detection_f_b(c):
	#detection Front et Back faces
	bad = 0
	pos = []
	# Front
	if c.cube[0][1][0] == 4 or c.cube[0][1][0] == 1:
		bad += 1 ; pos.append([0, 1, 0])
	if c.cube[0][1][2] == 4 or c.cube[0][1][2] == 1:
		bad += 1 ; pos.append([0, 1, 2])
	if c.cube[0][1][0] == 0 or c.cube[0][1][0] == 3:
		if c.cube[4][1][2] == 5 or c.cube[4][1][2] == 2:
			bad += 1 ; pos.append([4, 1, 2])
	if c.cube[0][1][2] == 0 or c.cube[0][1][2] == 3:
		if c.cube[1][1][0] == 2 or c.cube[1][1][0] == 5:
			bad += 1 ; pos.append([1, 1, 0])
	# Back
	if c.cube[3][1][0] == 4 or c.cube[3][1][0] == 1:
		bad += 1 ; pos.append([3, 1, 0])
	if c.cube[3][1][2] == 4 or c.cube[3][1][2] == 1:
		bad += 1 ; pos.append([3, 1, 2])
	if c.cube[3][1][0] == 0 or c.cube[3][1][0] == 3:
		if c.cube[1][1][2] == 5 or c.cube[1][1][2] == 2:
			bad += 1 ; pos.append([1, 1, 2])
	if c.cube[3][1][2] == 0 or c.cube[3][1][2] == 3:
		if c.cube[4][1][0] == 2 or c.cube[4][1][0] == 5:
			bad += 1 ; pos.append([4, 1, 0])
	#print("Bad after F_B : ", bad)
	return bad, pos
#----------------------------------------------------#
