import sys
sys.path.insert(0, "../../SecondaryFunctions")
sys.path.insert(0, "../../../rubiks")
import SecondaryFunctions.check_colors as check_c
import cubik
from SecondaryFunctions import mix
from SecondaryFunctions import utils

class step_four:
    """step four : do the yellow cross"""
    def __init__(self):
        self.lst_moves = []

    def run(self, cubeCurrent, lst_moves):
        self.set_lst_moves = lst_moves
        mixManager = mix.Mix()
        to_move = ["F", "L", "D", "L'", "D'", "F'"]
        one, two = utils.check_back_state(cubeCurrent.down, "yellow")
        if one == 4:
                return self.lst_moves
        if one == 1:
                mixManager.runMix(to_move, cubeCurrent)
                self.lst_moves = utils.append_list(self.lst_moves, to_move)
        one, two = utils.check_back_state(cubeCurrent.down, "yellow")
        if one == 2 and two == 0:
                mixManager.runMix(to_move, cubeCurrent)
                self.lst_moves = utils.append_list(self.lst_moves, to_move)
        elif one == 2 and two == 1:
                mixManager.runMix(["D'", "F", "L", "D", "L'", "D'", "F'"], cubeCurrent)
                self.lst_moves = utils.append_list(self.lst_moves, ["D'", "F", "L", "D", "L'", "D'", "F'"])
        elif one == 2 and two == 2:
                mixManager.runMix(["D'", "D'", "F", "L", "D", "L'", "D'", "F'"], cubeCurrent)
                self.lst_moves = utils.append_list(self.lst_moves, ["D'", "D'", "F", "L", "D", "L'", "D'", "F'"])
        elif one == 2 and two == 3:
                mixManager.runMix(["D", "F", "L", "D", "L'", "D'", "F'"], cubeCurrent)
                self.lst_moves = utils.append_list(self.lst_moves, ["D", "F", "L", "D", "L'", "D'", "F'"])
        one,two = utils.check_back_state(cubeCurrent.down, "yellow")		
        
        if one == 3 and two == 0:
                mixManager.runMix(to_move, cubeCurrent)
                self.lst_moves = utils.append_list(self.lst_moves, to_move)
        elif one == 3 and two == 1:
                mixManager.runMix(["D", "F", "L", "D", "L'", "D'", "F'"], cubeCurrent)
                self.lst_moves = utils.append_list(self.lst_moves, ["D", "F", "L", "D", "L'", "D'", "F'"])
        
        one,two = utils.check_back_state(cubeCurrent.down, "yellow")
        if one == 4:
                return self.lst_moves
