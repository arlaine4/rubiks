import argparse

def arg_parse():
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--mix", required=True, help="cube shuffle")
    parser.add_argument("-v", "--visual", action="store_true", help="Show visual")
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
