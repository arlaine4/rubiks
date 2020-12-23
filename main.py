import numpy as np
import utils
import cube as c
import move
import hta
import visual as visu
import copy

if __name__ == "__main__":
	options = utils.arg_parse_options()
	cube = c.Cube(options.mix)
	cube_before = copy.deepcopy(cube)
	cube = utils.shuffle_cube(options.mix, cube)
	cube, lst_moves = hta.main_algo(cube)
	if options.visu:
		visu.main_visual(cube_before, options.mix, lst_moves)
