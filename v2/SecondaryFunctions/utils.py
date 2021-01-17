import argparse

def arg_parse():
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--mix", required=True, help="cube shuffle")
    options = parser.parse_args()
    return options
