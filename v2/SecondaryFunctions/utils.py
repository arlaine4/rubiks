import argparse

def arg_parse():
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--mix", required=True, help="cube shuffle")
    options = parser.parse_args()
    return options

def append_list(lst_moves, to_add):
    for elem in to_add:
        lst_moves.append(elem)
    return(lst_moves)
