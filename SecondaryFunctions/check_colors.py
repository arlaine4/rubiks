import sys

class CheckerColors:

    def two(self, cub, colorOne, colorTwo):
        if (cub.up[0][1] is colorOne) and (cub.back[0][1] is colorTwo):
            return ([['up', colorOne, 0, 1],['back', colorTwo, 0, 1]])
        elif (cub.up[0][1] is colorTwo) and (cub.back[0][1] is colorOne):
            return ([['up', colorTwo, 0, 1],['back', colorOne, 0, 1]])
#
        elif (cub.up[1][2] is colorOne) and (cub.right[0][1] is colorTwo):
            return ([['up', colorOne, 1, 2],['right', colorTwo, 0, 1]])
        elif (cub.up[1][2] is colorTwo) and (cub.right[0][1] is colorOne):
            return ([['up', colorTwo, 1, 2],['right', colorOne, 0, 1]])
#
        elif (cub.up[2][1] is colorOne) and (cub.front[0][1] is colorTwo):
            return ([['up', colorOne, 2, 1],['front', colorTwo, 0, 1]])
        elif (cub.up[2][1] is colorTwo) and (cub.front[0][1] is colorOne):
            return ([['up', colorTwo, 2, 1],['front', colorOne, 0, 1]])
#
        elif (cub.up[1][0] is colorOne) and (cub.left[0][1] is colorTwo):
            return ([['up', colorOne, 1, 0],['left', colorTwo, 0, 1]])
        elif (cub.up[1][0] is colorTwo) and (cub.left[0][1] is colorOne):
            return ([['up', colorTwo, 1, 0],['left', colorOne, 0, 1]])
#
        elif (cub.left[1][2] is colorOne) and (cub.front[1][0] is colorTwo):
            return ([['left', colorOne, 1, 2],['front', colorTwo, 1, 0]])
        elif (cub.left[1][2] is colorTwo) and (cub.front[1][0] is colorOne):
            return ([['left', colorTwo, 1, 2],['front', colorOne, 1, 0]])
#
        elif (cub.left[1][0] is colorOne) and (cub.back[1][2] is colorTwo):
            return ([['left', colorOne, 1, 0],['back', colorTwo, 1, 2]])
        elif (cub.left[1][0] is colorTwo) and (cub.back[1][2] is colorOne):
            return ([['left', colorTwo, 1, 0],['back', colorOne, 1, 2]])
#
        elif (cub.front[1][2] is colorOne) and (cub.right[1][0] is colorTwo):
            return ([['front', colorOne, 1, 2],['right', colorTwo, 1, 0]])
        elif (cub.front[1][2] is colorTwo) and (cub.right[1][0] is colorOne):
            return ([['front', colorTwo, 1, 2],['right', colorOne, 1, 0]])
#
        elif (cub.right[1][2] is colorOne) and (cub.back[1][0] is colorTwo):
            return ([['right', colorOne, 1, 2],['back', colorTwo, 1, 0]])
        elif (cub.right[1][2] is colorTwo) and (cub.back[1][0] is colorOne):
            return ([['right', colorTwo, 1, 2],['back', colorOne, 1, 0]])
#
        elif (cub.down[0][1] is colorOne) and (cub.front[2][1] is colorTwo):
            return ([['down', colorOne, 0, 1],['front', colorTwo, 2, 1]])
        elif (cub.down[0][1] is colorTwo) and (cub.front[2][1] is colorOne):
            return ([['down', colorTwo, 0, 1],['front', colorOne, 2, 1]])
#
        elif (cub.down[1][2] is colorOne) and (cub.right[2][1] is colorTwo):
           return ([['down', colorOne, 1, 2],['right', colorTwo, 2, 1]])
        elif (cub.down[1][2] is colorTwo) and (cub.right[2][1] is colorOne):
            return ([['down', colorTwo, 1, 2],['right', colorOne, 2, 1]])
#
        elif (cub.down[2][1] is colorOne) and (cub.back[2][1] is colorTwo):
            return ([['down', colorOne, 2, 1],['back', colorTwo, 2, 1]])
        elif (cub.down[2][1] is colorTwo) and (cub.back[2][1] is colorOne):
            return ([['down', colorTwo, 2, 1],['back', colorOne, 2, 1]])
