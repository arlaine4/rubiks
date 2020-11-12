import argparse

def arg_parse_options():
	parser = argparse.ArgumentParser()
	parser.add_argument("mix", action="store", help="melange du cube")
	parser.add_argument("-v", "--visu", action="store_true", help="trigger visual")
	options = parser.parse_args()
	return options
