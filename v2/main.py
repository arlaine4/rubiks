from SecondaryFunctions import utils, mix
import sys
import cubik as c

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
