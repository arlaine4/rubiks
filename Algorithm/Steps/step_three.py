import sys
sys.path.insert(0, "../../SecondaryFunctions")
sys.path.insert(0, "../../../rubiks")
import SecondaryFunctions.check_colors as check_c
import cubik
from SecondaryFunctions import mix
from SecondaryFunctions import utils


class step_three:
	def __init__(self, cubeOrigin):
		self.cubeOrigin = cubeOrigin
		self.lst_pos_curr = []
		self.lst_pos_origin = []
		self.checkerManager = check_c.CheckerColors()
        self.lst_moves = []

    def set_lst_moves(self, lst_moves):
        self.lst_moves = lst_moves

	def run(self, cubeCurrent, lst_moves):
		if (self.finished_three_color_pos(cubeCurrent, ["green", "orange"])) is False:
			self.moving(cubeCurrent, lst_moves, ["green", "orange"], "front")
		if (self.finished_three_color_pos(cubeCurrent, ["orange", "blue"])) is False:
			self.moving(cubeCurrent, lst_moves, ["orange", "blue"], "left")
		if (self.finished_three_color_pos(cubeCurrent, ["blue", "red"])) is False:
			self.moving(cubeCurrent, lst_moves, ["blue", "red"], "back")
		if (self.finished_three_color_pos(cubeCurrent, ["red", "green"])) is False:
			self.moving(cubeCurrent, lst_moves, ["red", "green"], "right")

	def finished_three_color_pos(self, cubeCurrent, colors_list):
		return cubik.check_pos_color(self.cubeOrigin, cubeCurrent, colors_list[0], colors_list[1])

	def update_pos_lst(self, cub, colors_list):
		return self.checkerManager.two(cub, colors_list[0], colors_list[1])

	def moving(self, cubeCurrent, lst_moves, colors_list, face):
		self.lst_pos_origin = self.update_pos_lst(self.cubeOrigin, colors_list)
		self.lst_pos_curr = self.update_pos_lst(cubeCurrent, colors_list)
		check_side_lst = self.check_side(cubeCurrent, colors_list)
		if check_side_lst[0] is True:
			self.wich_sequences(cubeCurrent, lst_moves, colors_list)
		else:
			if self.lst_pos_curr[0][0] != "down":
				self.push_down(cubeCurrent, lst_moves, colors_list)
				self.lst_pos_curr = self.update_pos_lst(cubeCurrent, colors_list)
			if self.lst_pos_curr[0][0] != "down":
				print ("ERROR DOWN IS NOT")
				sys.exit(-1)
			self.lst_pos_curr = self.update_pos_lst(cubeCurrent, colors_list)
			if self.lst_pos_curr[0][0] == "down":
				self.move_to_center(cubeCurrent, lst_moves, colors_list, face)
				self.lst_pos_curr = self.update_pos_lst(cubeCurrent, colors_list)
				self.wich_sequences(cubeCurrent, lst_moves, colors_list)
	def move_to_center(self, cubeCurrent, lst_moves, colors_list, face):
		check_side_lst = self.check_side(cubeCurrent, colors_list)
		while check_side_lst[0] is False:
			cubeCurrent.move_down()
			lst_moves.append("D")
			check_side_lst = self.check_side(cubeCurrent, colors_list)

	def push_down(self, cubeCurrent, lst_moves, colors_list):
		face_one, face_two, colorOne, colorTwo = self.get_side_params(cubeCurrent, colors_list)
		pattern = self.get_pattern_push_down(face_one, face_two)
		if pattern == "rightPattern":
			self.right_sequence(cubeCurrent, lst_moves, face_one)
		elif pattern == "leftPattern":
			self.left_sequence(cubeCurrent, lst_moves, face_one)

	def get_pattern_push_down(self, face_one, face_two):
		if face_one == "left":
			if face_two == "front":
				return ("rightPattern")
			elif face_two == "back":
				return ("leftPattern")
		elif face_one == "front" and face_two == "right":
				return ("rightPattern")
		elif face_one == "right" and face_two == "back":
			return ("rightPattern")

	def get_side_params(self, cubeCurrent, colors_list):
		self.lst_pos_curr = self.update_pos_lst(cubeCurrent, colors_list)
		down = self.lst_pos_curr[0][0]
		colorDown = self.lst_pos_curr[0][1]
		colorFace = self.lst_pos_curr[1][1]
		face = self.lst_pos_curr[1][0]
		return down, face, colorDown, colorFace

	def check_side(self, cubeCurrent, colors_list):
		down, face, colorDown, colorFace = self.get_side_params(cubeCurrent, colors_list)
		if down != "down":
			return [False, "null"]
		if face == "front":
			if colorDown == "orange" and colorFace == "green":
				return [True, "leftPattern"] 
			elif colorDown == "red" and colorFace == "green":
				return [True, "rightPattern"] 
		if face == "back":
			if colorDown == "orange" and colorFace == "blue":
				return [True, "leftPattern"] 
			elif colorDown == "red" and colorFace == "blue":
				return [True, "rightPattern"]
		if face == "right":
			if colorDown == "blue" and colorFace == "red":
				return [True, "rightPattern"]
			elif colorDown == "green" and colorFace == "red":
				return [True, "leftPattern"] 
		if face == "left":
			if colorDown == "green" and colorFace == "orange":
				return [True, "rightPattern"] 
			elif colorDown == "blue" and colorFace == "orange":
				return [True, "leftPattern"]
		return [False, "null"]

	def wich_sequences(self, cubeCurrent, lst_moves, colors_list):
		down, face, colorDown, colorFace = self.get_side_params(cubeCurrent, colors_list)
		check_side_lst = self.check_side(cubeCurrent, colors_list)
		if check_side_lst[1] == "rightPattern":
			self.right_sequence(cubeCurrent, lst_moves, face)
		elif check_side_lst[1] == "leftPattern":
			self.left_sequence(cubeCurrent, lst_moves, face)

    def left_sequence(self, cubeCurrent, lst_moves, face):
        mixManager = MixManager()

        if face == "front":
            mixManager.runMix([ "D", "L", "D'", "L'", "D'", "F'", "D", "F" ], cubeCurrent)
            self.lst_moves = utils.append_list(self.lst_moves, [ "D", "L", "D'", "L'", "D'", "F'", "D", "F" ])
        elif face == "left":
            mixManager.runMix([ "D", "B", "D'", "B'", "D'", "L'", "D", "L" ], cubeCurrent)
            self.lst_moves = utils.append_list(self.lst_moves, [ "D", "B", "D'", "B'", "D'", "L'", "D", "L" ])
        elif face == "back":
            mixManager.runMix([ "D'", "L'", "D", "L", "D", "B", "D'", "B'" ], cubeCurrent)
            self.lst_moves = utils.append_list(self.lst_moves, [ "D'", "L'", "D", "L", "D", "B", "D'", "B'" ])
        elif face == "right":
            mixManager.runMix([ "D", "F", "D'", "F'", "D'", "R'", "D", "R" ], cubeCurrent)
            self.lst_moves = utils.append_list(self.lst_moves, [ "D", "F", "D'", "F'", "D'", "R'", "D", "R" ])

    def right_sequence(self, cubeCurrent, lst_moves, face):
        mixManager = mix.Mix()
        if face == "front":
            mixManager.runMix([ "D'", "R'", "D", "R", "D", "F", "D'", "F'" ], cubeCurrent)
            self.lst_moves = utils.append_list(self.lst_moves, [ "D'", "R'", "D", "R", "D", "F", "D'", "F'" ])
        elif face == "left":
            mixManager.runMix([ "D'", "F'", "D", "F", "D", "L", "D'", "L'" ], cubeCurrent)
            self.lst_moves = utils.append_list(self.lst_moves, [ "D'", "F'", "D", "F", "D", "L", "D'", "L'" ])
        elif face == "right":
            mixManager.runMix([ "D'", "B'", "D", "B", "D", "R", "D'", "R'"], cubeCurrent)
            self.lst_moves = utils.append_list(self.lst_moves, [ "D'", "B'", "D", "B", "D", "R", "D'", "R'"])
        elif face == "back":
            mixManager.runMix([ "D", "R", "D'", "R'", "D'", "B'", "D", "B" ], cubeCurrent)
            self.lst_moves = utils.append_list(self.lst_moves, [ "D", "R", "D'", "R'", "D'", "B'", "D", "B" ])
