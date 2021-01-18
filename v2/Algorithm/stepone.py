import sys
sys.path.insert(0, "../SecondaryFunctions")
import check_colors as check_c
import cubik

class   StepOne():
    def __init__(self, cubeOrigin):
        self.cubeOrigin = cubeOrigin
        self.lst_pos_curr = []
        self.lst_pos_origin = []
        self.checker = check_c.CheckerColors()

    def run(self, cubeCurrent, lst_moves):
        if self.finished_two_color_pos(cubeCurrent, "white", "green") is False:
            self.edge_move_two_color(cubeCurrent, lst_moves, "white", "green", "front")
        if self.finished_two_color_pos(cubeCurrent, "white", "blue") is False:
            self.edge_move_two_color(cubeCurrent, lst_moves, "white", "blue", "back")
        if self.finished_two_color_pos(cubeCurrent, "white", "red") is False:
            self.edge_move_two_color(cubeCurrent, lst_moves, "white", "red", "right")
        if self.finished_two_color_pos(cubeCurrent, "white", "orange") is False:
            self.edge_move_two_color(cubeCurrent, lst_moves, "white", "orange", "left")

    def finished_two_color_pos(self, cubeCurrent, color_one, color_two):
        return check_pos_color(self.cubeOrigin, cubeCurrent, color_one, color_two)

    def edge_move_two_color(self, cubeCurrent, lst_moves, color_one, color_two, face):
        self.lst_pos_curr = self.checker.two(cubeCurrent, color_one, color_two)
        self.lst_pos_origin = self.checker.two(self.cubeOrigin, color_one, color_two)
        if face != self.lst_pos_curr[0][0] and face != self.lst_pos_curr[1][0]:
            self.move_down_two_color(cubeCurrent, lst_moves, color_one, color_two, face)
        if face == self.lst_pos_current[0][0] or face == self.lst_pos_current[1][0]:
            self.moveCenter(cubeCurrent, lst_moves, face, color_one, color_two)
            if self.lst_pos_current[0][1] != lst_pos_origin[0][1]:
                self.change_side(cubeCurrent, lst_moves, face)

    def move_center(self, cubeCurrent, lst_moves, face, color_one, color_two):
        while self.lst_pos_curr[1][2] != self.lst_pos_origin[1][2]:
            if face == "front":
                cubeCurrent.move_back_counter()
                lst_moves.append("F'")
            if face == "right":
                cubeCurrent.move_right_counter()
                lst_moves.append("R'")
            if face == "left":
                cubeCurrebt.move_left_counter()
                lst_moves.append("L'")
            if face == "back":
                cubeCurrent.move_back_counter()
                lst_moves.append("B'")
            self.lst_pos_curr = self.checker.two(cubeCurrent, color_one, color_two)

    def update_face_color(self, cubeCurrent, color_one, color_two):
        self.lst_pos_curr = self.checker.two(cubeCurrent, color_one, color_two)
        return self.lst_pos_curr[0][0], self.lst_pos_curr[1][0]

    def move_down_two_color(self, cubeCurrent, lst_moves, color_one, color_two, face):
        face_one, face_two = self.update_face_color(cubeCurrebt, color_one, color_two)

