import argparse
import cube
import move
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

def	check_bad_ud_edges_positions(c):
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
        

def	check_good_ud_edges_positions(c):
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
	#print("c'est bon ou pas ? up", triggered)
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
	#print("c'est bon ou pas ? down", triggered)
	triggered = 0
	#print(pos_up, pos_down)
	return pos_up, pos_down

def check_and_get_ud_slice_edge(cube, face, lst_moves):
	groups = [3, 1, 0, 4]
	if cube.cube[4][1][2] in groups and cube.cube[0][1][0] == 2 if face == "U" else 5: #FL
		move.move_L(cube, True if face == "U" else False)
		lst_moves.append("L" if face == "U" else "L'")
	elif cube.cube[1][1][0] in groups and cube.cube[0][1][2] == 2 if face == "U" else 5: #FR
		move.move_R(cube, True if face == "U" else False)
		lst_moves.append("R" if face == "U" else "R'")
	elif cube.cube[1][1][2] in groups and cube.cube[3][1][0] == 2 if face == "U" else 5: #RB
		move.move_R(cube, False if face == "U" else True)
		lst_moves.append("R'" if face == "U" else "R")
	elif cube.cube[4][1][0] in groups and cube.cube[3][1][2] == 2 if face == "U" else 5: #BL
		move.move_L(cube, False if face == "U" else True)
		lst_moves.append("L'" if face == "U" else "L")
	else:
		return lst_moves, cube, False
	return lst_moves, cube, True

def check_and_get_edge_opposite_face(cube, face, lst_moves):
	if face == "U":
		if cube.cube[0][2][1] in groups and cube.cube[5][0][1] == 2: #DF
			move.move_F(cube, True)
			move.move_F(cube, True)
			lst_moves.append("F2")
		elif cube.cube[1][2][1] in groups and cube.cube[5][1][2] == 2: #DR
			move.move_R(cube, True)
			move.move_R(cube, True)
			lst_moves.append("R2")
		elif cube.cube[3][2][1] in groups and cube.cube[5][2][1] == 2: #DB
			move.move_B(cube, True)
			move.move_B(cube, True)
			lst_moves.append("B2")
		elif cube.cube[4][2][1] in groups and cube.cube[5][1][0] == 2: #DL
			move.move_L(cube, True)
			move.move_L(cube, True)
			lst_moves.append("L2")
	elif face == "D":
		if cube.cube[0][0][1] in groups and cube.cube[2][2][1] == 5: #UF
			move.move_F(cube, True)
			move.move_F(cube, True)
			lst_moves.append("F2")
		elif cube.cube[1][0][1] in groups and cube.cube[2][1][2] == 5: #UR
			move.move_R(cube, True)
			move.move_R(cube, True)
			lst_moves.append("R2")
		elif cube.cube[3][0][1] in groups and cube.cube[2][1][2] == 5: #UB
			move.move_B(cube, True)
			move.move_B(cube, True)
			lst_moves.append("B2")
		elif cube.cube[4][0][1] in groups and cube.cube[2][1][0] == 5: #UL
			move.move_L(cube, True)
			move.move_L(cube, True)
			lst_moves.append("L2")
	return lst_moves, cube

def replace_tpu(lst_order, face):
    new_lst_order = []
    new_value = []
    if face == "U":
        if lst_order == [1, 0, 1]:
            new_lst_order = [2, 1, 2]
            new_value = [2, 1]
        elif lst_order == [0, 0, 1]:
            new_lst_order = [2, 2, 1]
            new_value = [2, 0]
        elif lst_order == [4, 0, 1]:
            new_lst_order = [2, 1, 0]
            new_value = [2, 4]
        elif lst_order == [3, 0, 1]:
            new_lst_order = [2, 0, 1]
            new_value = [2, 3]
    elif face == "D":
        if lst_order == [1, 2, 1]:
            new_lst_order = [5, 1, 2]
            new_value = [5, 1]
        elif lst_order == [3, 2, 1]:
            new_lst_order = [5, 2, 1]
            new_value = [5, 3]
        elif lst_order == [4, 2, 1]:
            new_lst_order = [5, 1, 0]
            new_value = [5, 4]
        elif lst_order == [0, 2, 1]:
            new_lst_order = [5, 0, 1]
            new_value = [5, 0]
    return new_lst_order, new_value

