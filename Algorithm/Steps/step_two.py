import sys
sys.path.insert(0, "../SecondaryFunctions")
from SecondaryFunctions import check_colors as check_c
import cubik
from SecondaryFunctions import mix

class   step_two:
	
	def __init__(self, cubOrigin):
		self.cubOrigin = cubOrigin
		self.lst_pos_cur = []
		self.lst_pos_origin = []
		self.checker = check_c.CheckerColors()

	def 	run(self, cubeCurrent, lst_moves):
		if ((self.finished_three_color_pos(cubeCurrent, "white", "green", "red")) is False):
			self.move_three_color(cubeCurrent, lst_moves, "white", "green", "red", "front")
		if ((self.finished_three_color_pos(cubeCurrent, "white", "red", "blue")) is False):
			self.move_three_color(cubeCurrent, lst_moves, "white", "red", "blue", "right")
		if ((self.finished_three_color_pos(cubeCurrent, "white", "blue", "orange")) is False):
			self.move_three_color(cubeCurrent, lst_moves, "white", "blue", "orange", "back")
		if ((self.finished_three_color_pos(cubeCurrent, "white", "orange", "green")) is False):
			self.move_three_color(cubeCurrent, lst_moves, "white", "orange", "green", "left")

	def finished_three_color_pos(self, cubeCurrent, color_one, color_two, color_three):
		return cubik.check_pos_color(self.cubOrigin, cubeCurrent, color_one, color_two, color_three)

	def 	update_pos_lst(self, cub, color_one, color_two, color_three):
		return (self.checker.three(cub, color_one, color_two, color_three))

	def 	move_three_color(self, cubeCurrent, lst_moves, color_one, color_two, color_three, face):
		self.lst_pos_cur = self.update_pos_lst(self.cubOrigin, color_one, color_two, color_three)
		self.lst_pos_origin = self.update_pos_lst(cubeCurrent, color_one, color_two, color_three)
		if self.check_side(cubeCurrent, face) is False:	
			if self.lst_pos_origin[0][0] == "upper":			
				self.move_edge_down(cubeCurrent, lst_moves, color_one, color_two, color_three)
			if self.lst_pos_origin[0][0] == "down":
				self.move_edge_down_loop(cubeCurrent, lst_moves, color_one, color_two, color_three, face)
		self.lst_pos_origin = self.update_pos_lst(cubeCurrent, color_one, color_two, color_three)
		if self.check_side(cubeCurrent, face) is True:
			self.move_side(cubeCurrent, lst_moves, color_one, color_two, color_three, face)

	def 	move_edge_down(self, cubeCurrent, lst_moves, color_one, color_two, color_three):
		self.lst_pos_origin = self.update_pos_lst(cubeCurrent, color_one, color_two, color_three)
		mixManager = mix.Mix()
		if self.lst_pos_origin[1][0] == "right" and self.lst_pos_origin[2][0] == "front":
			mixManager.mixRun(["F", "D'", "F'"], cubeCurrent)
			appendListInList(lst_moves, ["F", "D'", "F'"])
		elif self.lst_pos_origin[1][0] == "left" and self.lst_pos_origin[2][0] == "front":
			mixManager.mixRun(["F'", "D", "F"], cubeCurrent)
			appendListInList(lst_moves, ["F'", "D", "F"])
		elif self.lst_pos_origin[1][0] == "right" and self.lst_pos_origin[2][0] == "back":
			mixManager.mixRun(["B'", "D", "B"], cubeCurrent)
			appendListInList(lst_moves, ["B'", "D", "B"])
		elif self.lst_pos_origin[1][0] == "left" and self.lst_pos_origin[2][0] == "back":
			mixManager.mixRun(["B", "D'", "B'"], cubeCurrent)
			appendListInList(lst_moves, ["B", "D'", "B'"])
		self.lst_pos_origin = self.update_pos_lst(cubeCurrent, color_one, color_two, color_three)

	def 	move_edge_down_loop(self, cubeCurrent, lst_moves, color_one, color_two, color_three, face):
		while (self.check_side(cubeCurrent, face)) is False:
			cubeCurrent.moveD()
			lst_moves.append("D")
			self.lst_pos_origin = self.update_pos_lst(cubeCurrent, color_one, color_two, color_three)

	def 	check_side(self, cubeCurrent, face):
		if face == "front":
			return self.check_both_side(face, "right")
		elif face == "right":
			return self.check_both_side(face, "back")
		elif face == "back":
			return self.check_both_side(face, "left")
		elif face == "left":
			return self.check_both_side(face, "front")
		return False

	def 	check_both_side(self, face, adj_face):
		count = 0
		i = 0
		while i < len(self.lst_pos_origin):
			if (self.lst_pos_origin[i][0] == face) or (self.lst_pos_origin[i][0] == adj_face):
				count += 1
			i += 1
		return True if count == 2 else False

	def 	move_side(self, cubeCurrent, lst_moves, color_one, color_two, color_three, face):
		mixManager = MixManager()
		while self.finished_three_color_pos(cubeCurrent, color_one, color_two, color_three) is False:
			if face == "front":
				mixManager.mixRun(["R'", "D'", "R", "D"], cubeCurrent)
				lst_moves = utils.append_list(lst_moves, ["R'", "D'", "R", "D"])
			elif face == "right":
				mixManager.mixRun(["B'", "D'", "B", "D"], cubeCurrent)
				lst_moves = utils.append_list(lst_moves, ["B'", "D'", "B", "D"])
			elif face == "back":
				mixManager.mixRun(["L'", "D'", "L", "D"], cubeCurrent)
				lst_moves = utils.append_list(lst_moves, ["L'", "D'", "L", "D"])
			elif face == "left":
				mixManager.mixRun(["F'", "D'", "F", "D"], cubeCurrent)
				lst_moves = utils.append_list(lst_moves, ["F'", "D'", "F", "D"])
