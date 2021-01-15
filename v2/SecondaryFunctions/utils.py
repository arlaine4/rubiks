import argparse

def arg_parse():
    parser = argparse.ArgumentParser()
    parser.add_argument("mix", action="store", help="cube shuffle")
    parser.add_argument("random", "--r", action='store_true', help='random mix generator')
    parser.add_argument("iterations", "--i", actopm='store_true', type=int, help='number of moves in random shuffle')
    options = parser.parse_args()
    return options
