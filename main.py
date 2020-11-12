import numpy as np
import utils
import cube as c
import move

if __name__ == "__main__":
	options = utils.arg_parse_options()
	cube = c.Cube(options.mix)
	move.move_F(cube, False)
	print(options.mix)
