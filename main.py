import numpy as np
import utils
import cube as c

if __name__ == "__main__":
	options = utils.arg_parse_options()
	cube = c.Cube(options.mix)
	print(options.mix)
