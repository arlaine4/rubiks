import utils
import cube as c
import move
import time
import twophase as tp

def	process_steps(cube):
	c.print_cube(cube)
	print(tp.phase_one(cube))
	return cube
