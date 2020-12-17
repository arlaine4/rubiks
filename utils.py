import argparse
import cube
import move
import sys

import visual as visu
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *


# Up-move
coU = {"URF" : 0, "UFL" : 0, "ULB" : 0, "UBR" : 0, "DFR" : 0, "DLF" : 0, "DBL" : 0, "DRB" : 0}
eoU = {"UR" : 0, "UF" : 0, "UL" : 0, "UB" : 0, "DR" : 0, "DF" : 0, "DL" : 0, "DB" : 0, "FR" : 0, "FL" : 0, "BL" : 0, "BR" : 0}
# Right-move
coR = {"URF" : 2, "UFL" : 0, "ULB" : 0, "UBR" : 1, "DFR" : 1, "DLF" : 0, "DBL" : 0, "DRB" : 2}
eoR = {"UR" : 0, "UF" : 0, "UL" : 0, "UB" : 0, "DR" : 0, "DF" : 0, "DL" : 0, "DB" : 0, "FR" : 0, "FL" : 0, "BL" : 0, "BR" : 0}
# Front-move
coF = {"URF" : 1, "UFL" : 2, "ULB" : 0, "UBR" : 0, "DFR" : 2, "DLF" : 1, "DBL" : 0, "DRB" : 0}
eoF = {"UR" : 0, "UF" : 1, "UL" : 0, "UB" : 0, "DR" : 0, "DF" : 1, "DL" : 0, "DB" : 0, "FR" : 1, "FL" : 1, "BL" : 0, "BR" : 0}
# Down-move
coD = {"URF" : 0, "UFL" : 0, "ULB" : 0, "UBR" : 0, "DFR" : 0, "DLF" : 0, "DBL" : 0, "DRB" : 0}
eoD = {"UR" : 0, "UF" : 0, "UL" : 0, "UB" : 0, "DR" : 0, "DF" : 0, "DL" : 0, "DB" : 0, "FR" : 0, "FL" : 0, "BL" : 0, "BR" : 0}
# Left-move
coL = {"URF" : 0, "UFL" : 1, "ULB" : 2, "UBR" : 0, "DFR" : 0, "DLF" : 2, "DBL" : 1, "DRB" : 0}
eoL = {"UR" : 0, "UF" : 0, "UL" : 0, "UB" : 0, "DR" : 0, "DF" : 0, "DL" : 0, "DB" : 0, "FR" : 0, "FL" : 0, "BL" : 0, "BR" : 0}
# Back-move
coB = {"URF" : 0, "UFL" : 0, "ULB" : 1, "UBR" : 2, "DFR" : 0, "DLF" : 0, "DBL" : 2, "DRB" : 1}
eoB = {"UR" : 0, "UF" : 0, "UL" : 0, "UB" : 1, "DR" : 0, "DF" : 0, "DL" : 0, "DB" : 1, "FR" : 0, "FL" : 0, "BL" : 1, "BR" : 1}

def arg_parse_options():
	"""Parsing arguments"""
	parser = argparse.ArgumentParser()
	parser.add_argument("mix", action="store", help="melange du cube")
	parser.add_argument("-v", "--visu", action="store_true", help="trigger visual")
	options = parser.parse_args()
	return options

