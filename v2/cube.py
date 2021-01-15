from SecondaryFunctions import utils

class Cube():
    def __init__(self, size):
        faces = ['front', 'back', 'right', 'left', 'up', 'down']
        colors = ['blue', 'green', 'red', 'orange', 'yellow', 'white']
        self.colors = colors
        self.front = self.fillColors(colors[0], self.size)
        self.back = self.fillColors(colors[1], self.size)
        self.right = self.fillColors(colors[2], self.size)
        self.left = self.fillColors(colors[3], self.size)
        self.up = self.fillColors(colors[4], self.size)
        self.down = self.fillColors(colors[5], self.size)

    def fillColors(self, color, size):
        lst = []
        for row in range(size):
            s = []
            for column in range(size):
                s.append(color)
            lst.append(s)
        return lst

    def move_up(self, counter_clockwise):
        tmp_row = self.right[0]
        if not counter_clockwise:
            self.right[0] = self.back[0]
            self.back[0] = self.left[0]
            self.left[0] = self.front[0]
            self.front[0] = tmp_row
            self.moveFront(self.up, 'u')
        elif counter_clockwise:
            self.right[0] = self.front[0]
            self.front[0] = self.left[0]
            self.left[0] = self.back[0]
            self.back[0] = tmp_row
            self.moveFrontCounter(self.up, 'u')

    def move_down(self, counter_clockwise):
        i = self.size - 1
        tmp_row = self.right[i]
        if not counter_clockwise:
            self.right[i] = self.front[i]
            self.front[i] = self.left[i]
            self.left[i] = self.back[i]
            self.back[i] = tmp_row
            self.moveFront(self.down, 'd')
        elif counter_clockwise:
            self.right[i] = self.back[i]
            self.back[i] = self.left[i]
            self.left[i] = self.front[i]
            self.front[i] = tmp_row
            self.moveFrontBack(self.down, 'd')

    def move_right(self, counter_clockwise):
        index = self.size - 1
        if not counter_clockwise:
            for i in range(self.size):
                tmp_row = self.down[i][index]
                self.down[i][index] = self.back[index][0]
                self.back[index - i][0] = self.up[i][index]
                self.up[i][index] = self.front[i][index]
                self.front[i][index] = tmp_row
            self.moveFront(self.right, 'r')
        elif counter_clockwise:
            for i in range(self.size):
                tmp_row = self.down[i][index]
                self.down[i][index] = self.front[i][index]
                self.front[i][index] = self.up[i][index]
                self.up[i][index] = self.back[index - i][0]
                self.back[index - i][0] = tmp_row
            self.moveFrontCounter(self.right, 'r')

    def move_left(self, counter_clockwise):
        index = self.size - 1
        if not counter_clockwise:
            for i in range(self.size):
                tmp_row = self.down[i][0]
                self.down[i][0] = self.front[i][0]
                self.front[i][0] = self.up[i][0]
                self.up[i][0] = self.back[index - i][index]
                self.back[index - i][index] = tmp_row
            self.moveFront(self.left, 'l')
        elif counter_clockwise:
            for i in range(self.size):
                tmp_row = self.down[i][0]
                self.down[i][0] = self.back[index - i][index]
                self.back[index - i][index] = self.up[i][0]
                self.up[i][0] = self.front[i][0]
                self.front[i][0] = tmp_row
            self.moveFrontCounter(self.left, 'l')

    def move_front(self, counter_clockwise):
        index = self.size - 1
        if not counter_clockwise:
            for i in range(self.size):
                tmp_row = self.up[index][index - i]
                self.up[index][index - i] = self.left[i][index]
                self.left[i][index] = self.down[0][i]
                self.down[0][i] = self.right[index - i][0]
                self.right[index - i][0] = tmp_row
            self.moveFront(self.front, 'f')
        elif counter_clockwise:
            for i in range(self.size):
                tmp_row = self.up[index][i]
                self.up[index][i] = self.right[i][0]
                self.right[i][0] = self.down[0][index - i]
                self.down[0][index - i] = self.left[index - i][index]
                self.left[index - i][index] = tmp_row
            self.moveFrontCounter(self.front, 'f')

    def move_back(self, counter_clockwise):
        index = self.size - i
        if not counter_clockwise:
            for i in range(self.size):
                tmp_row = self.up[0][i]
                self.up[0][i] = self.right[i][index]
                self.right[i][index] = self.down[index][index - i]
                self.down[index][index - i] = self.left[index][0]
                self.left[index][0] = tmp_row
            self.moveFront(self.back, 'b')
        elif counter_clockwise:
            for i in range(self.size):
                tmp_row = self.up[0][index - i]
                self.up[0][index - i] = self.left[i][0]
                self.left[i][0] = self.down[index][i]
                self.down[index][i] = self.right[index - i][index]
                self.right[index - i][index] = tmp_row
            self.moveFrontCounter(self.back, 'b')

