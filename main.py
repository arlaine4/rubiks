from SecondaryFunctions import utils, mix
from Algorithm import Algo as a
import sys
import cubik as c

if __name__ == "__main__":
    args = utils.arg_parse()
    cube = c.Cube(3)
    mix_ = mix.Mix()
    if args.mix is None:
        lst_moves = mix_.create()
    else:
        lst_moves = args.mix
        lst_moves = lst_moves.split(' ')
        if mix_.valid(lst_moves) is False:
            print("The hand written mix seems to be weird, please try again with a valid mix.")
            sys.exit(0)
    #-----------------------------------------#
    #           Cube Shuffle                  #
    cube = mix_.runMix(lst_moves, cube)
    cube.print_cube()
    #                                         #
    #-----------------------------------------#

    #-----------------------------------------#
    #           Cube Solve                    #
    algo = a.Algo(cube)
    solution = algo.run()
    #                                         #
    #-----------------------------------------#

    #-----------------------------------------#
    #           Printing solution             #
    cube.print_cube()
    print("Solution found in {} moves".format(len(solution)))
    print("The list of moves :")
    for move in solution:
        print(move, end=' ')
    print()
    #                                         #
    #-----------------------------------------#
