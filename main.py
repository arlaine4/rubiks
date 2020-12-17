import numpy as np
import utils
import cube as c
import move
import solve
import visual as visu

if __name__ == "__main__":
	options = utils.arg_parse_options()
	cube = c.Cube(options.mix)
	corientation = {"URF" : 0, "UFL" : 0, "ULB" : 0, "UBR" : 0, "DFR" : 0, "DLF" : 0, "DBL" : 0, "DRB" : 0}
	eoriantation = {"UR" : 0, "UF" : 0, "UL" : 0, "UB" : 0, "DR" : 0, "DF" : 0, "DL" : 0, "DB" : 0, "FR" : 0, "FL" : 0, "BL" : 0, "BR" : 0}
	pack = [corientation, eoriantation]
	if options.visu:
		visu.main_visual(cube, options.mix, pack)
	else:
		cube, pack = utils.shuffle_cube(options.mix, cube, pack)
		cube = solve.process_steps(cube, pack)
