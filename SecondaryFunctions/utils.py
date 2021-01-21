import argparse
import sys
import moves_for_visu as move

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
	return cube


def arg_parse():
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--mix", required=True, help="cube shuffle")
    parser.add_argument("-v", "--visual", action="store_true", help="trigger visual")
    options = parser.parse_args()
    return options

def check_back_state(cubFace, color):
	if cubFace[0][1] == color and cubFace[1][1] == color and cubFace[1][2] == color and cubFace[1][0] == color and cubFace[2][1] == color:
		return (4, 0)
	elif cubFace[1][0] == color and cubFace[1][1] == color and cubFace[1][2] == color:
		return (3, 0)
	elif cubFace[0][1] == color and cubFace[1][1] == color and cubFace[2][1] == color:
		return (3, 1)
	elif cubFace[2][1] == color and cubFace[1][1] == color and cubFace[1][2] == color:
		return (2, 0)
	elif cubFace[1][0] == color and cubFace[1][1] == color and cubFace[2][1] == color:
		return (2, 1)
	elif cubFace[0][1] == color and cubFace[1][1] == color and cubFace[1][0] == color:
		return (2, 2)
	elif cubFace[0][1] == color and cubFace[1][1] == color and cubFace[1][2] == color:
		return (2, 3)
	elif cubFace[1][1] == color:
		return (1, 0)
	return False, False

def append_list(lst_moves, to_add):
    for elem in to_add:
        lst_moves.append(elem)
    return(lst_moves)
