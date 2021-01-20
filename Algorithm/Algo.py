import sys
import cubik
sys.path.insert(0, "../SecondaryFunctions")
from SecondaryFunctions import check_colors as check_c
from .Steps import step_one as s1
from .Steps import step_two as s2
from .Steps import step_three as s3
from .Steps import step_four as s4
from .Steps import step_five as s5
from .Steps import step_six as s6
from .Steps import step_seven as s7

class   Algo():
    def __init__(self, cube_instance):
        self.cube = cube_instance
        self.lst_moves = []

    def run(self):
        cubeOrigin = cubik.Cube(3)
        step_one = s1.step_one(cubeOrigin)
        step_two = s2.step_two(cubeOrigin)
        step_three = s3.step_three(cubeOrigin)
        step_four = s4.step_four()
        step_five = s5.step_five(cubeOrigin)
        step_six = s6.step_six(cubeOrigin)
        step_seven = s7.step_seven(cubeOrigin)

        self.lst_moves = step_one.run(self.cube, self.lst_moves)
        self.lst_moves = step_two.run(self.cube, self.lst_moves)
        self.lst_moves = step_three.run(self.cube, self.lst_moves)
        self.lst_moves = step_four.run(self.cube, self.lst_moves)
        self.lst_moves = step_five.run(self.cube, self.lst_moves)
        self.lst_moves = step_six.run(self.cube, self.lst_moves)
        self.lst_moves = step_seven.run(self.cube, self.lst_moves)
        return self.lst_moves
