import utils
import cube as c
import move
import time
import twophase as tp
import twophase_convert as tpc

def	process_steps(cube):
	c.print_cube(cube)
	tpc.convert(cube)
	# print(tp.phase_one(cube))
	return cube
