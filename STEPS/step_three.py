import sys
sys.path.append('..')
import move
import utils

def	step_three(c):
	return c

def	check_step_three(c):
	well_placed = 0
	# check face Front (Blue)
	well_placed += utils.check_face_rows(c.cube[0], 0, 2)
	# check face Right (Red)
	well_placed += utils.check_face_rows(c.cube[1], 1, 2)
	# check face Back (Green)
	well_placed += utils.check_face_rows(c.cube[3], 3, 2)
	# check face Left (Orange)
	well_placed += utils.check_face_rows(c.cube[4], 4, 2)
	# check face down (White)
	well_placed += utils.check_face_rows(c.cube[5], 5, 3)
	return True if well_placed == 33 else False
