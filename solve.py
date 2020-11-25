import utils
import cube as c
import move
import STEPS.step_one as s
import time

def	process_steps(cube):
	c.print_cube(cube)
	cube = s.step_one(cube)
	print("After solve step_one :")
	for i in range(100):
		c.print_cube(cube)
		time.sleep(1)
	print(s.check_valid_step_one(cube))
	return cube
