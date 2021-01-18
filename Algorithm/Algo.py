import sys
sys.path.insert(0, "../SecondaryFunctions")
import check_colors as check_c
import cubik

class   Algo():
    def __init__(self, cube_instance):
        self.cube = cube_instance
        self.lst_moves = []

    def run_steps(self):
        cubeOrigin = cubik.Cube()
        step_one = StepOne(cubeOrigin)
        
        step_one.run(self.cube, self.lst_moves)
