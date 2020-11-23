import sys
sys.path.append('..')
import move
import utils

def	step_one(c):
	color_prio = [0, 4, 3, 1]
	for color in color_prio:
		check = False
		if already_valid(c, color):
			continue
		c, check = case_one(c, color)
		if check:
			continue
		c, check = case_two(c, color)
		if check:
			continue
	return c

def case_two(c, color):
	return c, False
def case_one(c, color):
	if color == 0:
		if c.cube[1][1][0] == 5 and c.cube[0][1][2] == color:
			move.move_F(c, True)
			return c, True
		if c.cube[4][1][2] == 5 and c.cube[0][1][0] == color:
			move.move_F(c, False)
			return c, True
		if c.cube[2][2][1] == 5 and c.cube[0][0][1] == color:
			move.move_F(c, True)
			move.move_F(c, True)
			return c, True
	if color == 4:
		if c.cube[4][1][2] == color and c.cube[0][1][0] == 5:
			move.move_L(c, True)
			return c, True
		if c.cube[3][1][2] == 5 and c.cube[4][1][0] == color:
			move.move_L(c, False)
			return c, True
		if c.cube[2][1][0] == 5 and c.cube[4][0][1] == color:
			move.move_L(c, True)
			move.move_L(c, True)
			return c, True
	if color == 3:
		if c.cube[3][1][2] == color and c.cube[4][1][0] == 5:
			move.move_B(c, True)
			return c, True
		if c.cube[1][1][2] == 5 and c.cube[3][1][0] == color:
			move.move_B(c, False)
			return c, True
		if c.cube[2][0][1] == 5 and c.cube[3][0][1] == color:
			move.move_B(c, True)
			move.move_B(c, True)
			return c, True
	if color == 1:
		if c.cube[1][1][2] == color and c.cube[3][1][0] == 5:
			move.move_R(c, True)
			return c, True
		if c.cube[0][1][2] == 5 and c.cube[1][1][0] == color:
			move.move_R(c, False)
			return c, True
		if c.cube[2][1][2] == 5 and c.cube[1][0][1] == color:
			move.move_R(c, True)
			move.move_R(c, True)
			return c, True
	return c, False

def already_valid(c, color):
	if color == 0:
		if c.cube[5][0][1] == 5 and c.cube[0][2][1] == color:
			return True
	if color == 4:
		if c.cube[5][1][0] == 5 and c.cube[4][2][1] == color:
			return True
	if color == 3:
		if c.cube[5][1][2] == 5 and c.cube[3][2][1] == color:
			return True
	if color == 1:
		if c.cube[5][2][1] == 5 and c.cube[1][2][1] == color:
			return True

def	check_valid_step_one(c):
	well_placed = 0

	#--------------------------------------------
	# Partie check white cross
	for j in range(3):
		if c.cube[5][j][1] == 5:
			well_placed += 1
	if c.cube[5][1][0] == 5:
		well_placed += 1
	if c.cube[5][1][2] == 5:
		well_placed += 1
	if well_placed != 5: #Temporaire
		print("White cross pas finie dans step ONE") #Temporaire
	#--------------------------------------------

	#--------------------------------------------
	# Partie check des middle colors de F R B L
	if c.cube[0][0][1] == 0 and c.cube[0][0][1] == 0: #BLUE Front
		well_placed += 2
	if c.cube[1][0][1] == 1 and c.cube[1][1][1] == 1: #RED Right
		well_placed += 2
	if c.cube[3][0][1] == 3 and c.cube[3][1][1] == 3: #GREEN Back
		well_placed += 2
	if c.cube[4][0][1] == 4 and c.cube[4][1][1] == 4: #ORANGE Left
		well_placed += 2
	#
	#--------------------------------------------

	if well_placed == 13:
		return True
	else:
		return False
