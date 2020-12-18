import numpy as np
import utils
import cube as c
import move
import hta as algo
import visual as visu

if __name__ == "__main__":
	options = utils.arg_parse_options()
	cube = c.Cube(options.mix)
	if options.visu:
		visu.main_visual(cube, options.mix)
	else:
		cube = utils.shuffle_cube(options.mix, cube)
		cube = algo.main_algo(cube)
