import move
import utils

def	step_two(c):
	return c

def	check_step_two(c):
	well_placed = 0
	#---------------------------------------------
	# Partie check face blanche complete
	for i in range(3):
		for j in range(3):
			if c.cube[5][i][j] == 5:
				well_placed += 1
	if well_placed != 9: #Temporaire
		print("Face blanche pas finie") #temporaire
	#---------------------------------------------

	#---------------------------------------------
	# Partie check face Front (Blue)
	for f in range(3):
		if c.cube[0][0][f] == 0:
			well_placed += 1
	if c.cube[0][1][1] == 0:
		well_placed += 1
	#---------------------------------------------

	#---------------------------------------------
	# Partie check face Right (Red)
	for r in range(3):
		if c.cube[1][0][r] == 1:
			well_placed += 1
	if c.cube[1][1][1] == 1:
		well_placed += 1
	#---------------------------------------------

	#---------------------------------------------
	# Partie check face Back (Green)
	for b in range(3):
		if c.cube[3][0][b] == 3:
			well_placed += 1
	if c.cube[3][1][1] == 3:
		well_placed += 1
	#---------------------------------------------

	#---------------------------------------------
	# Partie check face Left (Orange)
	for l in range(3):
		if c.cube[4][0][l] == 4:
			well_placed += 1
	if c.cube[4][1][1] == 4:
		well_placed += 1
	#---------------------------------------------

	if well_placed == 25:
		return True
	else:
		return False	
