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
	return cube

def	edge_o_detection(cube):
	#calcul en deux etapes du nb de edges mal orientees
	bad_edges += o_detection_u_d(cube, bad_edge)
	bad_edges += o_detection_f_b(cube, bad_edge)
	return bad_edges

def	o_detection_u_d(cube, bad_edge):
	#detection Up et Down faces
	return bad_edge

def	o_detection_f_b(cube, bad_edge):
	#detection Front et Back faces
	return bad_edge 

#----------------------------------------------------#
