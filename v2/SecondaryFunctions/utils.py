import argparse

def arg_parse():
    parser = argparse.ArgumentParser()
    parser.add_argument("mix", action="store", help="cube shuffle")
    parser.add_argument("r", "-r", action='store_true', help='random mix generator')
    #add argument for number of moves in random shuffle generator
    #parser.add_argument("")
    options = parser.parse_args()
    return options
