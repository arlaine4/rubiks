import sys
sys.path.insert(0, "../../SecondaryFunctions")
sys.path.insert(0, "../../../rubiks")
import SecondaryFunctions.check_colors as check_c
import cubik
from SecondaryFunctions import mix
from SecondaryFunctions import utils

class   step_one():
    """First step : do the white cross"""
    def __init__(self, cubeOrigin):
        self.cubeOrigin = cubeOrigin
        self.lst_pos_curr = []
        self.lst_pos_origin = []
        self.checker = check_c.CheckerColors()
        self.lst_moves = []

    def set_lst_moves(self, lst_moves):
        """lst_moves setteur"""
        self.lst_moves = lst_moves

    def run(self, cubeCurrent, lst_moves):
        self.set_lst_moves(lst_moves)
        if self.finished_two_color_pos(cubeCurrent, "white", "green") is False:
            self.edge_move_two_color(cubeCurrent, "white", "green", "front")
        if self.finished_two_color_pos(cubeCurrent, "white", "blue") is False:
            self.edge_move_two_color(cubeCurrent, "white", "blue", "back")
        if self.finished_two_color_pos(cubeCurrent, "white", "red") is False:
            self.edge_move_two_color(cubeCurrent, "white", "red", "right")
        if self.finished_two_color_pos(cubeCurrent, "white", "orange") is False:
            self.edge_move_two_color(cubeCurrent, "white", "orange", "left")
        return self.lst_moves

    def finished_two_color_pos(self, cubeCurrent, color_one, color_two):
        """check if the two cubies, current and adjacent one are correct"""
        return cubik.check_pos_color(self.cubeOrigin, cubeCurrent, color_one, color_two)

    def edge_move_two_color(self, cubeCurrent, color_one, color_two, face):
        """move the edge corresponding to the cubie with color_one and color_two"""
        self.lst_pos_curr = self.checker.two(cubeCurrent, color_one, color_two)
        self.lst_pos_origin = self.checker.two(self.cubeOrigin, color_one, color_two)
        if ((face != self.lst_pos_curr[0][0]) and (face != self.lst_pos_curr[1][0])):
            self.move_down_two_color(cubeCurrent, color_one, color_two, face)
        if (face == self.lst_pos_curr[0][0]) or (face == self.lst_pos_curr[1][0]):
            self.move_center(cubeCurrent, face, color_one, color_two)
            if self.lst_pos_curr[0][1] != self.lst_pos_origin[0][1]:
                self.change_side(cubeCurrent, face)

    def move_center(self, cubeCurrent, face, color_one, color_two):
        """move edges from UF (up front) || UL (up left) || UR (up right) || UB (up back) to
        the up face"""
        while self.lst_pos_curr[1][2] != self.lst_pos_origin[1][2]:
            if face == "front":
                cubeCurrent.move_front_counter()
                self.lst_moves.append("F'")
            if face == "right":
                cubeCurrent.move_right_counter()
                self.lst_moves.append("R'")
            if face == "left":
                cubeCurrent.move_left_counter()
                self.lst_moves.append("L'")
            if face == "back":
                cubeCurrent.move_back_counter()
                self.lst_moves.append("B'")
            self.lst_pos_curr = self.checker.two(cubeCurrent, color_one, color_two)

    def update_face_color(self, cubeCurrent, color_one, color_two):
        """refresh current positions"""
        self.lst_pos_curr = self.checker.two(cubeCurrent, color_one, color_two)
        return self.lst_pos_curr[0][0], self.lst_pos_curr[1][0]

    def move_down_two_color(self, cubeCurrent, color_one, color_two, face):
        face_one, face_two = self.update_face_color(cubeCurrent, color_one, color_two)

        def move_down_center(cubeCurrent, color_one, color_two, face):
            """move middle edges on down face"""
            face_one, face_two = self.update_face_color(cubeCurrent, color_one, color_two)
            while 1:
                if face_one == face or face_two == face:
                    break
                cubeCurrent.move_down()
                self.lst_moves.append("D")
                face_one, face_two = self.update_face_color(cubeCurrent, color_one, color_two)
        
        def optimization_step(count, move):
            """Optimizating moves"""
            if count == 3:
                #If 3 moves of one kind have been made, we replace it with a counter clockwise
                # ex: D D D -> D'
                count = 1
                self.lst_moves.append(move + "'")
                return count, 1
            else:
                x = 0
                while x != count:
                    x += 1
                    self.lst_moves.append(move)
                return count, 0

        """Finishing step one"""
        count = 0
        if face_one == "front" or face_two == "front":
            while 1:
                if face_one == "down" or face_two == "down":
                    break
                count += 1
                cubeCurrent.move_front()
                face_one, face_two = self.update_face_color(cubeCurrent, color_one, color_two)
            count, flag = optimization_step(count, "F")
            move_down_center(cubeCurrent, color_one, color_two, face)
            while count != 0:
                count -= 1
                if flag == 0:
                    cubeCurrent.move_front_counter()
                    self.lst_moves.append("F'")
                else:
                    cubeCurrent.move_front()
                    self.lst_moves.append("F")
        elif face_one == "left" or face_two == "left":
            while 1:
                if face_one == "down" or face_two == "down":
                    break
                count += 1
                cubeCurrent.move_left()
                face_one,face_two = self.update_face_color(cubeCurrent, color_one, color_two)
            count,flag = optimization_step(count, "L")
            move_down_center(cubeCurrent, color_one, color_two, face)
            while count != 0:
                count -= 1
                if flag == 0:
                    cubeCurrent.move_left_counter()
                    self.lst_moves.append("L'")
                else:
                    cubeCurrent.move_left()
                    self.lst_moves.append("L")
        elif face_one == "right" or face_two == "right":
            while 1:
                if face_one == "down" or face_two == "down":
                    break
                count += 1
                cubeCurrent.move_right()
                face_one,face_two = self.update_face_color(cubeCurrent, color_one, color_two)
            count,flag = optimization_step(count, "R")
            move_down_center(cubeCurrent, color_one, color_two, face)
            while count != 0:
                count -= 1
                if flag == 0:
                    cubeCurrent.move_right_counter()
                    self.lst_moves.append("R'")
                else:
                    cubeCurrent.move_right()
                    self.lst_moves.append("R")
        elif face_one == "back" or face_two == "back":
            while 1:
                if face_one == "down" or face_two == "down":
                    break
                count += 1
                cubeCurrent.move_back_counter()
                face_one,face_two = self.updateFaceColor(cubeCurrent, color_one, color_two)
            count,flag = optimization_step(count, "B")
            move_down_center(cubeCurrent, color_one, color_two, face)
            while count != 0:
                count -= 1
                if (flag == 0):
                    cubeCurrent.move_back_counter()
                    self.lst_moves.append("B'")
                else:
                    cubeCurrent.move_back()
                    self.lst_moves.append("B")

    def    change_side(self, cubeCurrent, face):
        """Re positionning edges"""
        mixManager = mix.Mix()
        if face == "front":
            mixManager.runMix(["F", "U'", "R", "U"], cubeCurrent)
            self.lst_moves = utils.append_list(self.lst_moves, ["F", "U'", "R", "U"])
        elif face == "right":
            mixManager.runMix(["R", "U'", "B", "U"], cubeCurrent)
            self.lst_moves = utils.append_list(self.lst_moves, ["R", "U'", "B", "U"])
        elif face == "left":
            mixManager.runMix(["L", "U'", "F", "U"], cubeCurrent)
            self.lst_moves = utils.append_list(self.lst_moves, ["L", "U'", "F", "U"])
        elif face == "back":
            mixManager.runMix(["B", "U'", "L", "U"], cubeCurrent)
            self.lst_moves = utils.append_list(self.lst_moves, ["B", "U'", "L", "U"])
