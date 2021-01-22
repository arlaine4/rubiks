import sys
sys.path.insert(0, "../../SecondaryFunctions")
sys.path.insert(0, "../../../rubiks")
import SecondaryFunctions.check_colors as check_c
import cubik
from SecondaryFunctions import mix
from SecondaryFunctions import utils


class step_three:
    """second layer placement (Up and middle layers for F L R B)"""
    def __init__(self, cubeOrigin):
        self.cubeOrigin = cubeOrigin
        self.lst_pos_curr = []
        self.lst_pos_origin = []
        self.checker = check_c.CheckerColors()
        self.lst_moves = []

    def set_lst_moves(self, lst_moves):
        self.lst_moves = lst_moves

    def run(self, cubeCurrent, lst_moves):
        self.set_lst_moves(lst_moves)
        if self.finished_three_color_pos(cubeCurrent, ["green", "orange"]) is False:
                self.moving(cubeCurrent, ["green", "orange"], "front")
        if self.finished_three_color_pos(cubeCurrent, ["orange", "blue"]) is False:
                self.moving(cubeCurrent, ["orange", "blue"], "left")
        if self.finished_three_color_pos(cubeCurrent, ["blue", "red"]) is False:
                self.moving(cubeCurrent, ["blue", "red"], "back")
        if self.finished_three_color_pos(cubeCurrent, ["red", "green"]) is False:
                self.moving(cubeCurrent, ["red", "green"], "right")

    def finished_three_color_pos(self, cubeCurrent, lst_colors):
        return cubik.check_pos_color(self.cubeOrigin, cubeCurrent, lst_colors[0], lst_colors[1])

    def update_pos_lst(self, cub, lst_colors):
        return self.checker.two(cub, lst_colors[0], lst_colors[1])

    def moving(self, cubeCurrent, lst_colors, face):
        self.lst_pos_origin = self.update_pos_lst(self.cubeOrigin, lst_colors)
        self.lst_pos_curr = self.update_pos_lst(cubeCurrent, lst_colors)
        check_side_lst = self.check_side(cubeCurrent, lst_colors)
        if check_side_lst[0] is True:
            self.wich_sequences(cubeCurrent, lst_colors)
        else:
            if self.lst_pos_curr[0][0] != "down":
                self.push_down(cubeCurrent, lst_colors)
                self.lst_pos_curr = self.update_pos_lst(cubeCurrent, lst_colors)
            if self.lst_pos_curr[0][0] != "down":
                print ("An error has occured, sorry guys")
                sys.exit(-1)
            self.lst_pos_curr = self.update_pos_lst(cubeCurrent, lst_colors)
            if self.lst_pos_curr[0][0] == "down":
                self.move_to_center(cubeCurrent, lst_colors, face)
                self.lst_pos_curr = self.update_pos_lst(cubeCurrent, lst_colors)
                self.wich_sequences(cubeCurrent, lst_colors)

    def move_to_center(self, cubeCurrent, lst_colors, face):
        """Orienting edge on down face"""
        check_side_lst = self.check_side(cubeCurrent, lst_colors)
        while check_side_lst[0] is False:
            cubeCurrent.move_down()
            self.lst_moves.append("D")
            check_side_lst = self.check_side(cubeCurrent, lst_colors)

    def push_down(self, cubeCurrent, lst_colors):
        face_one, face_two, colorOne, colorTwo = self.get_side_params(cubeCurrent, lst_colors)
        pattern = self.get_pattern_push_down(face_one, face_two)
        if pattern == "rightPattern":
            self.right_sequence(cubeCurrent, face_one)
        elif pattern == "leftPattern":
            self.left_sequence(cubeCurrent, face_one)

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

    def get_side_params(self, cubeCurrent, lst_colors):
        self.lst_pos_curr = self.update_pos_lst(cubeCurrent, lst_colors)
        down = self.lst_pos_curr[0][0]
        colorDown = self.lst_pos_curr[0][1]
        colorFace = self.lst_pos_curr[1][1]
        face = self.lst_pos_curr[1][0]
        return down, face, colorDown, colorFace

    def check_side(self, cubeCurrent, lst_colors):
        down, face, colorDown, colorFace = self.get_side_params(cubeCurrent, lst_colors)
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

    def wich_sequences(self, cubeCurrent, lst_colors):
        down, face, colorDown, colorFace = self.get_side_params(cubeCurrent, lst_colors)
        check_side_lst = self.check_side(cubeCurrent, lst_colors)
        if check_side_lst[1] == "rightPattern":
            self.right_sequence(cubeCurrent, face)
        elif check_side_lst[1] == "leftPattern":
            self.left_sequence(cubeCurrent, face)

    def left_sequence(self, cubeCurrent, face):
        mixManager = mix.Mix()

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

    def right_sequence(self, cubeCurrent, face):
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
