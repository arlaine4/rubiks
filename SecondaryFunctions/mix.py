import random
import os
import sys
sys.path.insert(0, "../cubik")
from cubik import *

class Mix():
    def __init__(self):
        self.max_iteration = 200
        self.available_moves = ["F", "D", "B", "R", "L", "U", "F2", "D2", "B2", "R2", \
                "L2", "U2", "F'", "B'", "R'", "L'", "U'", "D'"]

    def runMix(self, lst_moves, cube):
        """Run mix move by move"""
        for move in lst_moves:
            if move == "F":
                cube.move_front()
            elif move == "F'":
                cube.move_front_counter()
            elif move == "F2":
                cube.move_f2()
            elif move == "B":
                cube.move_back()
            elif move == "B'":
                cube.move_back_counter()
            elif move == "B2":
                cube.move_b2()
            elif move == "D":
                cube.move_down()
            elif move == "D'":
                cube.move_down_counter()
            elif move == "D2":
                cube.move_d2()
            elif move == "L":
                cube.move_left()
            elif move == "L'":
                cube.move_left_counter()
            elif move == "L2":
                cube.move_l2()
            elif move == "R":
                cube.move_right()
            elif move == "R'":
                cube.move_right_counter()
            elif move == "R2":
                cube.move_r2()
            elif move == "U":
                cube.move_up()
            elif move == "U'":
                cube.move_up_counter()
            elif move == "U2":
                cube.move_u2()
        return cube
