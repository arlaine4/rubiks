import utils
import cube as c
import move
import STEPS.step_one as s

def print_cube(c): 
	list_move = ['F', 'R', 'U', 'B', 'L', 'D']
	print("\n       {}\n       {}\n       {}".format(c.cube[2][0], c.cube[2][1], c.cube[2][2]))
	print("{}{}{}{}".format(c.cube[4][0], c.cube[0][0], c.cube[1][0], c.cube[3][0]))
	print("{}{}{}{}".format(c.cube[4][1], c.cube[0][1], c.cube[1][1], c.cube[3][1]))
	print("{}{}{}{}".format(c.cube[4][2], c.cube[0][2], c.cube[1][2], c.cube[3][2]))
	print("       {}\n       {}\n       {}\n".format(c.cube[5][0], c.cube[5][1], c.cube[5][2]))
    #for i in range(len(c.cube)):
        #print(list_move[i], ":")
        #print(c.cube[i])

def	process_steps(cube):
	print_cube(cube)
	cube = s.step_one(cube)
	print("After solve step_one :")
	print_cube(cube)
	print(s.check_valid_step_one(cube))
	return cube
