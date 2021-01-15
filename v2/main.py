from SecondaryFunctions import utils, mix
import cubik as c

if __name__ == "__main__":
    args = utils.arg_parse()
    cube = cubik.Cube(3)
    lst_moves = []
    if args.random:
        lst_moves = mix.Mix.randomMove(args.iterations)
    elif not args.random:
        lst_moves = args.mix.split(' ')
    mix.Mix.runMix(lst_move, cube)
    #add in utils.arg_parse argument for number of moves in random shuffle generator
    #and call the classic shuffle or the random shuffle based on args
    #shuffle = Mix()
    #if args.r:
        #shuffle.randomMove(
