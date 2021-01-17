from SecondaryFunctions import utils, mix
import sys
import cubik as c

if __name__ == "__main__":
    args = utils.arg_parse()
    cube = c.Cube(3)
    mix_ = mix.Mix()
    if len(args.mix) == 0:
        print("Random moves generator not triggered, and hand written mix not valid, please try again with a valid mix.")
        sys.exit(0)
    lst_moves = args.mix
    cube = mix_.runMix(lst_moves, cube)
    cube.print_cube()
