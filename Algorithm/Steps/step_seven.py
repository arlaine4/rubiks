import sys
sys.path.insert(0, "../../SecondaryFunctions")
sys.path.insert(0, "../../../rubiks")
import SecondaryFunctions.check_colors as check_c
import cubik
from SecondaryFunctions import mix
from SecondaryFunctions import utils

class step_seven:
    def __init__(self, cubeOrigin):
        self.cubeOrigin = cubeOrigin
        self.checker = check_c.CheckerColors()
        self.third_corner = ["yellow", "blue", "red"]
        self.fourth_corner = ["yellow", "red", "green"]
        self.first_corner = ["yellow", "green", "orange"]
        self.second_corner = ["yellow", "blue", "orange"]

    def run(self, cubeCurrent, lst_moves):
        cubeCurrent.mathHash()
        if (self.cubeOrigin.hash == cubeCurrent.hash):
            return True
        self.move_side(cubeCurrent, lst_moves, self.first_corner)
        self.move_down(cubeCurrent, lst_moves)	
        self.move_side(cubeCurrent, lst_moves, self.second_corner)
        self.move_down(cubeCurrent, lst_moves)
        self.move_side(cubeCurrent, lst_moves, self.third_corner)
        self.move_down(cubeCurrent, lst_moves)
        self.move_side(cubeCurrent, lst_moves, self.fourth_corner)
        self.move_down(cubeCurrent, lst_moves)

    def move_down(self, cubeCurrent, lst_moves):
        cubeCurrent.move_down()
        lst_moves.append("D")

    def     move_side(self, cubeCurrent, lst_moves, lst_colors):
        mixManager = MixManager()
        while (self.finished_three_color_pos(cubeCurrent, lst_colors)) == False:
            mixManager.mixRun(["L'", "U'", "L", "U"], cubeCurrent)
            appendListInList(lst_moves, ["L'", "U'", "L", "U"])

    def finished_three_color_pos(self, cubeCurrent, lst_colors):
        lst_pos = self.checkerManager.three(cubeCurrent, lst_colors[0], lst_colors[1], lst_colors[2])
        # lst_pos_origin = self.checkerManager.three(self.cubeOrigin, lst_colors[0], lst_colors[1], lst_colors[2])
        if (lst_pos[0][0] == "down" and lst_pos[0][1] == "yellow"):
            return True
        return False