def get_next_edge_placement_pos(order_edge, cube, face):
    next_pos = None
    if face == "U":
        if order_edge == [2, 0, 1]:
            next_pos = [2, 1, 2]
        elif order_edge == [2, 1, 2]:
            next_pos = [2, 2, 1]
        elif order_edge == [2, 2, 1]:
            next_pos = [2, 1, 0]
        elif order_edge == [2, 1, 0]:
            next_pos = [2, 0, 1]
    elif face == "D":
        if order_edge == [5, 0, 1]:
            next_pos = [5, 1, 2]
        elif order_edge == [5, 1, 2]:
            next_pos = [5, 2, 1]
        elif order_edge == [5, 2, 1]:
            next_pos = [5, 1, 0]
        elif order_edge == [5, 1, 0]:
            next_pos = [5, 0, 1]
    return next_pos

def append_bad_edges_values(new_pos, cube):
    value = None
    if new_pos[0] == 0: #Face Front
        if new_pos[1] == 0: #Ligne up
            value = cube.cube[2][2][1]
        elif new_pos[1] == 2: #ligne down
            value = cube.cube[5][0][1]
        elif new_pos[1] == 1: #Ligne middle
            if new_pos[2] == 0: #piece left
                value = cube.cube[4][1][2]
            elif new_pos[2] == 2: #piece right
                value = cube.cube[1][1][0]
    elif new_pos[0] == 1: #Face Right
        if new_pos[1] == 0: #Ligne up
            value = cube.cube[2][1][2]
        elif new_pos[1] == 2: #Ligne down
            value = cube.cube[5][1][2]
        elif new_pos[1] == 1: #Ligne middle
            if new_pos[2] == 0: #piece left
                value = cube.cube[0][1][2]
            elif new_pos[2] == 2:
                value = cube.cube[3][1][0]
    elif new_pos[0] == 2: #Face up
        if new_pos[1] == 0: #Ligne up
            value = cube.cube[3][0][1]
        elif new_pos[1] == 2: #Ligne down
            value = cube.cube[0][0][1]
        elif new_pos[1] == 1: #Ligne middle
            if new_pos[2] == 0:
                value = cube.cube[4][0][1]
            elif new_pos[2] == 2:
                value = cube.cube[1][0][1]
    elif new_pos[0] == 3: #Face back
        if new_pos[1] == 0: #Line up
            value = cube.cube[2][0][1]
        elif new_pos[1] == 2: #Line down
            value = cube.cube[5][2][1]
        elif new_pos[1] == 1: #Line middle
            if new_pos[2] == 0:
                value = cube.cube[1][1][2]
            elif new_pos[2] == 2:
                value = cube.cube[4][1][0]
    elif new_pos[0] == 4: #Face left
        if new_pos[1] == 0:
            value = cube.cube[2][1][0]
        elif new_pos[1] == 2:
            value = cube.cube[5][1][0]
        elif new_pos[1] == 1:
            if new_pos[2] == 0:
                value = cube.cube[3][1][2]
            elif new_pos[2] == 2:
                value = cube.cube[0][1][0]
    elif new_pos[0] == 5: #Face down
        if new_pos[1] == 0:
            value = cube.cube[0][2][1]
        elif new_pos[1] == 2:
            value = cube.cube[3][2][1]
        elif new_pos[1] == 1:
            if new_pos[2] == 0:
                value = cube.cube[4][2][1]
            elif new_pos[2] == 2:
                value = cube.cube[1][2][1]
    return value

