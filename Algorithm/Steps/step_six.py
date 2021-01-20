import sys
sys.path.insert(0, "../../SecondaryFunctions")
sys.path.insert(0, "../../../rubiks")
import SecondaryFunctions.check_colors as check_c
import cubik
from SecondaryFunctions import mix
from SecondaryFunctions import utils

class step_six:
	def __init__(self, cubeOrigin):
		self.cubeOrigin = cubeOrigin
		self.lst_pos_curr = []
		self.checker = check_c.CheckerColors()
        self.lst_moves = []

	def 	run(self, cubeCurrent, lst_moves):
		res = self.check_corner(cubeCurrent)
		if res == 4:
			return True
		else:
			res = self.check_next_pos(cubeCurrent)
			if (res[0] == 4):
				return True
			else:
				if res[0] == 0:
					self.move_to_next_pos(cubeCurrent, lst_moves, ["D", "L", "D'", "R'", "D", "L'", "D'", "R"])
				res = self.check_next_pos(cubeCurrent)
				colorsList = res[1]
				lst_pattern = self.get_pattern(cubeCurrent, colorsList)
				self.move_fown_face(cubeCurrent, lst_moves, lst_pattern)

	def 	move_fown_face(self, cubeCurrent, lst_moves, lst_pattern):
		face = lst_pattern[1]
		if face == "frontFace":
			if lst_pattern[0] == "right":
				self.move_to_next_pos(cubeCurrent, lst_moves, ["D", "L", "D'", "R'", "D", "L'", "D'", "R"])
			else:
				self.move_to_next_pos(cubeCurrent, lst_moves, ["D'", "R'", "D", "L", "D'", "R", "D", "L'"])
		elif face == "backFace":
			if lst_pattern[0] == "right":
				self.move_to_next_pos(cubeCurrent, lst_moves, ["D", "R", "D'", "L'", "D", "R'", "D'", "L"])
			else:
				self.move_to_next_pos(cubeCurrent, lst_moves, ["D'", "L'", "D", "R", "D'", "L", "D", "R'"])
		elif face == "rightFace":
			if lst_pattern[0] == "right":
				self.move_to_next_pos(cubeCurrent, lst_moves, ["D", "F", "D'", "B'", "D", "F'", "D'", "B"])
			else:
				self.move_to_next_pos(cubeCurrent, lst_moves, ["D'", "B'", "D", "F", "D'", "B", "D", "F'"])
		elif face == "leftFace":
			if lst_pattern[0] == "right":
				self.move_to_next_pos(cubeCurrent, lst_moves, ["D", "B", "D'", "F'", "D", "B'", "D'", "F"])
			else:
				self.move_to_next_pos(cubeCurrent, lst_moves, ["D'", "F'", "D", "B", "D'", "F", "D", "B'"])
	
	def 	get_pattern(self, cubeCurrent, colorsList):
		lst_pattern = []
		if ["yellow", "green", "red"] == colorsList:
			lst_pattern.append(self.get_direction(cubeCurrent))
			if (lst_pattern[0] == "left"):
				lst_pattern.append("frontFace")
			else:
				lst_pattern.append("rightFace")
		elif (["yellow", "blue", "orange"] == colorsList):
			lst_pattern.append(self.get_direction(cubeCurrent))
			if (lst_pattern[0] == "left"):
				lst_pattern.append("backFace")
			else:
				lst_pattern.append("leftFace")
		elif (["yellow", "blue", "red"] == colorsList):
			lst_pattern.append(self.get_direction(cubeCurrent))
			if (lst_pattern[0] == "left"):
				lst_pattern.append("rightFace")
			else:
				lst_pattern.append("backFace")
		elif (["yellow", "green", "orange"] == colorsList):
			lst_pattern.append(self.get_direction(cubeCurrent))
			if (lst_pattern[0] == "left"):
				lst_pattern.append("leftFace")
			else:
				lst_pattern.append("frontFace")
		return lst_pattern

	def 	get_direction(self, cubeCurrent):
		cubeCurrent.move_down()
		res = self.check_next_pos(cubeCurrent)
		direction = "left"
		if (res[0] == 0):
			direction = "right"
		cubeCurrent.move_back_counter()
		return (direction)

	def 	check_corner(self, cubeCurrent):
		count = 0
		if self.finishedThreeColorPosition(cubeCurrent, ["yellow", "green", "red"]) is True:
			count += 1
		if self.finishedThreeColorPosition(cubeCurrent, ["yellow", "blue", "orange"]) is True:
			count += 1
		if self.finishedThreeColorPosition(cubeCurrent, ["yellow", "red", "blue"]) is True:
			count += 1
		if self.finishedThreeColorPosition(cubeCurrent, ["yellow", "orange", "green"]) is True:
			count += 1
		return (count)

	def 	updatePositionList(self, cub, colors):
		return (self.checkerManager.three(cub, colors[0], colors[1], colors[2]))

	def 	check_next_pos(self, cubeCurrent):
		count = 0
		correct_corner = []
		self.lst_pos_curr = self.updatePositionList(cubeCurrent, ["yellow", "green", "red"])
		if self.check_side(cubeCurrent, "front") is True:
			count += 1
			correct_corner = ["yellow", "green", "red"]
		self.lst_pos_curr = self.updatePositionList(cubeCurrent, ["yellow", "blue", "red"])
		if self.check_side(cubeCurrent, "right") is True:
			count += 1
			correct_corner = ["yellow", "blue", "red"]
		self.lst_pos_curr = self.updatePositionList(cubeCurrent, ["yellow", "blue", "orange"])
		if self.check_side(cubeCurrent, "back") is True: 
			count += 1
			correct_corner = ["yellow", "blue", "orange"]
		self.lst_pos_curr = self.updatePositionList(cubeCurrent, ["yellow", "green", "orange"])
		if self.check_side(cubeCurrent, "left") is True:
			count += 1
			correct_corner = ["yellow", "green", "orange"]
		return (count, correct_corner)

	def finishedThreeColorPosition(self, cubeCurrent, colorsList):
		return checkPositionColor(self.cubeOrigin, cubeCurrent, colorsList[0], colorsList[1], colorsList[2])

	def 	check_side(self, cubeCurrent, face):
		if face == "front":
			return (self.checkDoubleSide(face, "right"))
		elif face == "right":
			return (self.checkDoubleSide(face, "back"))
		elif face == "back":
			return (self.checkDoubleSide(face, "left"))
		elif face == "left":
			return (self.checkDoubleSide(face, "front"))
		return False

	def 	checkDoubleSide(self, face, subFace):
		count = 0
		i = 0
		while i < len(self.lst_pos_curr):
			if ((self.lst_pos_curr[i][0]) == face) or ((self.lst_pos_curr[i][0]) == subFace):
				count += 1
			i += 1
		return (count == 2)

	def 	move_to_next_pos(self, cubeCurrent, lst_moves, listMix):
		mixManager = mix.Mix()
		mixManager.runMix(listMix, cubeCurrent)
		self.lst_moves = utils.append_list(lst_moves, listMix)