#
        elif (cub.down[1][0] is colorOne) and (cub.left[2][1] is colorTwo):
            return ([['down', colorOne, 1, 0],['left', colorTwo, 2, 1]])
        elif (cub.down[1][0] is colorTwo) and (cub.left[2][1] is colorOne):
            return ([['down', colorTwo, 1, 0],['left', colorOne, 2, 1]])
        else:
            return False

    def three(self, cub, colorOne, colorTwo, colorThree):
        if cub.up[0][0] == colorOne and cub.left[0][0] == colorTwo and cub.back[0][2] == colorThree:
            return (['up', colorOne, 0, 0],['left', colorTwo, 0, 0], ['back', colorThree, 0, 2])
        elif cub.up[0][0] == colorOne and cub.left[0][0] == colorThree and cub.back[0][2] == colorTwo:
            return (['up', colorOne, 0, 0],['left', colorThree, 0, 0], ['back', colorTwo, 0, 2])
        elif cub.up[0][0] == colorTwo and cub.left[0][0] == colorThree and cub.back[0][2] == colorOne:
            return (['up', colorTwo, 0, 0],['left', colorThree, 0, 0], ['back', colorOne, 0, 2])
        elif cub.up[0][0] == colorTwo and cub.left[0][0] == colorOne and cub.back[0][2] == colorThree:
            return (['up', colorTwo, 0, 0],['left', colorOne, 0, 0], ['back', colorThree, 0, 2])
        elif cub.up[0][0] == colorThree and cub.left[0][0] == colorOne and cub.back[0][2] == colorTwo:
            return (['up', colorThree, 0, 0],['left', colorOne, 0, 0], ['back', colorTwo, 0, 2])
        elif cub.up[0][0] == colorThree and cub.left[0][0] == colorTwo and cub.back[0][2] == colorOne:
            return (['up', colorThree, 0, 0],['left', colorTwo, 0, 0], ['back', colorOne, 0, 2])
#f
        elif cub.up[0][2] == colorOne and cub.right[0][2] == colorTwo and cub.back[0][0] == colorThree:
            return (['up', colorOne, 0, 2],['right', colorTwo, 0, 2], ['back', colorThree, 0, 0])
        elif cub.up[0][2] == colorOne and cub.right[0][2] == colorThree and cub.back[0][0] == colorTwo:
            return (['up', colorOne, 0, 2],['right', colorThree, 0, 2], ['back', colorTwo, 0, 0])
        elif cub.up[0][2] == colorTwo and cub.right[0][2] == colorThree and cub.back[0][0] == colorOne:
            return (['up', colorTwo, 0, 2],['right', colorThree, 0, 2], ['back', colorOne, 0, 0])
        elif cub.up[0][2] == colorTwo and cub.right[0][2] == colorOne and cub.back[0][0] == colorThree:
            return (['up', colorTwo, 0, 2],['right', colorOne, 0, 2], ['back', colorThree, 0, 0])
        elif cub.up[0][2] == colorThree and cub.right[0][2] == colorOne and cub.back[0][0] == colorTwo:
            return (['up', colorThree, 0, 2],['right', colorOne, 0, 2], ['back', colorTwo, 0, 0])
        elif cub.up[0][2] == colorThree and cub.right[0][2] == colorTwo and cub.back[0][0] == colorOne:
            return (['up', colorThree, 0, 2],['right', colorTwo, 0, 2], ['back', colorOne, 0, 0])
