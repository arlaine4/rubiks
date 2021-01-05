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

def	select_best_move_f_b(cube, pos):
	move_lst = []
	nb_mooves = 0
	#Select best move(s) to place an edge in F or B face
	#regarding his position

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
