import sys
sys.path.insert(0, "../../SecondaryFunctions")
sys.path.insert(0, "../../../rubiks")
import SecondaryFunctions.check_colors as check_c
import cubik
from SecondaryFunctions import mix
from SecondaryFunctions import utils

class step_seven:
    """step seven : place yellow corners and finish the cube"""
    def __init__(self, cubeOrigin):
        self.cubeOrigin = cubeOrigin
        self.checker = check_c.CheckerColors()
        self.third_corner = ["yellow", "blue", "red"]
        self.fourth_corner = ["yellow", "red", "green"]
        self.first_corner = ["yellow", "green", "orange"]
        self.second_corner = ["yellow", "blue", "orange"]
        self.lst_moves = []

    def set_lst_moves(self, lst_moves):
        self.lst_moves = lst_moves

    def run(self, cubeCurrent, lst_moves):
        self.set_lst_moves(lst_moves)
        if cubeCurrent.is_solved():
            return self.lst_moves
        self.move_side(cubeCurrent, self.first_corner)
        self.move_down(cubeCurrent)	
        self.move_side(cubeCurrent,self.second_corner)
        self.move_down(cubeCurrent)
        self.move_side(cubeCurrent, self.third_corner)
        self.move_down(cubeCurrent)
        self.move_side(cubeCurrent, self.fourth_corner)
        self.move_down(cubeCurrent)
        return self.lst_moves

    def move_down(self, cubeCurrent):
        cubeCurrent.move_down()
        self.lst_moves.append("D")

    def move_side(self, cubeCurrent, lst_colors):
        mixManager = mix.Mix()
        while self.finished_three_color_pos(cubeCurrent, lst_colors) == False:
            mixManager.runMix(["L'", "U'", "L", "U"], cubeCurrent)
            self.lst_moves = utils.append_list(self.lst_moves, ["L'", "U'", "L", "U"])

    def finished_three_color_pos(self, cubeCurrent, lst_colors):
        lst_pos = self.checker.three(cubeCurrent, lst_colors[0], lst_colors[1], lst_colors[2])
        if lst_pos[0][0] == "down" and lst_pos[0][1] == "yellow":
            return True
        return False
