import sys
sys.path.insert(0, "../SecondaryFunctions")
import check_colors as check_c
import cubik
import mix

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
                cubeCurrent.move_left_counter()
                lst_moves.append("L'")
            if face == "back":
                cubeCurrent.move_back_counter()
                lst_moves.append("B'")
            self.lst_pos_curr = self.checker.two(cubeCurrent, color_one, color_two)

    def update_face_color(self, cubeCurrent, color_one, color_two):
        self.lst_pos_curr = self.checker.two(cubeCurrent, color_one, color_two)
        return self.lst_pos_curr[0][0], self.lst_pos_curr[1][0]

    def move_down_two_color(self, cubeCurrent, lst_moves, color_one, color_two, face):
        face_one, face_two = self.update_face_color(cubeCurrent, color_one, color_two)

        def move_down_center(cubeCurrent, lst_moves, color_one, color_two, face):
            face_one, face_two = self.update_face_color(cubeCurrent, color_one, color_two)
            while 1:
                if face_one == face or face_two = face:
                    cubeCurrent.move_down()
                    lst_moves.append("D")
                    face_one, face_two = self.update_face_color(cubeCurrent, color_one, color_two)
        
        def optimization_step(count, lst_moves, move):
            if count == 3:
                count = 1
                lst_moves.append(move + "'")
                return count, 1
            else:
                x = 0
                while x != count:
                    x += 1
                    lst_moves.append(move)
                return count, 0

        count = 0
        if (face_one == "front" or face_two == "front"):
            while (1):
                if (face_one == "down" or face_two == "down"):
                    break
                count += 1
                cubeCurrent.move_front()
                face_one,face_two = self.updateFaceColor(cubeCurrent, color_one, color_two)
            count, flag = optimizationStep(count, lst_moves, "F")
            moveDownCenter(cubeCurrent, lst_moves, color_one, color_two, face)
            while (count != 0):
                count -= 1
                if (flag == 0):
                    cubeCurrent.move_front_counter()
                    lst_moves.append("F'")
                else:
                    cubeCurrent.move_front()
                    lst_moves.append("F")
        elif (face_one == "left" or face_two == "left"):
            while (1):
                if (face_one == "down" or face_two == "down"):
                    break
                count += 1
                cubeCurrent.move_left()
                face_one,face_two = self.updateFaceColor(cubeCurrent, color_one, color_two)
            count,flag = optimizationStep(count, lst_moves, "L")
            moveDownCenter(cubeCurrent, lst_moves, color_one, color_two, face)
            while (count != 0):
                count -= 1
                if (flag == 0):
                    cubeCurrent.moveBackL()
                    lst_moves.append("L'")
                else:
                    cubeCurrent.move_left()
                    lst_moves.append("L")
        elif (face_one == "right" or face_two == "right"):
            while (1):
                if (face_one == "down" or face_two == "down"):
                    break
                count += 1
                cubeCurrent.move_right()
                face_one,face_two = self.updateFaceColor(cubeCurrent, color_one, color_two)
            count,flag = optimizationStep(count, lst_moves, "R")
            moveDownCenter(cubeCurrent, lst_moves, color_one, color_two, face)
            while (count != 0):
                count -= 1
                if (flag == 0):
                    cubeCurrent.move_right_counter()
                    lst_moves.append("R'")
                else:
                    cubeCurrent.move_right()
                    lst_moves.append("R")
        elif (face_one == "back" or face_two == "back"):
            while (1):
                if (face_one == "down" or face_two == "down"):
                    break
                count += 1
                cubeCurrent.move_back_counter()
                face_one,face_two = self.updateFaceColor(cubeCurrent, color_one, color_two)
            count,flag = optimizationStep(count, lst_moves, "B")
            moveDownCenter(cubeCurrent, lst_moves, color_one, color_two, face)
            while (count != 0):
                count -= 1
                if (flag == 0):
                    cubeCurrent.move_back_counter()
                    lst_moves.append("B'")
                else:
                    cubeCurrent.move_back()
                    lst_moves.append("B")

    def    changeSide(cubeCurrent, lst_moves, face):
        mixManager = mix.Mix()
        if (face == "front"):
            mixManager.mixRun(["F", "U'", "R", "U"], cubeCurrent)
            lst_moves = utils.append_list(lst_moves, ["F", "U'", "R", "U"])
        elif (face == "right"):
            mixManager.mixRun(["R", "U'", "B", "U"], cubeCurrent)
            lst_moves = utils.append_list(lst_moves, ["R", "U'", "B", "U"])
        elif (face == "left"):
            mixManager.mixRun(["L", "U'", "F", "U"], cubeCurrent)
            lst_moves = utils.append_list(lst_moves, ["L", "U'", "F", "U"])
        elif (face == "back"):
            mixManager.mixRun(["B", "U'", "L", "U"], cubeCurrent)
            lst_moves = utils.append_list(lst_moves, ["B", "U'", "L", "U"])