def find_and_move_next_edge_placement(cube, lst_order_edges, lst_order_value, bad_edges, bad_edges_value, next_pos, face, lst_moves):
	new_order_edge = []
	new_value_edge = []
	#print("------------------------------------------------------------|")
	#print("|        Print inside find_and_move_next_edge_placement     |\n")
	#print("bad_edges : ", bad_edges)
	#print("bad_edges_values : ",bad_edges_value)
	#print("lst_order_values : ",lst_order_value)
	#print("next_pos : ",next_pos)
	for i in range(6):
		for j in range(3):
			for k in range(3):
				if (j == 0 or j == 2 and k == 1) or (j == 1 and k != 1):
						if cube.cube[i][j][k] == lst_order_value[0]:
							tmp_value = append_bad_edges_values([i, j, k], cube)
							print("inside loop : ", lst_order_value, tmp_value)
							if tmp_value == lst_order_value[1]:
								new_order_edge = [i, j, k]
								new_value_edge = [cube.cube[i][j][k], tmp_value]
								print(new_order_edge)
	print("{} edge has the {} cubie values couple that we are looking for\n---> need to move it to {}".format(new_order_edge, new_value_edge, next_pos))
	print("------------------------------------------------------------|")
	if new_order_edge[0] == 0 and next_pos[0] == 2: # front
		if new_order_edge[1] == 1:
			if next_pos[1] == 0:
				if new_order_edge[2] == 0:
					move.move_U(cube, False)
					move.move_L(cube, False)
					lst_moves.append("U'")
					lst_moves.append("L'")
				if new_order_edge[2] == 2:
					move.move_U(cube, True)
					move.move_R(cube, True)
					lst_moves.append("U")
					lst_moves.append("R")
			elif next_pos[1] == 2:
				if new_order_edge[2] == 0:
					move.move_U(cube, True)
					move.move_L(cube, False)
					lst_moves.append("U")
					lst_moves.append("L'")
				if new_order_edge[2] == 2:
					move.move_U(cube, False)
					move.move_R(cube, True)
					lst_moves.append("U'")
					lst_moves.append("R")
			elif next_pos[1] == 1 and next_pos[2] == 0:
				if new_order_edge[2] == 0:
					move.move_L(cube, False)
					lst_moves.append("L'")
				if new_order_edge[2] == 2:
					move.move_U(cube, True)
					move.move_U(cube, True)
					move.move_R(cube, True)
					lst_moves.append("U2")
					lst_moves.append("R")
			elif next_pos[1] == 1 and next_pos[2] == 2:
				if new_order_edge[2] == 0:
					move.move_U(cube, True)
					move.move_U(cube, True)
					move.move_L(cube, False)
					lst_moves.append("U2")
					lst_moves.append("L'")
				if new_order_edge[2] == 2:
					move.move_R(cube, True)
					lst_moves.append("R")
	if new_order_edge[0] == 2 and next_pos[0] == 2: # deja face up mais pas placer
		if new_order_edge[1] == 0:
			move.move_B(cube, True)
			move.move_B(cube, True)
			lst_moves.append("B2")
			if next_pos[1] == 2:
				move.move_U(cube, True)
				move.move_U(cube, True)
				move.move_B(cube, True)
				move.move_B(cube, True)
				lst_moves.append("U2")
				lst_moves.append("B2")
			elif next_pos[1] == 1 and next_pos[2] == 0:
				move.move_U(cube, True)
				move.move_B(cube, True)
				move.move_B(cube, True)
				lst_moves.append("U")
				lst_moves.append("B2")
			elif next_pos[1] == 1 and next_pos[2] == 2:
				move.move_U(cube, False)
				move.move_B(cube, True)
				move.move_B(cube, True)
				lst_moves.append("U'")
				lst_moves.append("B2")
		elif new_order_edge[1] == 2:
			move.move_F(cube, True)
			move.move_F(cube, True)
			lst_moves.append("F2")
			if next_pos[1] == 0:
				move.move_U(cube, True)
				move.move_U(cube, True)
				move.move_B(cube, True)
				move.move_B(cube, True)
				lst_moves.append("U2")
				lst_moves.append("B2")
			elif next_pos[1] == 1 and next_pos[2] == 0:
				move.move_U(cube, False)
				move.move_B(cube, True)
				move.move_B(cube, True)
				lst_moves.append("U'")
				lst_moves.append("B2")
			elif next_pos[1] == 1 and next_pos[2] == 2:
				move.move_U(cube, True)
				move.move_B(cube, True)
				move.move_B(cube, True)
				lst_moves.append("U")
				lst_moves.append("B2")
		elif new_order_edge[1] == 1 and new_order_edge[2] == 0:
			move.move_L(cube, True)
			move.move_L(cube, True)
			lst_moves.append("L2")
			if next_pos[1] == 1 and next_pos[2] == 2:
				move.move_U(cube, True)
				move.move_U(cube, True)
				move.move_B(cube, True)
				move.move_B(cube, True)
				lst_moves.append("U2")
				lst_moves.append("B2")
			elif next_pos[1] == 0:
				move.move_U(cube, False)
				move.move_B(cube, True)
				move.move_B(cube, True)
				lst_moves.append("U'")
				lst_moves.append("B2")
			elif next_pos[1] == 2:
				move.move_U(cube, True)
				move.move_B(cube, True)
				move.move_B(cube, True)
				lst_moves.append("U")
				lst_moves.append("B2")
		elif new_order_edge[1] == 1 and new_order_edge[2] == 2:
			move.move_R(cube, True)
			move.move_R(cube, True)
			lst_moves.append("R2")
			if next_pos[1] == 1 and next_pos[2] == 0:
				move.move_U(cube, True)
				move.move_U(cube, True)
				move.move_B(cube, True)
				move.move_B(cube, True)
				lst_moves.append("U2")
				lst_moves.append("B2")
			elif next_pos[1] == 0:
				move.move_U(cube, True)
				move.move_B(cube, True)
				move.move_B(cube, True)
				lst_moves.append("U")
				lst_moves.append("B2")
			elif next_pos[1] == 2:
				move.move_U(cube, False)
				move.move_B(cube, True)
				move.move_B(cube, True)
				lst_moves.append("U'")
				lst_moves.append("B2")
	if new_order_edge[0] == 3 and next_pos[0] == 2: # back
		if new_order_edge[1] == 1:
			if next_pos[1] == 0:
				if new_order_edge[2] == 0:
					move.move_U(cube, True)
					move.move_R(cube, False)
					lst_moves.append("U")
					lst_moves.append("R'")
				elif new_order_edge[2] == 2:
					move.move_U(cube, False)
					move.move_L(cube, True)
					lst_moves.append("U'")
					lst_moves.append("L")
			elif next_pos[1] == 2:
				if new_order_edge[2] == 0:
					move.move_U(cube, False)
					move.move_R(cube, False)
					lst_moves.append("U'")
					lst_moves.append("R'")
				elif new_order_edge[2] == 2:
					move.move_U(cube, True)
					move.move_L(cube, True)
					lst_moves.append("U")
					lst_moves.append("L")
			elif next_pos[1] == 1 and next_pos[2] == 0:
				if new_order_edge[2] == 0:
					move.move_U(cube, True)
					move.move_U(cube, True)
					move.move_R(cube, False)
					lst_moves.append("U2")
					lst_moves.append("R'")
				elif new_order_edge[2] == 2:
					move.move_L(cube, True)
					lst_moves.append("L")
			elif next_pos[1] == 1 and next_pos[2] == 2:
				if new_order_edge[2] == 0:
					move.move_R(cube, False)
					lst_moves.append("R'")
				elif new_order_edge[2] == 2:
					move.move_U(cube, True)
					move.move_U(cube, True)
					move.move_L(cube, True)
					lst_moves.append("U2")
					lst_moves.append("L")
	if new_order_edge[0] == 5 and next_pos[0] == 2: # down
			if new_order_edge[1] == 0:
				if next_pos[1] == 0:
					move.move_U(cube, True)
					move.move_U(cube, True)
					move.move_F(cube, True)
					move.move_F(cube, True)
					lst_moves.append("U2")
					lst_moves.append("F2")
				elif next_pos[1] == 2:
					move.move_F(cube, True)
					move.move_F(cube, True)
					lst_moves.append("F2")
				elif next_pos[1] == 1 and next_pos[2] == 0:
					move.move_U(cube, False)
					move.move_F(cube, True)
					move.move_F(cube, True)
					lst_moves.append("U'")
					lst_moves.append("F2")
				elif next_pos[1] == 1 and next_pos[2] == 2:
					move.move_U(cube, True)
					move.move_F(cube, True)
					move.move_F(cube, True)
					lst_moves.append("U")
					lst_moves.append("F2")
			elif new_order_edge[1] == 2:
				if next_pos[1] == 0:
					move.move_B(cube, True)
					move.move_B(cube, True)
					lst_moves.append("B2")
				elif next_pos[1] == 2:
					move.move_U(cube, True)
					move.move_U(cube, True)
					move.move_B(cube, True)
					move.move_B(cube, True)
					lst_moves.append("U2")
					lst_moves.append("B2")
					move.move_U(cube, True)
					move.move_B(cube, True)
					move.move_B(cube, True)
					lst_moves.append("U")
					lst_moves.append("B2")
				elif next_pos[1] == 1 and next_pos[2] == 2:
					move.move_U(cube, False)
					move.move_B(cube, True)
					move.move_B(cube, True)
					lst_moves.append("U'")
					lst_moves.append("B2")
			elif new_order_edge[1] == 1 and new_order_edge[2] == 0:
				if next_pos[1] == 0:
					move.move_U(cube, False)
					move.move_L(cube, True)
					move.move_L(cube, True)
					lst_moves.append("U'")
					lst_moves.append("L2")
				elif next_pos[1] == 2:
					move.move_U(cube, True)
					move.move_L(cube, True)
					move.move_L(cube, True)
					lst_moves.append("U")
					lst_moves.append("L2")
				elif next_pos[1] == 1 and next_pos[2] == 0:
					move.move_L(cube, True)
					move.move_L(cube, True)
					lst_moves.append("L2")
				elif next_pos[1] == 1 and next_pos[2] == 2:
					move.move_U(cube, True)
					move.move_U(cube, True)
					move.move_L(cube, True)
					move.move_L(cube, True)
					lst_moves.append("U2")
					lst_moves.append("L2")
			elif new_order_edge[1] == 1 and new_order_edge[2] == 2: # ici
				if next_pos[1] == 0:
					move.move_U(cube, True)
					move.move_B(cube, True)
					move.move_B(cube, True)
					lst_moves.append("U")
					lst_moves.append("B2")
				elif next_pos[1] == 2:
					move.move_U(cube, False)
					move.move_B(cube, True)
					move.move_B(cube, True)
					lst_moves.append("U'")
					lst_moves.append("B2")
				if next_pos[1] == 1 and next_pos[2] == 0:
					move.move_U(cube, True)
					move.move_U(cube, True)
					move.move_B(cube, True)
					move.move_B(cube, True)
					lst_moves.append("U2")
					lst_moves.append("B2")
				if next_pos[1] == 1 and next_pos[2] == 2:
					move.move_B(cube, True)
					move.move_B(cube, True)
					lst_moves.append("B2")


	# if face == "U":
	# 	for i in range(len(bad_edges_value)):
	# 		if bad_edges_value[i] == lst_order_value:
	# 			print("this edge {} has {} value but needs to be placed at {}".format(bad_edges[i], bad_edges_value[i], next_pos))
	# elif face == "D":
	# 	pass
	new_order_edge = next_pos
	p = new_order_edge
	new_value_edge = [cube.cube[p[0]][p[1]][p[2]], append_bad_edges_values([p[0],p[1],p[2]], cube)]
	return cube, lst_moves, new_order_edge, new_value_edge
