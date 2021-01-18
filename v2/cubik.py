from SecondaryFunctions import utils

class Cube():
    def __init__(self, size):
        faces = ['front', 'back', 'right', 'left', 'up', 'down']
        colors = ['green', 'blue', 'red', 'orange', 'white', 'yellow']
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

    def move_up(self):
        buflst = self.right[0]
        self.right[0] = self.back[0]
        self.back[0] = self.left[0]
        self.left[0] = self.front[0]
        self.front[0] = buflst
        self.moveFront(self.up, 'u')

    def move_up_counter(self):
        buflst = self.right[0]
        self.right[0] = self.front[0]
        self.front[0] = self.left[0]
        self.left[0] = self.back[0]
        self.back[0] = buflst
        self.moveFrontCounter(self.up, 'u')

    def move_down(self):
        buflst = self.right[self.size - 1]
        self.right[self.size - 1] = self.front[self.size - 1]
        self.front[self.size - 1] = self.left[self.size - 1]
        self.left[self.size - 1] = self.back[self.size - 1]
        self.back[self.size - 1] = buflst
        self.moveFront(self.down, 'd')

    def move_down_counter(self):
        buflst = self.right[self.size - 1]
        self.right[self.size - 1] = self.back[self.size - 1]
        self.back[self.size - 1] = self.left[self.size - 1]
        self.left[self.size - 1] = self.front[self.size - 1]
        self.front[self.size - 1] = buflst
        self.moveFrontCounter(self.down, 'd')

    def move_right(self):
        for i in range(self.size):
            buflst = self.down[i][self.size - 1]
            self.down[i][self.size - 1] = self.back[self.size - 1 - i][0]
            self.back[self.size - 1 - i][0] = self.up[i][self.size - 1]
            self.up[i][self.size - 1] = self.front[i][self.size - 1]
            self.front[i][self.size - 1] = buflst
        self.moveFront(self.right, 'r')

    def move_right_counter(self):
        for i in range(self.size):
            print("bonsoir")
            buflst = self.down[i][self.size - 1]
            self.down[i][self.size - 1] = self.front[i][self.size - 1]
            self.front[i][self.size - 1] = self.up[i][self.size - 1]
            self.up[i][self.size - 1] = self.back[self.size - 1 - i][0]
            self.back[self.size - 1 - i][0] = buflst
        self.moveFrontCounter(self.right, 'r')

    def move_left(self):
        for i in range(self.size):
            buflst = self.down[i][0]
            self.down[i][0] = self.front[i][0]
            self.front[i][0] = self.up[i][0]
            self.up[i][0] = self.back[self.size - 1 - i][self.size - 1]
            self.back[self.size - 1 - i][self.size - 1] = buflst
        self.moveFront(self.left, 'l')

    def move_left_counter(self):
        for i in range(self.size):
            buflst = self.down[i][0]
            self.down[i][0] = self.back[self.size - 1 - i][self.size - 1]
            self.back[self.size - 1 - i][self.size - 1] = self.up[i][0]
            self.up[i][0] = self.front[i][0]
            self.front[i][0] = buflst
        self.moveFrontCounter(self.left, 'l')

    def move_front(self):
        for i in range(self.size):
            buflst = self.up[self.size - 1][self.size - 1 - i]
            self.up[self.size - 1][self.size - 1 - i] = self.left[i][self.size - 1]
            self.left[i][self.size - 1] = self.down[0][i]
            self.down[0][i] = self.right[self.size - 1 - i][0]
            self.right[self.size - 1 - i][0] = buflst
        self.moveFront(self.front, 'f')

    def move_front_counter(self):
        for i in range(self.size):
            buflst = self.up[self.size - 1][i]
            self.up[self.size - 1][i] = self.right[i][0]
            self.right[i][0] = self.down[0][self.size - 1 - i]
            self.down[0][self.size - 1 - i] = self.left[self.size - 1 - i][self.size - 1]
            self.left[self.size - 1 - i][self.size - 1] = buflst
        self.moveFrontCounter(self.front, 'f')

    def move_back(self):
        for i in range(self.size):
            buflst = self.up[0][i]
            self.up[0][i] = self.right[i][self.size - 1]
            self.right[i][self.size - 1] = self.down[self.size - 1][self.size - 1 - i]
            self.down[self.size - 1][self.size - 1 - i] = self.left[self.size - 1 - i][0]
            self.left[self.size - 1 - i][0] = buflst
        self.moveFront(self.back, 'b')

    def move_back_counter(self):
        for i in range(self.size):
            buflst = self.up[0][self.size - 1 - i]
            self.up[0][self.size - 1 - i] = self.left[i][0]
            self.left[i][0] = self.down[self.size - 1][i]
            self.down[self.size - 1][i] = self.right[self.size - 1 - i][self.size - 1]
            self.right[self.size - 1 - i][self.size - 1] = buflst
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
            return "\033[32m"
        elif color == "blue":
            return "\033[34m"
        elif color == "red":
            return "\033[31m"
        elif color == "orange":
            return "\033[38;5;208m"
        elif color == "yellow":
            return "\033[33m"
        elif color == "white":
            return "\033[0m"

    def print_cube(self):
        default = "\033[0m"
        print("\t", end='')
        print("{}# {}# {}#{}".format(self.get_color(self.up[0][0]), self.get_color(self.up[0][1]), self.get_color(self.up[0][2]), default))
        print("\t{}# {}# {}#{}".format(self.get_color(self.up[1][0]), self.get_color(self.up[1][1]), self.get_color(self.up[1][2]), default))
        print("\t{}# {}# {}#{}\n".format(self.get_color(self.up[2][0]), self.get_color(self.up[2][1]), self.get_color(self.up[2][2]), default))

        print("{}# {}# {}# {}".format(self.get_color(self.left[0][0]), self.get_color(self.left[0][1]), self.get_color(self.left[0][2]), default), end = '  ')
        print("{}# {}# {}# {}".format(self.get_color(self.front[0][0]), self.get_color(self.front[0][1]), self.get_color(self.front[0][2]), default), end='  ')
        print("{}# {}# {}# {}".format(self.get_color(self.right[0][0]), self.get_color(self.right[0][1]), self.get_color(self.right[0][2]), default), end='  ')
        print("{}# {}# {}# {}".format(self.get_color(self.back[0][0]), self.get_color(self.back[0][1]), self.get_color(self.back[0][2]), default))

        print("{}# {}# {}# {}".format(self.get_color(self.left[1][0]), self.get_color(self.left[1][1]), self.get_color(self.left[1][2]), default), end='  ')
        print("{}# {}# {}# {}".format(self.get_color(self.front[1][0]), self.get_color(self.front[1][1]), self.get_color(self.front[1][2]), default), end='  ')
        print("{}# {}# {}# {}".format(self.get_color(self.right[1][0]), self.get_color(self.right[1][1]), self.get_color(self.right[1][2]), default), end='  ')
        print("{}# {}# {}# {}".format(self.get_color(self.back[1][0]), self.get_color(self.back[1][1]), self.get_color(self.back[1][2]), default))

        print("{}# {}# {}# {}".format(self.get_color(self.left[2][0]), self.get_color(self.left[2][1]), self.get_color(self.left[2][2]), default), end='  ')
        print("{}# {}# {}# {}".format(self.get_color(self.front[2][0]), self.get_color(self.front[2][1]), self.get_color(self.front[2][2]), default), end='  ')
        print("{}# {}# {}# {}".format(self.get_color(self.right[2][0]), self.get_color(self.right[2][1]), self.get_color(self.right[2][2]), default), end='  ')
        print("{}# {}# {}# {}".format(self.get_color(self.back[2][0]), self.get_color(self.back[2][1]), self.get_color(self.back[2][2]), default))

        print("\n\t", end='')
        print("{}# {}# {}#{}".format(self.get_color(self.down[0][0]), self.get_color(self.down[0][1]), self.get_color(self.down[0][2]), default))
        print("\t{}# {}# {}#{}".format(self.get_color(self.down[1][0]), self.get_color(self.down[1][1]), self.get_color(self.down[1][2]), default))
        print("\t{}# {}# {}#{}\n".format(self.get_color(self.down[2][0]), self.get_color(self.down[2][1]), self.get_color(self.down[2][2]), default))

