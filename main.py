from SecondaryFunctions import utils, mix
from Algorithm import Algo as a
import sys
import cubik as c
import visual as visu

if __name__ == "__main__":
    args = utils.arg_parse()
    cube = c.Cube(3)
    mix_ = mix.Mix()
    cube.print_cube()
    if len(args.mix) == 0:
        print("Random moves generator not triggered, and hand written mix not valid, please try again with a valid mix.")
        sys.exit(0)
    lst_moves = args.mix
    lst_moves = lst_moves.split(' ')
    cube = mix_.runMix(lst_moves, cube)
    cube.print_cube()
    algo = a.Algo(cube)
    solution = algo.run()
    if args.visual:
        visu.main_visual(args.mix, solution)
    cube.print_cube()
