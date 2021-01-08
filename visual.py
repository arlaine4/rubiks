import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import utils
import time
from cube import print_cube

verticies = (
	#basic corners
	(3, -3, -3),
	(3, 3, -3),
	(-3, 3, -3),
	(-3, -3, -3),
	(3, -3, 3),
	(3, 3, 3),
	(-3, -3, 3),
	(-3, 3, 3),
	#front
	(-1, 3, 3),
	(1, 3, 3),
	(-3, 1, 3),
	(-1, 1, 3),
	(1, 1, 3),
	(3, 1, 3),
	(-3, -1, 3),
	(-1, -1, 3),
	(1, -1, 3),
	(3, -1, 3),
	(-1, -3, 3),
	(1, -3, 3),
	#right
	(3, 3, 1),
	(3, 3, -1),
	(3, 1, 1),
	(3, 1, -1),
	(3, 1, -3),
	(3, -1, 1),
	(3, -1, -1),
	(3, -1, -3),
	(3, -3, 1),
	(3, -3, -1),
	#back
	(1, 3, -3),
	(-1, 3, -3),
	(1, 1, -3),
	(-1, 1, -3),
	(-3, 1, -3),
	(1, -1, -3),
	(-1, -1, -3),
	(-3, -1, -3),
	(1, -3, -3),
	(-1, -3, -3),
	#left
	(-3, 3, -1),
	(-3, 3, 1),
	(-3, 1, -1),
	(-3, 1, 1),
	(-3, -1, -1),
	(-3, -1, 1),
	(-3, -3, -1),
	(-3, -3, 1),
	#up
	(-1, 3, -1),
	(1, 3, -1),
	(-1, 3, 1),
	(1, 3, 1),
	#down
	(-1, -3, -1),
	(1, -3, -1),
	(-1, -3, 1),
	(1, -3, 1),
	#angle gauche face back oublies
	(3, 1, -3),
	(3, -1, -3)
	)

edges = (
	#Front
	(7, 8),
	(7, 41),
	(7, 10),
	(8, 9),
	(8, 31),
	(8, 11),
	(9, 12),
	(9, 5),
	(9, 30),
	(5, 20),
	(5, 13),
	(10, 11),
	(11, 12),
	(12, 13),
	(10, 43),
	(10, 14),
	(14, 15),
	(14, 6),
	(14, 45),
	(15, 18),
	(15, 16),
	(15, 11),
	(16, 17),
	(16, 12),
	(16, 19),
	(6, 18),
	(6, 47),
	(18, 19),
	(18, 54),
	(19, 4),
	(19, 55),
	#Right
	(13, 22),
	(13, 17),
	(20, 22),
	(20, 21),
	(20, 51),
	(21, 49),
	(21, 1),
	(21, 23),
	(22, 23),
	(23, 24),
	(23, 26),
	(24, 27),
	(24, 1),
	(24, 32),
	(27, 35),
	(27, 0),
	(27, 26),
	(26, 29),
	(25, 22),
	(25, 26),
	(25, 28),
	(25, 17),
	(28, 55),
	(28, 29),
	(29, 53),
	(29, 0),
	(28, 4),
	(17, 4),
	#Back
	(2, 31),
	(31, 30),
	(31, 33),
	(33, 32),
	(36, 35),
	(30, 1),
	(31, 48),
	(30, 49),
	(2, 34),
	(31, 33),
	(30, 32),
	(1, 24),
	(24, 27),
	(24, 23),
	(27, 35),
	(33, 36),
	(32, 35),
	(34, 37),
	(34, 33),
	(37, 36),
	(34, 2),
	(34, 42),
	(37, 44),
	(37, 3),
	(38, 39),
	(36, 39),
	(35, 38),
	(39, 52),
	(38, 53),
	#Left
	(7, 41),
	(41, 40),
	(40, 2),
	(40, 48),
	(41, 50),
	(41, 43),
	(40, 42),
	(7, 10),
	(43, 42), #
	(10, 14),
	(10, 43),
	(10, 11),
	(14, 45),
	(14, 15),
	(43, 45),
	(45, 44),
	(42, 44),
	(42, 34),
	(44, 37),
	(44, 46),
	(45, 47),
	(37, 36),
	(34, 33),
	(37, 3),
	(44, 46),
	(47, 6),
	(47, 54),
	(46, 52),
	(46, 3),
	#Down
	(3, 39),
	(3, 46),
	(39, 52),
	(38, 53),
	(38, 0),
	(0, 27),
	(0, 29),
	(53, 29),
	(53, 52),
	(46, 52),
	(46, 47),
	(29, 26),
	(28, 25),
	(47, 54),
	(46, 44),
	(47, 45),
	(47, 6),
	(6, 18),
	(54, 18),
	(54, 55),
	(55, 19),
	(55, 28),
	(55, 53),
	(52, 54),
	(18, 15),
	(19, 16),
	#Up
	(2, 31),
	(31, 30),
	(30, 1),
	(31, 33),
	(30, 32),
	(21, 1),
	(49, 21),
	(21, 20),
	(48, 49),
	(40, 48),
	(48, 50),
	(40, 41),
	(40, 42),
	(41, 43),
	(41, 7),
	(41, 50),
	(50, 51),
	(51, 20),
	(20, 5),
	(20, 22),
	(21, 23),
	(51, 9),
	(50, 8),
	(8, 11),
	(9, 12),
	)

