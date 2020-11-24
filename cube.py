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

def print_cube(c):
	list_move = ['F', 'R', 'U', 'B', 'L', 'D']
	print("\n       {}\n       {}\n       {}".format(c.cube[2][0], c.cube[2][1], c.cube[2][2]))
	print("{}{}{}{}".format(c.cube[4][0], c.cube[0][0], c.cube[1][0], c.cube[3][0]))
	print("{}{}{}{}".format(c.cube[4][1], c.cube[0][1], c.cube[1][1], c.cube[3][1]))
	print("{}{}{}{}".format(c.cube[4][2], c.cube[0][2], c.cube[1][2], c.cube[3][2]))
	print("       {}\n       {}\n       {}\n".format(c.cube[5][0], c.cube[5][1], c.cube[5][2]))
    #for i in range(len(c.cube)):
        #print(list_move[i], ":")
        #print(c.cube[i])

def	check_face_rows(face, id_face, rows_to_check):
	well_placed = 0
	for i in range(rows_to_check):
		for j in range(3):
			if face[i][j] == id_face:
				well_placed += 1
	return well_placed
