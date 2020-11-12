import numpy as np

class Cube():
	def	__init__(self, initial_mix):
		self.cube = load_inital_solved_cube()
		self.coups = 0
		self.walk_coups = ""

	def	__str__(self):
		return '{}\n{}\n{}\n{}\n{}\n{}'.format(cube[0], cube[1], cube[2], cube[3], cube[4], cube[5], cube[6])

def	load_inital_solved_cube():
	cube = np.zeros((6, 3, 3,), dtype=np.int)
	for i in range(6):
		cube[i] = int(i)
	return cube
