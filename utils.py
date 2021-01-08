import argparse
import cube
import move as m
import sys

import visual as visu
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

def arg_parse_options():
	"""Parsing arguments"""
	parser = argparse.ArgumentParser()
	parser.add_argument("mix", action="store", help="melange du cube")
	parser.add_argument("-v", "--visu", action="store_true", help="trigger visual")
	options = parser.parse_args()
	return options

def	select_move_function_to_call(move_id, cube):
	repeat = 1 #nombre de repetitions du move
	nb_letter = 0
	lst_valid_elems = ['F', 'L', 'R', 'B', 'U', 'D', "'"]
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
	elif "R" in move_id:
		for loop in range(repeat):
			cube = move.move_R(cube, False) if "'" in move_id else move.move_R(cube, True)
	elif "B" in move_id:
		for loop in range(repeat):
			cube = move.move_B(cube, False) if "'" in move_id else move.move_B(cube, True)
	elif "L" in move_id:
		for loop in range(repeat):
			cube = move.move_L(cube, False) if "'" in move_id else move.move_L(cube, True)
	elif "U" in move_id:
		for loop in range(repeat):
			cube = move.move_U(cube, False) if "'" in move_id else move.move_U(cube, True)
	elif "D" in move_id:
		for loop in range(repeat):
			cube = move.move_D(cube, False) if "'" in move_id else move.move_D(cube, True)
	return cube.cube

def Do_I_move(positions, face, nb = False):
	x = 0
	for pos in positions:
		# Front bad edges
		if face == "F":
			if pos[0] == 0:
				x += 1
			if pos[0] == 4 and pos[1] == 1 and pos[2] == 2:
				x += 1
			if pos[0] == 1 and pos[1] == 1 and pos[2] == 0:
				x += 1
			if pos[0] == 5 and pos[1] == 0 and pos[2] == 1:
				x += 1
			if pos[0] == 2 and pos[1] == 2 and pos[2] == 1:
				x += 1
		# Back bad edges
		if face == "B":
			if pos[0] == 3:
				x += 1
			if pos[0] == 4 and pos[1] == 1 and pos[2] == 0:
				x += 1
			if pos[0] == 1 and pos[1] == 1 and pos[2] == 2:
				x += 1
			if pos[0] == 5 and pos[1] == 2 and pos[2] == 1:
				x += 1
			if pos[0] == 2 and pos[1] == 0 and pos[2] == 1:
				x += 1
	if nb == False:
		if x == 4:
			return True
		return False
	if nb == True:
		return x

def front_or_back(positions):
	f = 0
	b = 0
	for pos in positions:
		# Front bad edges
		if pos[0] == 0:
			f += 1
		if pos[0] == 4 and pos[1] == 1 and pos[2] == 2:
			f += 1
		if pos[0] == 1 and pos[1] == 1 and pos[2] == 0:
			f += 1
		if pos[0] == 5 and pos[1] == 0 and pos[2] == 1:
			f += 1
		if pos[0] == 2 and pos[1] == 2 and pos[2] == 1:
			f += 1
		# Back bad edges
		if pos[0] == 3:
			b += 1
		if pos[0] == 4 and pos[1] == 1 and pos[2] == 0:
			b += 1
		if pos[0] == 1 and pos[1] == 1 and pos[2] == 2:
			b += 1
		if pos[0] == 5 and pos[1] == 2 and pos[2] == 1:
			b += 1
		if pos[0] == 2 and pos[1] == 0 and pos[2] == 1:
			b += 1
	# print("F : {} | B : {}".format(f, b))
	return "F" if f >= b else "B" 

def	shuffle_cube(mix, c):
	c.main_walk = mix
	moves = mix.split(' ')
	for i in range(len(moves)):
		c.cube = select_move_function_to_call(moves[i], c)
	return c

