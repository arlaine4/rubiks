import sys
import cubik
sys.path.insert(0, "../SecondaryFunctions")
from SecondaryFunctions import check_colors as check_c
from .Steps import step_one as s1

class   Algo():
    def __init__(self, cube_instance):
        self.cube = cube_instance
        self.lst_moves = []

    def run(self):
        cubeOrigin = cubik.Cube(3)
        step_one = s1.StepOne(cubeOrigin)
        
        step_one.run(self.cube, self.lst_moves)
