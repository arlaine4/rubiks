import random
import sys
sys.path.append("../")
import cubik

class Mix():
    def __init__(self):
        self.max_iteration = 200
        self.available_moves = ["F", "D", "B", "R", "L", "U", "F2", "D2", "B2", "R2", \
                "L2", "U2", "F'", "B'", "R'", "L'", "U'", "D'"]

    def randomMove(self, iterations):
        if iterations > self.max_iterations:
            print("Too many moves for random shuffle generation, enter a value <= to 100")
            sys.exit()
        lst_moves = []
        size = len(self.available_moves) - 1
        for i in range(iterations):
            n = random.randint(0, size)
            lst_moves.append(self.available_moves[n])
        return lst_moves

    def runMix(self, lst_moves, cube):
        for move in lst_moves:
            if move == "F":
                cube.move_front(False)
            elif move == "F'":
                cube.move_front(True)
            elif move == "F2":
                cube.move_f2()
            elif move == "D":
                cube.move_down(False)
            elif move == "D'":
                cube.move_down(True)
            elif move == "D2":
                cube.move_d2()
            elif move == "L":
                cube.move_left(False)
            elif move == "L'":
                cube.move_left(True)
            elif move == "L2":
                cube.move_l2()
            elif move == "R":
                cube.move_right(False)
            elif move == "R'":
                cube.move_right(True)
            elif move == "R2":
                cube.move_r2()
            elif move == "U":
                cube.move_up(False)
            elif move == "U'":
                cube.move_up(True)
            elif move == "U2":
                cube.move_u2()
            elif move == "B":
                cube.move_back(False)
            elif move == "B'":
                cube.move_back(True)
            elif move == "B2":
                cube.move_b2()