#f
        elif cub.up[2][2] == colorOne and cub.right[0][0] == colorTwo and cub.front[0][2] == colorThree:
            return (['up', colorOne, 2, 2],['right', colorTwo, 0, 0], ['front', colorThree, 0, 2])
        elif cub.up[2][2] == colorOne and cub.right[0][0] == colorThree and cub.front[0][2] == colorTwo:
            return (['up', colorOne, 2, 2],['right', colorThree, 0, 0], ['front', colorTwo, 0, 2])
        elif cub.up[2][2] == colorTwo and cub.right[0][0] == colorThree and cub.front[0][2] == colorOne:
            return (['up', colorTwo, 2, 2],['right', colorThree, 0, 0], ['front', colorOne, 0, 2])
        elif cub.up[2][2] == colorTwo and cub.right[0][0] == colorOne and cub.front[0][2] == colorThree:
            return (['up', colorTwo, 2, 2],['right', colorOne, 0, 0], ['front', colorThree, 0, 2])
        elif cub.up[2][2] == colorThree and cub.right[0][0] == colorOne and cub.front[0][2] == colorTwo:
            return (['up', colorThree, 2, 2],['right', colorOne, 0, 0], ['front', colorTwo, 0, 2])
        elif cub.up[2][2] == colorThree and cub.right[0][0] == colorTwo and cub.front[0][2] == colorOne:
            return (['up', colorThree, 2, 2],['right', colorTwo, 0, 0], ['front', colorOne, 0, 2])
#f
        elif cub.up[2][0] == colorOne and cub.left[0][2] == colorTwo and cub.front[0][0] == colorThree:
            return (['up', colorOne, 2, 0],['left', colorTwo, 0, 2], ['front', colorThree, 0, 0])
        elif cub.up[2][0] == colorOne and cub.left[0][2] == colorThree and cub.front[0][0] == colorTwo:
            return (['up', colorOne, 2, 0],['left', colorThree, 0, 2], ['front', colorTwo, 0, 0])
        elif cub.up[2][0] == colorTwo and cub.left[0][2] == colorThree and cub.front[0][0] == colorOne:
            return (['up', colorTwo, 2, 0],['left', colorThree, 0, 2], ['front', colorOne, 0, 0])
        elif cub.up[2][0] == colorTwo and cub.left[0][2] == colorOne and cub.front[0][0] == colorThree:
            return (['up', colorTwo, 2, 0],['left', colorOne, 0, 2], ['front', colorThree, 0, 0])
        elif cub.up[2][0] == colorThree and cub.left[0][2] == colorOne and cub.front[0][0] == colorTwo:
            return (['up', colorThree, 2, 0],['left', colorOne, 0, 2], ['front', colorTwo, 0, 0])
        elif cub.up[2][0] == colorThree and cub.left[0][2] == colorTwo and cub.front[0][0] == colorOne:
            return (['up', colorThree, 2, 0],['left', colorTwo, 0, 2], ['front', colorOne, 0, 0])
#f
        elif cub.down[0][0] == colorOne and cub.left[2][2] == colorTwo and cub.front[2][0] == colorThree:
            return (['down', colorOne, 0, 0],['left', colorTwo, 2, 2], ['front', colorThree, 2, 0])
        elif cub.down[0][0] == colorOne and cub.left[2][2] == colorThree and cub.front[2][0] == colorTwo:
            return (['down', colorOne, 0, 0],['left', colorThree, 2, 2], ['front', colorTwo, 2, 0])
        elif cub.down[0][0] == colorTwo and cub.left[2][2] == colorThree and cub.front[2][0] == colorOne:
            return (['down', colorTwo, 0, 0],['left', colorThree, 2, 2], ['front', colorOne, 2, 0])
        elif cub.down[0][0] == colorTwo and cub.left[2][2] == colorOne and cub.front[2][0] == colorThree:
            return (['down', colorTwo, 0, 0],['left', colorOne, 2, 2], ['front', colorThree, 2, 0])
        elif cub.down[0][0] == colorThree and cub.left[2][2] == colorOne and cub.front[2][0] == colorTwo:
            return (['down', colorThree, 0, 0],['left', colorOne, 2, 2], ['front', colorTwo, 2, 0])
        elif cub.down[0][0] == colorThree and cub.left[2][2] == colorTwo and cub.front[2][0] == colorOne:
            return (['down', colorThree, 0, 0],['left', colorTwo, 2, 2], ['front', colorOne, 2, 0])
