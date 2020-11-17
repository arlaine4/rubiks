import argparse
import cube
import move

def arg_parse_options():
	parser = argparse.ArgumentParser()
	parser.add_argument("mix", action="store", help="melange du cube")
	parser.add_argument("-v", "--visu", action="store_true", help="trigger visual")
	options = parser.parse_args()
	return options

def	select_move_function_to_call(move_id, cube):
	if move_id == "F":
		cube = move.move_F(cube, False) if "'" in move_id else move.move_F(cube, True)
	elif move_id == "R":
		cube = move.move_R(cube, False) if "'" in move_id else move.move_R(cube, True)
	elif move_id == "B":
		cube = move.move_B(cube, False) if "'" in move_id else move.move_B(cube, True)
	return cube

def	shuffle_cube(mix, c):
	c.main_walk = mix
	moves = mix.split(' ')
	for i in range(len(moves)):
		c.cube = select_move_function_to_call(moves[i], c)
	return c
