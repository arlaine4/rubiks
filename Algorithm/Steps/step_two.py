import sys
sys.path.insert(0, "../SecondaryFunctions")
from SecondaryFunctions import check_colors as check_c
import cubik
from SecondaryFunctions import mix, utils

class   step_two:
    def __init__(self, cubOrigin):
        self.cubOrigin = cubOrigin
        self.lst_pos_cur = []
        self.lst_pos_origin = []
        self.checker = check_c.CheckerColors()
        self.lst_moves = []

    def set_lst_moves(self, lst_moves):
        self.lst_moves = lst_moves

    def run(self, cubeCurrent, lst_moves):
        self.set_lst_moves(lst_moves)
        if self.finished_three_color_pos(cubeCurrent, "white", "green", "red") is False:
            cubeCurrent.print_cube()
            self.move_three_color(cubeCurrent, "white", "green", "red", "front")
            cubeCurrent.print_cube()
        if self.finished_three_color_pos(cubeCurrent, "white", "red", "blue") is False:
            cubeCurrent.print_cube()
            self.move_three_color(cubeCurrent, "white", "red", "blue", "right")
            cubeCurrent.print_cube()
        if self.finished_three_color_pos(cubeCurrent, "white", "blue", "orange") is False:
            cubeCurrent.print_cube()
            self.move_three_color(cubeCurrent, "white", "blue", "orange", "back")
            cubeCurrent.print_cube()
        if self.finished_three_color_pos(cubeCurrent, "white", "orange", "green") is False:
            cubeCurrent.print_cube()
            self.move_three_color(cubeCurrent, "white", "orange", "green", "left")
            cubeCurrent.print_cube()
        return self.lst_moves

    def finished_three_color_pos(self, cubeCurrent, color_one, color_two, color_three):
        return cubik.check_pos_color(self.cubOrigin, cubeCurrent, color_one, color_two, color_three)

    def update_pos_lst(self, cub, color_one, color_two, color_three):
        return self.checker.three(cub, color_one, color_two, color_three)

    def move_three_color(self, cubeCurrent, color_one, color_two, color_three, face):
        self.lst_pos_cur = self.update_pos_lst(cubeCurrent, color_one, color_two, color_three)
        self.lst_pos_origin = self.update_pos_lst(self.cubOrigin, color_one, color_two, color_three)
        if self.check_side(cubeCurrent, face) is False:
            if self.lst_pos_cur[0][0] == "up":
                self.move_edge_down(cubeCurrent, color_one, color_two, color_three)
            if self.lst_pos_cur[0][0] == "down":
                self.move_edge_down_loop(cubeCurrent, color_one, color_two, color_three, face)
        self.lst_pos_cur = self.update_pos_lst(cubeCurrent, color_one, color_two, color_three)
        if self.check_side(cubeCurrent, face) is True:
            self.move_side(cubeCurrent, color_one, color_two, color_three, face)

    def move_edge_down(self, cubeCurrent, color_one, color_two, color_three):
        self.lst_pos_cur = self.update_pos_lst(cubeCurrent, color_one, color_two, color_three)
        mixManager = mix.Mix()
        if self.lst_pos_cur[1][0] == "right" and self.lst_pos_cur[2][0] == "front":
            mixManager.runMix(["F", "D'", "F'"], cubeCurrent)
            self.lst_moves = utils.append_list(self.lst_moves, ["F", "D'", "F'"])
        elif self.lst_pos_cur[1][0] == "left" and self.lst_pos_cur[2][0] == "front":
            mixManager.runMix(["F'", "D", "F"], cubeCurrent)
            self.lst_moves = utils.append_list(self.lst_moves, ["F'", "D", "F"])
        elif self.lst_pos_cur[1][0] == "right" and self.lst_pos_cur[2][0] == "back":
            mixManager.runMix(["B'", "D", "B"], cubeCurrent)
            self.lst_moves = utils.append_list(self.lst_moves, ["B'", "D", "B"])
        elif self.lst_pos_cur[1][0] == "left" and self.lst_pos_cur[2][0] == "back":
            mixManager.runMix(["B", "D'", "B'"], cubeCurrent)
            self.lst_moves = utils.append_list(self.lst_moves, ["B", "D'", "B'"])
        self.lst_pos_cur = self.update_pos_lst(cubeCurrent, color_one, color_two, color_three)

    def move_edge_down_loop(self, cubeCurrent, color_one, color_two, color_three, face):
        while self.check_side(cubeCurrent, face) is False:
            cubeCurrent.move_down()
            self.lst_moves.append("D")
            self.lst_pos_cur = self.update_pos_lst(cubeCurrent, color_one, color_two, color_three)

    def check_side(self, cubeCurrent, face):
        if face == "front":
            return self.check_both_side(face, "right")
        elif face == "right":
            return self.check_both_side(face, "back")
        elif face == "back":
            return self.check_both_side(face, "left")
        elif face == "left":
            return self.check_both_side(face, "front")
        else:
            return False

    def check_both_side(self, face, adj_face):
        count = 0
        i = 0
        while i < len(self.lst_pos_cur):
            if (self.lst_pos_cur[i][0] == face) or (self.lst_pos_cur[i][0] == adj_face):
                count += 1
            i += 1
        return True if count == 2 else False

    def move_side(self, cubeCurrent, color_one, color_two, color_three, face):
        mixManager = mix.Mix()
        while self.finished_three_color_pos(cubeCurrent, color_one, color_two, color_three) is False:
            if face == "front":
                mixManager.runMix(["R'", "D'", "R", "D"], cubeCurrent)
                self.lst_moves = utils.append_list(self.lst_moves, ["R'", "D'", "R", "D"])
            elif face == "right":
                mixManager.runMix(["B'", "D'", "B", "D"], cubeCurrent)
                self.lst_moves = utils.append_list(self.lst_moves, ["B'", "D'", "B", "D"])
            elif face == "back":
                mixManager.runMix(["L'", "D'", "L", "D"], cubeCurrent)
                self.lst_moves = utils.append_list(self.lst_moves, ["L'", "D'", "L", "D"])
            elif face == "left":
                mixManager.runMix(["F'", "D'", "F", "D"], cubeCurrent)
                self.lst_moves = utils.append_list(self.lst_moves, ["F'", "D'", "F", "D"])
