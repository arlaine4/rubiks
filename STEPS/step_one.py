import sys
sys.path.append('..')
import move
import utils

def	step_one(c):
	return c

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
