import sys
sys.path.insert(0, "../../SecondaryFunctions")
sys.path.insert(0, "../../../rubiks")
import SecondaryFunctions.check_colors as check_c
import cubik
from SecondaryFunctions import mix
from SecondaryFunctions import utils

class step_six:
    """step six : yellow corners orientation"""
    def __init__(self, cubeOrigin):
        self.cubeOrigin = cubeOrigin
        self.lst_pos_curr = []
        self.checker = check_c.CheckerColors()
        self.lst_moves = []

    def set_lst_moves(self, lst_moves):
        self.lst_moves = lst_moves

    def run(self, cubeCurrent, lst_moves):
        self.set_lst_moves(lst_moves)
        res = self.check_corner(cubeCurrent)
        if res == 4:
            return self.lst_moves
        else:
            res = self.check_next_pos(cubeCurrent)
            if res[0] == 4:
                return self.lst_moves
            else:
                if res[0] == 0:
                    self.move_to_next_pos(cubeCurrent, ["D", "L", "D'", "R'", "D", "L'", "D'", "R"])
                res = self.check_next_pos(cubeCurrent)
                lst_colors = res[1]
                lst_pattern = self.get_pattern(cubeCurrent, lst_colors)
                self.move_fown_face(cubeCurrent, lst_pattern)
        return self.lst_moves

    def move_fown_face(self, cubeCurrent, lst_pattern):
        face = lst_pattern[1]
        if face == "frontFace":
            if lst_pattern[0] == "right":
                self.move_to_next_pos(cubeCurrent, ["D", "L", "D'", "R'", "D", "L'", "D'", "R"])
            else:
                self.move_to_next_pos(cubeCurrent, ["D'", "R'", "D", "L", "D'", "R", "D", "L'"])
        elif face == "backFace":
            if lst_pattern[0] == "right":
                self.move_to_next_pos(cubeCurrent, ["D", "R", "D'", "L'", "D", "R'", "D'", "L"])
            else:
                self.move_to_next_pos(cubeCurrent, ["D'", "L'", "D", "R", "D'", "L", "D", "R'"])
        elif face == "rightFace":
            if lst_pattern[0] == "right":
                self.move_to_next_pos(cubeCurrent, ["D", "F", "D'", "B'", "D", "F'", "D'", "B"])
            else:
                self.move_to_next_pos(cubeCurrent, ["D'", "B'", "D", "F", "D'", "B", "D", "F'"])
        elif face == "leftFace":
            if lst_pattern[0] == "right":
                self.move_to_next_pos(cubeCurrent, ["D", "B", "D'", "F'", "D", "B'", "D'", "F"])
            else:
                self.move_to_next_pos(cubeCurrent, ["D'", "F'", "D", "B", "D'", "F", "D", "B'"])

    def get_pattern(self, cubeCurrent, lst_colors):
        lst_pattern = []
        if ["yellow", "green", "red"] == lst_colors:
            lst_pattern.append(self.get_direction(cubeCurrent))
            if lst_pattern[0] == "left":
                lst_pattern.append("frontFace")
            else:
                lst_pattern.append("rightFace")
        elif ["yellow", "blue", "orange"] == lst_colors:
            lst_pattern.append(self.get_direction(cubeCurrent))
            if lst_pattern[0] == "left":
                lst_pattern.append("backFace")
            else:
                lst_pattern.append("leftFace")
        elif ["yellow", "blue", "red"] == lst_colors:
            lst_pattern.append(self.get_direction(cubeCurrent))
            if lst_pattern[0] == "left":
                lst_pattern.append("rightFace")
            else:
                lst_pattern.append("backFace")
        elif ["yellow", "green", "orange"] == lst_colors:
            lst_pattern.append(self.get_direction(cubeCurrent))
            if lst_pattern[0] == "left":
                lst_pattern.append("leftFace")
            else:
                lst_pattern.append("frontFace")
        return lst_pattern

    def get_direction(self, cubeCurrent):
        cubeCurrent.move_down()
        res = self.check_next_pos(cubeCurrent)
        direction = "left"
        if res[0] == 0:
            direction = "right"
        cubeCurrent.move_down_counter()
        return direction

    def check_corner(self, cubeCurrent):
        count = 0
        if self.finishedThreeColorPosition(cubeCurrent, ["yellow", "green", "red"]) is True:
            count += 1
        if self.finishedThreeColorPosition(cubeCurrent, ["yellow", "blue", "orange"]) is True:
            count += 1
        if self.finishedThreeColorPosition(cubeCurrent, ["yellow", "red", "blue"]) is True:
            count += 1
        if self.finishedThreeColorPosition(cubeCurrent, ["yellow", "orange", "green"]) is True:
            count += 1
        return count

    def updatePositionList(self, cub, colors):
        return self.checker.three(cub, colors[0], colors[1], colors[2])

    def check_next_pos(self, cubeCurrent):
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
        return count, correct_corner

    def finishedThreeColorPosition(self, cubeCurrent, lst_colors):
        return cubik.check_pos_color(self.cubeOrigin, cubeCurrent, lst_colors[0], lst_colors[1], lst_colors[2])

    def check_side(self, cubeCurrent, face):
        if face == "front":
            return self.checkDoubleSide(face, "right")
        elif face == "right":
            return self.checkDoubleSide(face, "back")
        elif face == "back":
            return self.checkDoubleSide(face, "left")
        elif face == "left":
            return self.checkDoubleSide(face, "front")
        return False

    def checkDoubleSide(self, face, subFace):
        count = 0
        i = 0
        while i < len(self.lst_pos_curr):
            if (self.lst_pos_curr[i][0] == face) or (self.lst_pos_curr[i][0] == subFace):
                count += 1
            i += 1
        return True if count == 2 else False

    def move_to_next_pos(self, cubeCurrent, list_mix):
        mixManager = mix.Mix()
        mixManager.runMix(list_mix, cubeCurrent)
        self.lst_moves = utils.append_list(self.lst_moves, list_mix)
