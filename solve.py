import utils
import cube as c
import move
import STEPS.step_one as s

def	process_steps(cube):
	c.print_cube(cube)
	cube = s.step_one(cube)
	print("After solve step_one :")
	c.print_cube(cube)
	print(s.check_valid_step_one(cube))
	return cube
