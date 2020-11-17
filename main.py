import numpy as np
import utils
import cube as c
import move

if __name__ == "__main__":
	options = utils.arg_parse_options()
	cube = c.Cube(options.mix)
	utils.shuffle_cube(options.mix, cube)
	print(options.mix)