def	select_move_function_to_call(move_id, cube, pack):
	repeat = 1 #nombre de repetitions du move
	nb_letter = 0
	lst_valid_elems = ['F', 'L', 'R', 'B', 'U', 'D', "'"]
	# Unpack elem
	corientation = pack[0]
	eorientation = pack[1]
	#-----------------------------------------------------------------------------
	# Petit parsing de check de validite de la string mix
	for c in move_id:
		if c.isdigit() and c == "2":
			repeat = int(c)
		elif c not in lst_valid_elems:
			print("{} is not a valid mix char, please enter a valid mix.".format(c))
			sys.exit()
		elif c.isalpha():
			nb_letter += 1
		if nb_letter > 1:
			print("Error in mix parameter, please enter a valid mix.")
			sys.exit(0)
	if nb_letter == 0:
		print("Error in mix parameter, please_enter a valid mix.")
		sys.exit(0)
	#
	#-----------------------------------------------------------------------------
	if "F" in move_id:
		for loop in range(repeat):
			cube = move.move_F(cube, False) if "'" in move_id else move.move_F(cube, True)
			if not "'" in move_id:
				corientation["UFL"] += 2
				corientation["UFL"] %= 3
				corientation["DFR"] += 2
				corientation["DFR"] %= 3
				corientation["DLF"] += 1
				corientation["DLF"] %= 3
				corientation["URF"] += 1
				corientation["URF"] %= 3
			else:
				corientation["UFL"] += 1
				corientation["UFL"] %= 3
				corientation["DFR"] += 1
				corientation["DFR"] %= 3
				corientation["DLF"] += 2
				corientation["DLF"] %= 3
				corientation["URF"] += 2
				corientation["URF"] %= 3
	elif "R" in move_id:
		for loop in range(repeat):
			cube = move.move_R(cube, False) if "'" in move_id else move.move_R(cube, True)
			if not "'" in move_id:	
				corientation["URF"] += 2
				corientation["URF"] %= 3
				corientation["DRB"] += 2
				corientation["DRB"] %= 3
				corientation["UBR"] += 1
				corientation["UBR"] %= 3
				corientation["DFR"] += 1
				corientation["DFR"] %= 3
			else:
				corientation["URF"] += 1
				corientation["URF"] %= 3
				corientation["DRB"] += 1
				corientation["DRB"] %= 3
				corientation["UBR"] += 2
				corientation["UBR"] %= 3
				corientation["DFR"] += 2
				corientation["DFR"] %= 3
	elif "B" in move_id:
		for loop in range(repeat):
			cube = move.move_B(cube, False) if "'" in move_id else move.move_B(cube, True)
			if not "'" in move_id:	
				corientation["UBR"] += 2
				corientation["UBR"] %= 3
				corientation["DBL"] += 2
				corientation["DBL"] %= 3
				corientation["ULB"] += 1
				corientation["ULB"] %= 3
				corientation["DRB"] += 1
				corientation["DRB"] %= 3
			else:
				corientation["UBR"] += 1
				corientation["UBR"] %= 3
				corientation["DBL"] += 1
				corientation["DBL"] %= 3
				corientation["ULB"] += 2
				corientation["ULB"] %= 3
				corientation["DRB"] += 2
				corientation["DRB"] %= 3
	elif "L" in move_id:
		for loop in range(repeat):
			cube = move.move_L(cube, False) if "'" in move_id else move.move_L(cube, True)
			if not "'" in move_id:	
				corientation["ULB"] += 2
				corientation["ULB"] %= 3
				corientation["DLF"] += 2
				corientation["DLF"] %= 3
				corientation["UFL"] += 1
				corientation["UFL"] %= 3
				corientation["DBL"] += 1
				corientation["DBL"] %= 3
			else:
				corientation["ULB"] += 1
				corientation["ULB"] %= 3
				corientation["DLF"] += 1
				corientation["DLF"] %= 3
				corientation["UFL"] += 2
				corientation["UFL"] %= 3
				corientation["DBL"] += 2
				corientation["DBL"] %= 3
	elif "U" in move_id:
		for loop in range(repeat):
			cube = move.move_U(cube, False) if "'" in move_id else move.move_U(cube, True)
	elif "D" in move_id:
		for loop in range(repeat):
			cube = move.move_D(cube, False) if "'" in move_id else move.move_D(cube, True)
	return cube.cube, [corientation, eorientation]

def	shuffle_cube(mix, c, pack):
	c.main_walk = mix
	moves = mix.split(' ')
	for i in range(len(moves)):
		c.cube, pack = select_move_function_to_call(moves[i], c, pack)
	return c, pack
