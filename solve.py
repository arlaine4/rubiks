import utils
import cube as c
import move
import time
import twophase as tp

def	process_steps(cube, pack):
	c.print_cube(cube)
	tp.phase_main(cube, pack)
	return cube
