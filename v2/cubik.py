from SecondaryFunctions import utils

class Cube():
    def __init__(self, size):
        faces = ['front', 'back', 'right', 'left', 'up', 'down']
        colors = ['blue', 'green', 'red', 'orange', 'yellow', 'white']
        self.size = size
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
        index = self.size - 1
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

    def moveFront(self, face, l):
        nlist = [[x[i] for x in face] for i in range(len(face[0]))]
        for row in range(self.size):
            for col in range(self.size):
                if col >= int((self.size) / 2):
                    break
                else:
                    buffer_ = nlist[row][col]
                    nlist[row][col] = nlist[row][self.size - 1 - col]
                    nlist[row][self.size - 1 - col] = buffer_
        if l == 'f':
            self.front = nlist
        elif l == 'u':
            self.up = nlist
        elif l == 'd':
            self.down = nlist
        elif l == 'l':
            self.left = nlist
        elif l == 'r':
            self.right = nlist
        elif l == 'b':
            self.back = nlist

    def moveFrontCounter(self, face, l):
        self.moveFront(face, l)
        if l == 'f':
            self.moveFront(self.front, l)
            self.moveFront(self.front, l)
        elif l == 'u':
            self.moveFront(self.up, l)
            self.moveFront(self.up, l)
        elif l == 'd':
            self.moveFront(self.down, l)
            self.moveFront(self.down, l)
        elif l == 'l':
            self.moveFront(self.left, l)
            self.moveFront(self.left, l)
        elif l == 'r':
            self.moveFront(self.right, l)
            self.moveFront(self.right, l)
        elif l == 'b':
            self.moveFront(self.back, l)
            self.moveFront(self.back, l)

    def move_f2(self):
        self.move_front()
        self.move_front()

    def move_b2(self):
        self.move_back()
        self.move_back()

    def move_d2(self):
        self.move_down()
        self.move_down()

    def move_r2(self):
        self.move_right()
        self.move_right()

    def move_l2(self):
        self.move_left()
        self.move_left()

    def move_u2(self):
        self.move_up()
        self.move_up()

    @staticmethod
    def get_color(color):
        if color == "green":
            return "\033[92m"
        elif color == "blue":
            return "\033[34m"
        elif color == "red":
            return "\033[91m"
        elif color == "orange":
            return "\033[214m"
        elif color == "yellow":
            return "\033[93m"
        elif color == "white":
            return "\033[30m"

    def print_cube(self):
        default = "\033[0m"
        for row in range(self.size):
            print()
            space = True
            for col in range(self.size):
                if space:
                    for i in range(self.size):
                        print('     ', end='')
                    print("{} ### {}".format(self.get_color(self.up[row][col]), default), end='')
                    space = False
        for row in range(self.size):
            print()
            for col in range(self.size):
                print("{} ### {}".format(self.get_color(self.left[row][col]), default), end='')
            for col in range(self.size):
                print("{} ### {}".format(self.get_color(self.front[row][col]), default), end='')
            for col in range(self.size):
                print("{} ### {}".format(self.get_color(self.right[row][col]), default), end='')
            for col in range(self.size):
                print("{} ### {}".format(self.get_color(self.back[row][col]), default), end='')
        for row in range(self.size):
            print()
            space = True
            for col in range(self.size):
                if space:
                    for i in range(self.size):
                        print('     ', end='')
                    print("{} ### {}".format(self.get_color(self.down[row][col]), default), end='')
                    space = False
        print()