def     check_bad_ud_edges_positions(c):
        pos = []
        #-----------------------------------------#
        #               Up Check                  #
        #-----------------------------------------#
        if c.cube[2][0][1] != 2:
            pos.append([2, 0, 1])
        if c.cube[2][1][0] != 2:
            pos.append([2, 1, 0])
        if c.cube[2][1][2] != 2:
            pos.append([2, 1, 2])
        if c.cube[2][2][1] != 2:
            pos.append([2, 2, 1])
        #-----------------------------------------#
        #               Down Check                #
        #-----------------------------------------#
        if c.cube[5][0][1] != 5:
            pos.append([5, 0, 1])
        if c.cube[5][1][0] != 5:
            pos.append([5, 1, 0])
        if c.cube[5][1][2] != 5:
            pos.append([5, 1, 2])
        if c.cube[5][2][1] != 5:
            pos.append([5, 2, 1])
        return pos
        

def     check_good_ud_edges_positions(c):
		pos_up = []
		pos_down = []
		up_coord = [[2,0,1,3,0,1],[2,1,0,4,0,1],[2,2,1,0,0,1],[2,1,2,1,0,1]]
		up_value = [[2,3],[2,4],[2,0],[2,1]]
		# up_check = [[[3],[4],[0],[1]],[[1],[3],[4],[0]],[[0],[1],[3],[4]],[[4],[0],[1],[3]]]
		down_coord = [[5,0,1,0,2,1],[5,1,0,4,2,1],[5,2,1,3,2,1],[5,1,2,1,2,1]]
		down_value = [[5,0],[5,4],[5,3],[5,1]]
		triggered = 0
		#-----------------------------------------#
		#               Up Check                  #
		#-----------------------------------------#
		for i in range(len(up_coord)):
			for j in range(len(up_value)):
				if c.cube[up_coord[i][0]][up_coord[i][1]][up_coord[i][2]] == up_value[j][0]\
					and c.cube[up_coord[i][3]][up_coord[i][4]][up_coord[i][5]] == up_value[j][1]:
					triggered += 1
					pos_up.append(up_coord[i][3:])
		print("c'est bon ou pas ? up", triggered)
		triggered = 0
		# test = []
		# check = []
		# keep = []
		# for elem in up_coord:
		# 	test.append(elem[3:])
		# for elem in test:
		# 	if elem in pos:
		# 		check.append(c.cube[elem[0]][elem[1]][elem[2]])
		# 	else:
		# 		check.append(-1)
		#-----------------------------------------#
		#               Down Check                #
		#-----------------------------------------#
		for i in range(len(down_coord)):
			for j in range(len(down_value)):
				if c.cube[down_coord[i][0]][down_coord[i][1]][down_coord[i][2]] == down_value[j][0]\
					and c.cube[down_coord[i][3]][down_coord[i][4]][down_coord[i][5]] == down_value[j][1]:
					triggered += 1
					pos_down.append(down_coord[i][:3])
		print("c'est bon ou pas ? down", triggered)
		triggered = 0
		print(pos_up, pos_down)
		return pos_up, pos_down

def check_and_get_ud_slice_edge(cube, face, lst_moves):
	#----------------------------------------------------------------------#
	#                               Up                                     #
	groups = [3, 1, 0, 4]
	if cube.cube[4][1][2] in groups and cube.cube[0][1][0] == 2 if face == "U" else 5: #FL
		lst_moves = m.move_L(cube, True)
	elif cube.cube[1][1][0] in groups and cube.cube[0][1][2] == 2: #FR
		lst_moves = m.move_R(cube, True)
	elif cube.cube[1][1][2] in groups and cube.cube[3][1][0] == 2: #RB
		lst_moves = m.move_R(cube, False)
	elif cube.cube[4][1][0] in groups and cube.cube[3][1][2] == 2: #BL
		lst_moves = m.move_L(cube, False)
	#----------------------------------------------------------------------#
	#                               Down                                   #
	return lst_moves, cube