#f
        elif cub.down[0][2] == colorOne and cub.right[2][0] == colorTwo and cub.front[2][2] == colorThree:
            return (['down', colorOne, 0, 2],['right', colorTwo, 2, 0], ['front', colorThree, 2, 2])
        elif cub.down[0][2] == colorOne and cub.right[2][0] == colorThree and cub.front[2][2] == colorTwo:
            return (['down', colorOne, 0, 2],['right', colorThree, 2, 0], ['front', colorTwo, 2, 2])
        elif cub.down[0][2] == colorTwo and cub.right[2][0] == colorThree and cub.front[2][2] == colorOne:
            return (['down', colorTwo, 0, 2],['right', colorThree, 2, 0], ['front', colorOne, 2, 2])
        elif cub.down[0][2] == colorTwo and cub.right[2][0] == colorOne and cub.front[2][2] == colorThree:
            return (['down', colorTwo, 0, 2],['right', colorOne, 2, 0], ['front', colorThree, 2, 2])
        elif cub.down[0][2] == colorThree and cub.right[2][0] == colorOne and cub.front[2][2] == colorTwo:
            return (['down', colorThree, 0, 2],['right', colorOne, 2, 0], ['front', colorTwo, 2, 2])
        elif cub.down[0][2] == colorThree and cub.right[2][0] == colorTwo and cub.front[2][2] == colorOne:
            return (['down', colorThree, 0, 2],['right', colorTwo, 2, 0], ['front', colorOne, 2, 2])
#f
        elif cub.down[2][2] == colorOne and cub.right[2][2] == colorTwo and cub.back[2][0] == colorThree:
            return (['down', colorOne, 2, 2],['right', colorTwo, 2, 2], ['back', colorThree, 2, 0])
        elif cub.down[2][2] == colorOne and cub.right[2][2] == colorThree and cub.back[2][0] == colorTwo:
            return (['down', colorOne, 2, 2],['right', colorThree, 2, 2], ['back', colorTwo, 2, 0])
        elif cub.down[2][2] == colorTwo and cub.right[2][2] == colorThree and cub.back[2][0] == colorOne:
            return (['down', colorTwo, 2, 2],['right', colorThree, 2, 2], ['back', colorOne, 2, 0])
        elif cub.down[2][2] == colorTwo and cub.right[2][2] == colorOne and cub.back[2][0] == colorThree:
            return (['down', colorTwo, 2, 2],['right', colorOne, 2, 2], ['back', colorThree, 2, 0])
        elif cub.down[2][2] == colorThree and cub.right[2][2] == colorOne and cub.back[2][0] == colorTwo:
            return (['down', colorThree, 2, 2],['right', colorOne, 2, 2], ['back', colorTwo, 2, 0])
        elif cub.down[2][2] == colorThree and cub.right[2][2] == colorTwo and cub.back[2][0] == colorOne:
            return (['down', colorThree, 2, 2],['right', colorTwo, 2, 2], ['back', colorOne, 2, 0])
#
        elif cub.down[2][0] == colorOne and cub.left[2][0] == colorTwo and cub.back[2][2] == colorThree:
            return (['down', colorOne, 2, 2],['left', colorTwo, 2, 0], ['back', colorThree, 2, 2])
        elif cub.down[2][0] == colorOne and cub.left[2][0] == colorThree and cub.back[2][2] == colorTwo:
            return (['down', colorOne, 2, 2],['left', colorThree, 2, 0], ['back', colorTwo, 2, 2])
        elif cub.down[2][0] == colorTwo and cub.left[2][0] == colorThree and cub.back[2][2] == colorOne:
            return (['down', colorTwo, 2, 2],['left', colorThree, 2, 0], ['back', colorOne, 2, 2])
        elif cub.down[2][0] == colorTwo and cub.left[2][0] == colorOne and cub.back[2][2] == colorThree:
            return (['down', colorTwo, 2, 2],['left', colorOne, 2, 0], ['back', colorThree, 2, 2])
        elif cub.down[2][0] == colorThree and cub.left[2][0] == colorOne and cub.back[2][2] == colorTwo:
            return (['down', colorThree, 2, 2],['left', colorOne, 2, 0], ['back', colorTwo, 2, 2])
        elif cub.down[2][0] == colorThree and cub.left[2][0] == colorTwo and cub.back[2][2] == colorOne:
            return (['down', colorThree, 2, 2],['left', colorTwo, 2, 0], ['back', colorOne, 2, 2])
        return False
