import utils
import cube as c
import move
import STEPS.step_one as s

def print_cube(c): 
    list_move = ['F', 'R', 'U', 'B', 'L', 'D']
    for i in range(len(c.cube)):
        print(list_move[i], ":")
        print(c.cube[i])

def	process_steps(cube):
	print_cube(cube)
	cube = s.step_one(cube)
	print("After solve step_one :")
	print_cube(cube)
	print(s.check_valid_step_one(cube))
	return cube
