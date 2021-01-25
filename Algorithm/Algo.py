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

    def run(self, explain):
        cubeOrigin = cubik.Cube(3) #CubeOrigin is the final solved cube != self.cube wich is the current cube state
        step_one = s1.step_one(cubeOrigin)
        step_two = s2.step_two(cubeOrigin)
        step_three = s3.step_three(cubeOrigin)
        step_four = s4.step_four()
        step_five = s5.step_five(cubeOrigin)
        step_six = s6.step_six(cubeOrigin)
        step_seven = s7.step_seven(cubeOrigin)

        #Running all seven steps one by one, append each move made to self.lst_moves and refreshing self.cube state
        if explain is True:
            print("First step :")
        self.lst_moves = step_one.run(self.cube, self.lst_moves)
        if explain is True:
            self.cube.print_cube()
            print("Second step :")
        self.lst_moves = step_two.run(self.cube, self.lst_moves)
        if explain is True:
            self.cube.print_cube()
            print("Third step :")
        self.lst_moves = step_three.run(self.cube, self.lst_moves)
        if explain is True:
            self.cube.print_cube()
            print("Fourth step :")
        self.lst_moves = step_four.run(self.cube, self.lst_moves)
        if explain is True:
            self.cube.print_cube()
            print("Fifth step :")
        self.lst_moves = step_five.run(self.cube, self.lst_moves)
        if explain is True:
            self.cube.print_cube()
            print("Sixth step :")
        self.lst_moves = step_six.run(self.cube, self.lst_moves)
        if explain is True:
            self.cube.print_cube()
            print("Seventh step :")
        self.lst_moves = step_seven.run(self.cube, self.lst_moves)
        return self.lst_moves
