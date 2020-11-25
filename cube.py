import numpy as np

class Cube():
	def	__init__(self, initial_mix):
		self.cube = load_inital_solved_cube()
		self.coups = 0
		self.walk_coups = ""

def	load_inital_solved_cube():
	cube = np.zeros((6, 3, 3,), dtype=np.int)
	for i in range(6):
		cube[i] = int(i)
	return cube

def	return_color(case):
	if case == 0:
		return 34
	elif case == 1:
		return 31
	elif case == 2:
		return "33"
	elif case == 3:
		return 32
	elif case == 4:
		return 208
	elif case == 5:
		return 231

def	print_cube(c, colors=True):
	if not colors:
		list_move = ['F', 'R', 'U', 'B', 'L', 'D']
		print("\n       {}\n       {}\n       {}".format(c.cube[2][0], c.cube[2][1], c.cube[2][2]))
		print("{}{}{}{}".format(c.cube[4][0], c.cube[0][0], c.cube[1][0], c.cube[3][0]))
		print("{}{}{}{}".format(c.cube[4][1], c.cube[0][1], c.cube[1][1], c.cube[3][1]))
		print("{}{}{}{}".format(c.cube[4][2], c.cube[0][2], c.cube[1][2], c.cube[3][2]))
	elif colors:
		#-------------------------------------------------------------#
		#  PAS TOUCHE AU BAZAR EN DESSOUS C'ETAIT SUPER RELOU A FAIRE #
		#-------------------------------------------------------------#
		cc = np.empty((6, 3, 3), dtype=object)
		for i in range(6):
			for j in range(3):
				for k in range(3):
					color = return_color(c.cube[i][j][k])
					cc[i][j][k] = "\033[" + str(color) + "m"
		print("       "+cc[2][0][0]+'# '+cc[2][0][1]+'# '+cc[2][0][2]+'#')
		print("       "+cc[2][1][0]+'# '+cc[2][1][1]+'# '+cc[2][1][2]+'#')
		print("       "+cc[2][2][0]+'# '+cc[2][2][1]+'# '+cc[2][2][2]+'#', end='\n\n')
		print(cc[4][0][0]+'# '+cc[4][0][1]+'# '+cc[4][0][2]+'#'+'  ', end='')
		print(cc[0][0][0]+'# '+cc[0][0][1]+'# '+cc[0][0][2]+'#'+'  ', end='')
		print(cc[1][0][0]+'# '+cc[1][0][1]+'# '+cc[1][0][2]+'#'+'  ', end='')
		print(cc[3][0][0]+'# '+cc[3][0][1]+'# '+cc[3][0][2]+'#')
		print(cc[4][1][0]+'# '+cc[4][1][1]+'# '+cc[4][1][2]+'#'+'  ', end='')
		print(cc[0][1][0]+'# '+cc[0][1][1]+'# '+cc[0][1][2]+'#'+'  ', end='')
		print(cc[1][1][0]+'# '+cc[1][1][1]+'# '+cc[1][1][2]+'#'+'  ', end='')
		print(cc[3][1][0]+'# '+cc[3][1][1]+'# '+cc[3][1][2]+'#')
		print(cc[4][2][0]+'# '+cc[4][2][1]+'# '+cc[4][2][2]+'#'+'  ', end='')
		print(cc[0][2][0]+'# '+cc[0][2][1]+'# '+cc[0][2][2]+'#'+'  ', end='')
		print(cc[1][2][0]+'# '+cc[1][2][1]+'# '+cc[1][2][2]+'#'+'  ', end='')
		print(cc[3][2][0]+'# '+cc[3][2][1]+'# '+cc[3][2][2]+'#', end='\n\n')
		print("       "+cc[5][0][0]+'# '+cc[5][0][1]+'# '+cc[5][0][2]+'#')
		print("       "+cc[5][1][0]+'# '+cc[5][1][1]+'# '+cc[5][1][2]+'#')
		print("       "+cc[5][2][0]+'# '+cc[5][2][1]+'# '+cc[5][2][2]+'#', end='\n\n')
		print("\33[0m")

def	check_face_rows(face, id_face, rows_to_check):
	well_placed = 0
	for i in range(rows_to_check):
		for j in range(3):
			if face[i][j] == id_face:
				well_placed += 1
	return well_placed
