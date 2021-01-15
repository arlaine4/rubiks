import random
import sys

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
        pass
