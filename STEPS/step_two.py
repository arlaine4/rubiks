import sys
sys.path.append('..')
import move
import utils

def	step_two(c):
	return c

def	check_step_two(c):
	well_placed = 0
	# Partie check face blanche complete
	well_placed += utils.check_face_rows(c.cube[5], 5, 3)
	if well_placed != 9: #Will be deleted later
		print('Face blanche pas finie dans step TWO')
	# Partie check face Front (Blue)
	well_placed += utils.check_face_rows(c.cube[0], 0, 1)
	if c.cube[0][1][1] == 0:
		well_placed += 1
	# Partie check face Right (Red)
	well_placed += utils.check_face_rows(c.cube[1], 1, 1)
	if c.cube[1][1][1] == 1:
		well_placed += 1
	# Partie check face Back (Green)
	well_placed += utils.check_face_rows(c.cube[3], 3, 1)
	if c.cube[3][1][1] == 3:
		well_placed += 1
	# Partie check face Left (Orange)
	well_placed += utils.check_face_rows(c.cube[4], 4, 1)
	if c.cube[4][1][1] == 4:
		well_placed += 1
	return True if well_placed == 25 else False