surfaces = (
	#Front
	(7, 8, 11, 10),
	(8, 9, 12, 11),
	(9, 5, 13, 12),
	(10, 11, 15, 14),
	(11, 12, 16, 15),
	(12, 13, 17, 16),
	(14, 15, 18, 6),
	(15, 16, 19, 18),
	(16, 17, 4, 19),
	#Right
	(5, 20, 22, 13),
	(20, 21, 23, 22),
	(21, 1, 24, 23),
	(13, 22, 25, 17),
	(22, 23, 26, 25),
	(26, 27, 0, 29),
	(25, 26, 29, 28),
	(17, 25, 28, 4),
	(23, 24, 27, 26),
	#Back UP
	(2, 31, 33, 34),
	(31, 30, 32, 33),
	(30, 1, 56, 32),
	(34, 33, 36, 37),
	(33, 32, 35, 36),
	(32, 56, 57, 35),
	(37, 36, 39, 3),
	(36, 35, 38, 39),
	(35, 57, 0, 38),
	#Left #BACK
	(7, 41, 43, 10),
	(41, 40, 42, 43),
	(40, 2, 34, 42),
	(10, 43, 45, 14),
	(43, 42, 44, 45),
	(42, 34, 37, 44),
	(14, 45, 47, 6),
	(45, 44, 46, 47),
	(44, 37, 3, 46),
	#Down #LEFT
	(3, 39, 52, 46),
	(39, 38, 53, 52),
	(38, 0, 29, 53),
	(46, 52, 54, 47),
	(52, 53, 55, 54),
	(53, 29, 28, 55),
	(47, 54, 18, 6),
	(54, 55, 19, 18),
	(55, 28, 4, 19),
	#Up #DOWN
	(2, 31, 48, 40),
	(31, 30, 49, 48),
	(30, 1, 21, 49),
	(40, 48, 50, 41),
	(48, 49, 51, 50),
	(49, 21, 20, 51),
	(41, 50, 8, 7),
	(50, 51, 9, 8),
	(51, 20, 5, 9),
	)

colors = (
	(0, 0, 1), #blue
	(1, 0, 0), #red
	(0, 1, 0), #green
	(1, 0.5, 0), #orange
	(1, 1, 1), #white
	(1, 1, 0), #yellow
	)

black = (0, 0, 0)

def	get_color_index(cube, index_surface):
	i = 0
	j = 0
	k = 0
	while (i + 1) * 9 <= index_surface:
		i += 1
	while (i * 9) + ((j + 1) * 3) <= index_surface:
		j += 1
	while (i * 9) + (j * 3) + (k + 1) <= index_surface:
			k += 1
	return cube[i][j][k]

def Cube(cube):
	#----------------------------------------
	# Remplissage de surfaces + couleurs
	glBegin(GL_QUADS)
	i = 0
	j = 0
	for surface in surfaces:
		i = get_color_index(cube, j)
		glColor3fv(colors[i])
		for vertex in surface:
			glVertex3fv(verticies[vertex])
		j += 1
	glEnd()
	#----------------------------------------

	#----------------------------------------
	# Tracage des contours des cubes
	glLineWidth(6.0)
	glBegin(GL_LINES)
	glColor3fv(black)
	for edge in edges:
		for vertex in edge:
			glVertex3fv(verticies[vertex])
	#----------------------------------------
	glEnd()

def	main_visual(c, mix, lst_moves):
	pygame.init()
	display = (1200, 1000)
	pygame.time.Clock()
	clock = pygame.time.Clock()
	clock.tick(120)
	pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
	gluPerspective(90, (display[0]/display[1]), 0.1, 30)
	glTranslatef(0, 0, -8)
	glRotate(50, 25, 25, 10)
	glEnable(GL_DEPTH_TEST)

	opaque = 1
	turn = -1
	x = 1
	y = 1
	moves = mix.split(' ')
	i = 0
	j = 0
	bool_shuffle = False
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					pygame.quit()
					quit()
				if event.key == pygame.K_o:
					opaque *= -1
				if event.key == pygame.K_SPACE:
					turn *= -1
				if event.key == pygame.K_LEFT:
					x = -1
				if event.key == pygame.K_RIGHT:
					x = 1
				if event.key == pygame.K_UP:
					y = 3
				if event.key == pygame.K_DOWN:
					y = -3
				if event.key == pygame.K_s and i < len(moves):
					while i < len(moves):
						bool_shuffle = True
						c.cube = utils.select_move_function_to_call(moves[i], c)
						i += 1
						glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
						Cube(c.cube)
						pygame.display.flip()
						pygame.time.wait(300)
						clock.tick(120)
						glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
						Cube(c.cube)
				if event.key == pygame.K_r and j < len(lst_moves) and bool_shuffle is True:
					while j < len(lst_moves):
						c.cube = utils.select_move_function_to_call(lst_moves[j], c)
						j += 1
						glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
						Cube(c.cube)
						pygame.display.flip()
						pygame.time.wait(300)
						clock.tick(120)
						glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
						Cube(c.cube)
		opaque_on_off(False) if opaque < 0 else opaque_on_off(True)
		if turn > 0:
			glRotatef(2, x, y, 1)
		clock.tick(120)
		pygame.display.set_caption("Rubiks | {} fps".format(int(clock.get_fps())))
		glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
		Cube(c.cube)
		pygame.display.flip()
		pygame.time.wait(7)

def	opaque_on_off(on_off):
	glDisable(GL_DEPTH_TEST) if on_off is False else glEnable(GL_DEPTH_TEST)
