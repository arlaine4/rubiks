import sys
import cubik
sys.path.insert(0, "../SecondaryFunctions")
from SecondaryFunctions import check_colors as check_c
from .Steps import step_one as s1
from .Steps import step_two as s2

class   Algo():
    def __init__(self, cube_instance):
        self.cube = cube_instance
        self.lst_moves = []

    def run(self):
        cubeOrigin = cubik.Cube(3)
        step_one = s1.step_one(cubeOrigin)
        step_two = s2.step_two(cubeOrigin)
        self.lst_moves = step_one.run(self.cube, self.lst_moves)
        self.lst_moves = step_two.run(self.cube, self.lst_moves)
        print(self.lst_moves)
