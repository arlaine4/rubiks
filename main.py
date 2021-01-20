from SecondaryFunctions import utils, mix
from Algorithm import Algo as a
import sys
import cubik as c

if __name__ == "__main__":
    args = utils.arg_parse()
    cube = c.Cube(3)
    mix_ = mix.Mix()
    if len(args.mix) == 0:
        print("Random moves generator not triggered, and hand written mix not valid, please try again with a valid mix.")
        sys.exit(0)
    scramble = args.mix
    scramble = scramble.split(' ')
    cube = mix_.runMix(scramble, cube)
    if args.visual is False:
        cube.print_cube()
    algo = a.Algo(cube)
    solution = algo.run()
    if args.visual is False:
        cube.print_cube()
        print("Solution found in {} moves".format(len(solution)))
    else:
        print("Visual coming soon")
