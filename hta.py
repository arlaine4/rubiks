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
	nb_bad_edges = edge_o_detection(cube)
	c.print_cube(cube)
	print(nb_bad_edges)
	return cube

def	edge_o_detection(cube):
	#calcul en deux etapes du nb de edges mal orientees
	bad_edges = 0
	bad_edges += o_detection_u_d(cube)
	bad_edges += o_detection_f_b(cube)
	return bad_edges

def	o_detection_u_d(c):
	#detection Up et Down faces
	bad = 0
	# Up
	if c.cube[2][0][1] == 4 or c.cube[2][0][1] == 1:
		bad += 1
	elif c.cube[2][1][0] == 4 or c.cube[2][1][0] == 1:
		bad += 1
	elif c.cube[2][1][2] == 4 or c.cube[2][1][2] == 1:
		bad += 1
	elif c.cube[2][2][1] == 4 or c.cube[2][2][1] == 1:
		bad += 1
	if c.cube[2][0][1] == 0 or c.cube[2][0][1] == 3:
		if c.cube[3][0][1] == 2 or c.cube[3][0][1] == 5:
			bad += 1
	elif c.cube[2][1][0] == 0 or c.cube[2][1][0] == 3:
		if c.cube[4][0][1] == 2 or c.cube[4][0][1] == 5:
			bad += 1
	elif c.cube[2][1][2] == 0 or c.cube[2][1][2] == 3:
		if c.cube[1][0][1] == 2 or c.cube[1][0][1] == 5:
			bad += 1
	elif c.cube[2][2][1] == 0 or c.cube[2][2][1] == 3:
		if c.cube[0][0][1] == 2 or c.cube[0][0][1] == 5:
			bad += 1
	print("Bad after up : ", bad)
	# Down
	if c.cube[5][0][1] == 4 or c.cube[5][0][1] == 1:
		bad += 1
	elif c.cube[5][1][0] == 4 or c.cube[5][1][0] == 1:
		bad += 1
	elif c.cube[5][1][2] == 4 or c.cube[5][1][2] == 1:
		bad += 1
	elif c.cube[5][2][1] == 4 or c.cube[5][2][1] == 1:
		bad += 1
	if c.cube[5][0][1] == 0 or c.cube[5][0][1] == 3:
		if c.cube[0][2][1] == 2 or c.cube[0][2][1] == 5:
			bad += 1
	elif c.cube[5][1][0] == 0 or c.cube[5][1][0] == 3:
		if c.cube[4][2][1] == 2 or c.cube[4][2][1] == 5:
			bad += 1
	elif c.cube[5][1][2] == 0 or c.cube[5][1][2] == 3:
		if c.cube[1][2][1] == 2 or c.cube[1][2][1] == 5:
			bad += 1
	elif c.cube[5][2][1] == 0 or c.cube[5][2][1] == 3:
		if c.cube[3][2][1] == 2 or c.cube[3][2][1] == 5:
			bad += 1
	print("Bad after down : ", bad)
	return bad

def	o_detection_f_b(c):
	#detection Front et Back faces
	bad = 0
	# Front
	if c.cube[0][0][1] == 4 or c.cube[0][0][1] == 1:
		bad += 1
	elif c.cube[0][1][0] == 4 or c.cube[0][1][0] == 1:
		bad += 1
	elif c.cube[0][1][2] == 4 or c.cube[0][1][2] == 1:
		bad += 1
	elif c.cube[0][2][1] == 4 or c.cube[0][2][1] == 1:
		bad += 1
	if c.cube[0][0][1] == 0 or c.cube[0][0][1] == 3:
		if c.cube[2][2][1] == 5:
			bad += 1
	elif c.cube[0][1][0] == 0 or c.cube[0][1][0] == 3:
		if c.cube[4][1][2] == 2 or c.cube[4][1][2] == 5:
			bad += 1
	elif c.cube[0][1][2] == 0 or c.cube[0][1][2] == 3:
		if c.cube[1][1][0] == 2 or c.cube[1][1][0] == 5:
			bad += 1
	elif c.cube[0][2][1] == 0 or c.cube[0][2][1] == 3:
		if c.cube[5][0][1] == 2:
			bad += 1
	print("Bad after front : ", bad)
	# Back
	if c.cube[3][0][1] == 4 or c.cube[3][0][1] == 1:
		bad += 1
	elif c.cube[3][1][0] == 4 or c.cube[3][1][0] == 1:
		bad += 1
	elif c.cube[3][1][2] == 4 or c.cube[3][1][2] == 1:
		bad += 1
	elif c.cube[3][2][1] == 4 or c.cube[3][2][1] == 1:
		bad += 1
	if c.cube[3][0][1] == 0 or c.cube[3][0][1] == 3:
		if c.cube[2][0][1] == 5:
			bad += 1
	elif c.cube[3][1][0] == 0 or c.cube[3][1][0] == 3:
		if c.cube[1][1][2] == 2 or c.cube[1][1][2] == 5:
			bad += 1
	elif c.cube[3][1][2] == 0 or c.cube[3][1][2] == 3:
		if c.cube[4][1][0] == 2 or c.cube[4][1][0] == 5:
			bad += 1
	elif c.cube[3][2][1] == 0 or c.cube[3][2][1] == 3:
		if c.cube[5][2][1] == 2:
			bad += 1
	print("Bad after back : ", bad)
	return bad
#----------------------------------------------------#
