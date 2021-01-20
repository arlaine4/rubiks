import sys
sys.path.insert(0, "../../SecondaryFunctions")
sys.path.insert(0, "../../../rubiks")
import SecondaryFunctions.check_colors as check_c
import cubik
from SecondaryFunctions import mix
from SecondaryFunctions import utils

class step_five:
    def __init__(self, cubeOrigin):
        self.cubeOrigin = cubeOrigin
        self.checkerManager = check_c.CheckerColors()

    def run(self, cubeCurrent, lst_moves):
        res = self.go_down(cubeCurrent, lst_moves)
        if res == 4:
            return True
        elif res == 2:
            self.move_to_face(cubeCurrent, lst_moves)

    def go_down(self, cubeCurrent, lst_moves):
        count = 0
        while (count < 2):
            if self.finished_two_color_pos(cubeCurrent, ["yellow", "green"]) is True:
                count += 1
            if self.finished_two_color_pos(cubeCurrent, ["yellow", "blue"]) is True:
                count += 1
            if self.finished_two_color_pos(cubeCurrent, ["yellow", "red"]) is True:
                count += 1
            if self.finished_two_color_pos(cubeCurrent, ["yellow", "orange"]) is True:
                count += 1
            if count == 4:
                return 4
            if count < 2:
                count = 0
                cubeCurrent.move_down()
                lst_moves.append("D")
        return 2

    def finished_two_color_pos(self, cubeCurrent, colorsList):
        return cubik.check_pos_color(self.cubeOrigin, cubeCurrent, colorsList[0], colorsList[1])

    def move_to_face(self, cubeCurrent, lst_moves):
        res = 2
        if self.finished_two_color_pos(cubeCurrent, ["yellow", "green"]) is True:
            if self.finished_two_color_pos(cubeCurrent, ["yellow", "blue"]) is True:
                res = self.move_opposite(cubeCurrent, lst_moves, "right")
        if self.finished_two_color_pos(cubeCurrent, ["yellow", "red"]) is True:
            if self.finished_two_color_pos(cubeCurrent, ["yellow", "orange"]) is True:
                res = self.move_opposite(cubeCurrent, lst_moves, "front")
        if res == 2:
            self.corner_change(cubeCurrent, lst_moves, self.get_missplaced_corners(cubeCurrent))

    def move_opposite(self, cubeCurrent, lst_moves, face):
        mixManager = mix.Mix()
        if face == "front":
            mixManager.runMix(["L", "D", "L'", "D", "L", "D2", "L'"], cubeCurrent)
            self.lst_moves = utils.append_list(lst_moves, ["L", "D", "L'", "D", "L", "D2", "L'"])
        if face == "right":
            mixManager.runMix(["F", "D", "F'", "D", "F", "D2", "F'"], cubeCurrent)
            self.lst_moves = utils.append_list(lst_moves, ["F", "D", "F'", "D", "F", "D2", "F'"])
        return self.go_down(cubeCurrent, lst_moves)

    def get_missplaced_corners(self, cubeCurrent):
        isFalseBlue = self.finished_two_color_pos(cubeCurrent, ["yellow", "blue"])
        isFalseGreen = self.finished_two_color_pos(cubeCurrent, ["yellow", "green"])
        isFalseRed = self.finished_two_color_pos(cubeCurrent, ["yellow", "red"])
        isFalseOrange = self.finished_two_color_pos(cubeCurrent, ["yellow", "orange"])
        if isFalseBlue == True and isFalseOrange == True:
            return ("front")
        elif isFalseGreen == True and isFalseOrange == True:
            return ("right")
        elif isFalseGreen == True and isFalseRed == True:
            return ("back")
        elif isFalseRed  == True and isFalseBlue == True:
            return ("left")

    def corner_change(self, cubeCurrent, lst_moves, face):
        mixManager = mix.Mix()
        if face == "front":
            mixManager.runMix(["L", "D", "L'", "D", "L", "D2", "L'", "D"], cubeCurrent)
            self.lst_moves = utils.append_list(lst_moves, ["L", "D", "L'", "D", "L", "D2", "L'", "D"])
        elif face == "back":
            mixManager.runMix(["R", "D", "R'", "D", "R", "D2", "R'", "D"], cubeCurrent)
            self.lst_moves = utils.append_list(lst_moves, ["R", "D", "R'", "D", "R", "D2", "R'", "D"])
        elif face == "right":
            mixManager.runMix(["F", "D", "F'", "D", "F", "D2", "F'", "D"], cubeCurrent)
            self.lst_moves = utils.append_list(lst_moves, ["F", "D", "F'", "D", "F", "D2", "F'", "D"])
        elif face == "left":
            mixManager.runMix(["B", "D", "B'", "D", "B", "D2", "B'", "D"], cubeCurrent)
            self.lst_moves = utils.append_list(lst_moves, ["B", "D", "B'", "D", "B", "D2", "B'", "D"])
