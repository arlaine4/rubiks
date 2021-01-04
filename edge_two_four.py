import move as m
import cube as c
import visual as visu
import utils
import hta

def	edge_o_two(cube, pos, lst_move):
	fb_prio = utils.front_or_back(pos)
	i = 0
	max_ = 0
	while len(pos) > 0:
		while i < len(pos):
			if ((pos[i][0] == 0) or (pos[i][0] == 4 and pos[i][1] == 1 and pos[i][2] == 2) \
				or (pos[i][0] == 2 and pos[i][1] == 2 and pos[i][2] == 1) or \
				(pos[i][0] == 1 and pos[i][1] == 1 and pos[i][2] == 0) or \
				(pos[i][0] == 5 and pos[i][1] == 0 and pos[i][2] == 1)):
				m.move_F(cube, True)
				lst_move.append("F")
				pos.pop(i)
				p = pos[0]
				pos = hta.edge_o_detection(cube)
				i = -1
				break
			elif ((pos[i][0] == 3) or (pos[i][0] == 4 and pos[i][1] == 1 and pos[i][2] == 0) \
				or (pos[i][0] == 2 and pos[i][1] == 0 and pos[i][2] == 1) or \
				(pos[i][0] == 1 and pos[i][1] == 1 and pos[i][2] == 2) or \
				(pos[i][0] == 5 and pos[i][1] == 2 and pos[i][2] == 1)):
				m.move_B(cube, True)
				lst_move.append("B")
				pos.pop(i)
				p = pos[0]
				pos = hta.edge_o_detection(cube)
				i = -2
				break
			i += 1
		if i == 2:
			p = pos[0]
			if (p[0] == 4 and p[1] == 0 and p[2] == 1) or (p[0] == 2 and p[1] == 1 and p[2] == 0):
				if [0,1,0] not in pos and [4,1,2] not in pos:
					m.move_L(cube, True)
					lst_move.append("L")
					print("L")
					i = -1
				elif [0,0,1] not in pos and [2,2,1] not in pos:
					m.move_U(cube, False)
					lst_move.append("U'")
					print("U'")
					i = -1
			elif (p[0] == 4 and p[1] == 2 and p[2] == 1) or (p[0] == 5 and p[1] == 1 and p[2] == 0):
				if [0,1,0] not in pos and [4,1,2] not in pos:
					m.move_L(cube, False)
					lst_move.append("L'")
					print("L'")
					i = -1
				elif [0,2,1] not in pos and [5,0,1] not in pos:
					m.move_D(cube, True)
					lst_move.append("D")
					print("D")
					i = -1
			elif (p[0] == 4 and p[1] == 1 and p[2] == 0) or (p[0] == 3 and p[1] == 1 and p[2] == 2):
				if [0,1,0] not in pos and [4,1,2] not in pos:
					m.move_L(cube, True)
					m.move_L(cube, True)
					lst_move.append("L2")
					print("L2")
					i = -1
				elif [0,1,2] not in pos and [1,1,0] not in pos:
					m.move_B(cube, True)
					m.move_B(cube, True)
					lst_move.append("B2")
					m.move_R(cube, True)
					m.move_R(cube, True)
					lst_move.append("R2")
					print("B2\nR2")
					i = -1
				# ----------------------------------------------
				elif [0,0,1] not in pos and [2,2,1] not in pos:
					m.move_L(cube, True)
					m.move_U(cube, False)
					m.move_L(cube, False)
					lst_move.append("L")
					lst_move.append("U'")
					lst_move.append("L'")
					print("L\nU'\nL'")
					i = -1
				elif [0,2,1] not in pos and [5,0,1] not in pos:
					m.move_L(cube, False)
					m.move_D(cube, True)
					m.move_L(cube, True)
					lst_move.append("L'")
					lst_move.append("D")
					lst_move.append("L")
					print("L'\nD\nL")
					i = -1
				# ----------------------------------------------
			#
			#--------------------------------------------------#

			#--------------------------------------------------#
			# 				bad edge sur right
			elif (p[0] == 1 and p[1] == 2 and p[2] == 1) or (p[0] == 5 and p[1] == 1 and p[2] == 2):
				if [0, 1, 2] not in pos and [1, 1, 0] not in pos:
					m.move_R(cube, True)
					lst_move.append("R")
					print("R")
					i = -1
				elif [0,2,1] not in pos and [5,0,1] not in pos:
					m.move_D(cube, False)
					lst_move.append("D'")
					print("D'")
					i = -1
			elif (p[0] == 1 and p[1] == 0 and p[2] == 1) or (p[0] == 2 and p[1] == 1 and p[2] == 2):
				if [0, 1, 2] not in pos and [1, 1, 0] not in pos:
					m.move_R(cube, False)
					lst_move.append("R'")
					print("R'")
					i = -1
				elif [0,0,1] not in pos and [2,2,1] not in pos:
					m.move_U(cube, True)
					lst_move.append("U")
					print("U")
					i = -1
				elif [4,1,2] not in pos and [0,1,0] not in pos:
					m.move_U(cube, True)
					m.move_U(cube, True)
					lst_move.append("U2")
					m.move_L(cube, True)
					lst_move.append("L")
					m.move_U(cube, True)
					m.move_U(cube, True)
					lst_move.append("U2")
					print("U2\nL\nU2")
					i = -1
			elif (p[0] == 1 and p[1] == 1 and p[2] == 2) or (p[0] == 3 and p[1] == 1 and p[2] == 0):
				if [0, 1, 2] not in pos and [1, 1, 0] not in pos:
					m.move_R(cube, True)
					m.move_R(cube, True)
					lst_move.append("R2")
					print("R2")
					i = -1
				elif [0,1,0] not in pos and [4,1,2] not in pos:
					m.move_B(cube, True)
					m.move_B(cube, True)
					lst_move.append("B2")
					m.move_L(cube, True)
					m.move_L(cube, True)
					lst_move.append("L2")
					print("B2\L2")
					i = -1
				# ----------------------------------------------
				elif [0,0,1] not in pos and [2,2,1] not in pos:
					m.move_R(cube, False)
					m.move_U(cube, True)
					m.move_R(cube, True)
					lst_move.append("R'")
					lst_move.append("U")
					lst_move.append("R")
					print("R'\nU\nR")
					i = -1
				elif [0,2,1] not in pos and [5,0,1] not in pos:
					m.move_R(cube, True)
					m.move_D(cube, False)
					m.move_R(cube, False)
					lst_move.append("R")
					lst_move.append("D'")
					lst_move.append("R'")
					print("R\nD'\nR'")
					i = -1
				# ----------------------------------------------
			#
			#--------------------------------------------------#

			#--------------------------------------------------#
			# 				bad edge sur up
			elif (p[0] == 2 and p[1] == 1 and p[2] == 2) or (p[0] == 1 and p[1] == 0 and p[2] == 1):
				if [2, 2, 1] not in pos and [0, 0, 1] not in pos:
					m.move_U(cube, True)
					lst_move.append("U")
					print("U")
					i = -1
				elif [0,1,2] not in pos and [1,1,0] not in pos:
					m.move_R(cube, False)
					lst_move.append("R'")
					print("R'")
					i = -1
			elif (p[0] == 2 and p[1] == 1 and p[2] == 0) or (p[0] == 4 and p[1] == 0 and p[1] == 1):
				if [2, 2, 1] not in pos and [0, 0, 1] not in pos:
					m.move_U(cube, False)
					lst_move.append("U'")
					print("U'")
					i = -1
				elif [0,1,0] not in pos and [4,1,2] not in pos:
					m.move_L(cube, True)
					lst_move.append("L")
					print("L")
					i = -1
			elif (p[0] == 2 and p[1] == 0 and p[2] == 1) or (p[0] == 3 and p[1] == 0 and p[2] == 1):
				if [2, 2, 1] not in pos and [0, 0, 1] not in pos:
					m.move_U(cube, True)
					m.move_U(cube, True)
					lst_move.append("U2")
					print("U2")
					i = -1
				elif [5, 0, 1] not in pos and [0, 2, 1] not in pos:
					m.move_B(cube, True)
					m.move_B(cube, True)
					lst_move.append("B2")
					m.move_D(cube, True)
					m.move_D(cube, True)
					lst_move.append("D2")
					print("B2\nD2")
					i = -1
				# ----------------------------------------------
				elif [0,1,2] not in pos and [1,1,0] not in pos:
					m.move_U(cube, True)
					m.move_R(cube, False)
					m.move_U(cube, False)
					lst_move.append("U")
					lst_move.append("R'")
					lst_move.append("U'")
					print("U\nR\nU'")
					i = -1
				elif [0,1,0] not in pos and [4,1,2] not in pos:
					m.move_U(cube, False)
					m.move_L(cube, True)
					m.move_U(cube, True)
					lst_move.append("U'")
					lst_move.append("L")
					lst_move.append("U")
					print("U'\nL\nU")
					i = -1
				# ----------------------------------------------
			#
			#--------------------------------------------------#
	
			#--------------------------------------------------#
			# 				bad edge sur down
			elif (p[0] == 5 and p[1] == 1 and p[2] == 0) or (p[0] == 4 and p[1] == 2 and p[2] == 1):
				if [5, 0, 1] not in pos and [0, 2, 1] not in pos:
					m.move_D(cube, True)
					lst_move.append("D")
					print("D")
					i = -1
				elif [0,1,0] not in pos and [4,1,2] not in pos:
					m.move_L(cube, False)
					lst_move.append("L'")
					print("L'")
					i = -1
			elif (p[0] == 5 and p[1] == 1 and p[2] == 2) or (p[0] == 1 and p[1] == 2 and p[2] == 1):
				if [5, 0, 1] not in pos and [0, 2, 1] not in pos:
					m.move_D(cube, False)
					lst_move.append("D'")
					print("D'")
					i = -1
				elif [0,1,2] not in pos and [1,1,0] not in pos:
					m.move_R(cube, True)
					lst_move.append("R")
					print("R")
					i = -1
			elif (p[0] == 5 and p[1] == 2 and p[2] == 1) or (p[0] == 3 and p[1] == 2 and p[2] == 1):
				if [5, 0, 1] not in pos and [0, 2, 1] not in pos:
					m.move_D(cube, True)
					m.move_D(cube, True)
					lst_move.append("D2")
					print("D2")
					i = -1
				elif [2, 2, 1] not in pos and [0, 0, 1] not in pos:
					m.move_B(cube, True)
					m.move_B(cube, True)
					lst_move.append("B2")
					m.move_D(cube, True)
					m.move_D(cube, True)
					lst_move.append("D2")
					print("B2\nD2")
					i = -1
				# ----------------------------------------------
				elif [0,1,2] not in pos and [1,1,0] not in pos:
					m.move_D(cube, False)
					m.move_R(cube, True)
					m.move_D(cube, True)
					lst_move.append("D'")
					lst_move.append("R")
					lst_move.append("D")
					print("D'\nR\nD")
					i = -1
				elif [0,1,0] not in pos and [4,1,2] not in pos:
					m.move_D(cube, True)
					m.move_L(cube, False)
					m.move_D(cube, False)
					lst_move.append("D")
					lst_move.append("L'")
					lst_move.append("D'")
					print("D\nL'\nD'")
					i = -1
				# ----------------------------------------------
			m.move_F(cube, True)
			lst_move.append("F")
			pos = hta.edge_o_detection(cube)
			for elem in pos:
				if ((elem[0] == 0) or (elem[0] == 4 and elem[1] == 1 and elem[2] == 2) \
					or (elem[0] == 2 and elem[1] == 2 and elem[2] == 1) or \
					(elem[0] == 1 and elem[1] == 1 and elem[2] == 0) or \
					(elem[0] == 5 and elem[1] == 0 and elem[2] == 1)):
					continue
				else:
					p = elem
					break
			i = -1
		if i == -1:
			print("ici mec:", p)
			# 				bad edge sur left
			if (p[0] == 4 and p[1] == 0 and p[2] == 1) or (p[0] == 2 and p[1] == 1 and p[2] == 0):
				if [0,1,0] not in pos and [4,1,2] not in pos:
					m.move_L(cube, True)
					lst_move.append("L")
					print("L")
				elif [0,0,1] not in pos and [2,2,1] not in pos:
					m.move_U(cube, False)
					lst_move.append("U'")
					print("U'")
			elif (p[0] == 4 and p[1] == 2 and p[2] == 1) or (p[0] == 5 and p[1] == 1 and p[2] == 0):
				if [0,1,0] not in pos and [4,1,2] not in pos:
					m.move_L(cube, False)
					lst_move.append("L'")
					print("L'")
				elif [0,2,1] not in pos and [5,0,1] not in pos:
					m.move_D(cube, True)
					lst_move.append("D")
					print("D")
			elif (p[0] == 4 and p[1] == 1 and p[2] == 0) or (p[0] == 3 and p[1] == 1 and p[2] == 2):
				if [0,1,0] not in pos and [4,1,2] not in pos:
					m.move_L(cube, True)
					m.move_L(cube, True)
					lst_move.append("L2")
					print("L2")
				elif [0,1,2] not in pos and [1,1,0] not in pos:
					m.move_B(cube, True)
					m.move_B(cube, True)
					lst_move.append("B2")
					m.move_R(cube, True)
					m.move_R(cube, True)
					lst_move.append("R2")
					print("B2\nR2")
				# ----------------------------------------------
				elif [0,0,1] not in pos and [2,2,1] not in pos:
					m.move_L(cube, True)
					m.move_U(cube, False)
					m.move_L(cube, False)
					lst_move.append("L")
					lst_move.append("U'")
					lst_move.append("L'")
					print("L\nU'\nL'")
				elif [0,2,1] not in pos and [5,0,1] not in pos:
					m.move_L(cube, False)
					m.move_D(cube, True)
					m.move_L(cube, True)
					lst_move.append("L'")
					lst_move.append("D")
					lst_move.append("L")
					print("L'\nD\nL")
				# ----------------------------------------------
			#
			#--------------------------------------------------#

			#--------------------------------------------------#
			# 				bad edge sur right
			elif (p[0] == 1 and p[1] == 2 and p[2] == 1) or (p[0] == 5 and p[1] == 1 and p[2] == 2):
				if [0, 1, 2] not in pos and [1, 1, 0] not in pos:
					m.move_R(cube, True)
					lst_move.append("R")
					print("R")
				elif [0,2,1] not in pos and [5,0,1] not in pos:
					m.move_D(cube, False)
					lst_move.append("D'")
					print("D'")
			elif (p[0] == 1 and p[1] == 0 and p[2] == 1) or (p[0] == 2 and p[1] == 1 and p[2] == 2):
				if [0, 1, 2] not in pos and [1, 1, 0] not in pos:
					m.move_R(cube, False)
					lst_move.append("R'")
					print("R'")
				elif [0,0,1] not in pos and [2,2,1] not in pos:
					m.move_U(cube, True)
					lst_move.append("U")
					print("U")
				elif [4,1,2] not in pos and [0,1,0] not in pos:
					m.move_U(cube, True)
					m.move_U(cube, True)
					lst_move.append("U2")
					print("U2")
					m.move_L(cube, True)
					lst_move.append("L")
					print("L")
					m.move_U(cube, True)
					m.move_U(cube, True)
					lst_move.append("U2")
					print("U2")
			elif (p[0] == 1 and p[1] == 1 and p[2] == 2) or (p[0] == 3 and p[1] == 1 and p[2] == 0):
				if [0, 1, 2] not in pos and [1, 1, 0] not in pos:
					m.move_R(cube, True)
					m.move_R(cube, True)
					lst_move.append("R2")
					print("R2")
				elif [0,1,0] not in pos and [4,1,2] not in pos:
					m.move_B(cube, True)
					m.move_B(cube, True)
					lst_move.append("B2")
					m.move_L(cube, True)
					m.move_L(cube, True)
					lst_move.append("L2")
					print("B2\L2")
				# ----------------------------------------------
				elif [0,0,1] not in pos and [2,2,1] not in pos:
					m.move_R(cube, False)
					m.move_U(cube, True)
					m.move_R(cube, True)
					lst_move.append("R'")
					lst_move.append("U")
					lst_move.append("R")
					print("R'\nU\nR")
				elif [0,2,1] not in pos and [5,0,1] not in pos:
					m.move_R(cube, True)
					m.move_D(cube, False)
					m.move_R(cube, False)
					lst_move.append("R")
					lst_move.append("D'")
					lst_move.append("R'")
					print("R\nD'\nR'")
				# ----------------------------------------------
			#
			#--------------------------------------------------#

			#--------------------------------------------------#
			# 				bad edge sur up
			elif (p[0] == 2 and p[1] == 1 and p[2] == 2) or (p[0] == 1 and p[1] == 0 and p[2] == 1):
				if [2, 2, 1] not in pos and [0, 0, 1] not in pos:
					m.move_U(cube, True)
					lst_move.append("U")
					print("U")
				elif [0,1,2] not in pos and [1,1,0] not in pos:
					m.move_R(cube, False)
					lst_move.append("R'")
					print("R'")
			elif (p[0] == 2 and p[1] == 1 and p[2] == 0) or (p[0] == 4 and p[1] == 0 and p[1] == 1):
				if [2, 2, 1] not in pos and [0, 0, 1] not in pos:
					m.move_U(cube, False)
					lst_move.append("U'")
					print("U'")
				elif [0,1,0] not in pos and [4,1,2] not in pos:
					m.move_L(cube, True)
					lst_move.append("L")
					print("L")
			elif (p[0] == 2 and p[1] == 0 and p[2] == 1) or (p[0] == 3 and p[1] == 0 and p[2] == 1):
				if [2, 2, 1] not in pos and [0, 0, 1] not in pos:
					m.move_U(cube, True)
					m.move_U(cube, True)
					lst_move.append("U2")
					print("U2")
				elif [5, 0, 1] not in pos and [0, 2, 1] not in pos:
					m.move_B(cube, True)
					m.move_B(cube, True)
					lst_move.append("B2")
					m.move_D(cube, True)
					m.move_D(cube, True)
					lst_move.append("D2")
					print("B2\nD2")
				# ----------------------------------------------
				elif [0,1,2] not in pos and [1,1,0] not in pos:
					m.move_U(cube, True)
					m.move_R(cube, False)
					m.move_U(cube, False)
					lst_move.append("U")
					lst_move.append("R'")
					lst_move.append("U'")
					print("U\nR\nU'")
				elif [0,1,0] not in pos and [4,1,2] not in pos:
					m.move_U(cube, False)
					m.move_L(cube, True)
					m.move_U(cube, True)
					lst_move.append("U'")
					lst_move.append("L")
					lst_move.append("U")
					print("U'\nL\nU")
				# ----------------------------------------------
			#
			#--------------------------------------------------#
	
			#--------------------------------------------------#
			# 				bad edge sur down
			elif (p[0] == 5 and p[1] == 1 and p[2] == 0) or (p[0] == 4 and p[1] == 2 and p[2] == 1):
				if [5, 0, 1] not in pos and [0, 2, 1] not in pos:
					m.move_D(cube, True)
					lst_move.append("D")
					print("D")
				elif [0,1,0] not in pos and [4,1,2] not in pos:
					m.move_L(cube, False)
					lst_move.append("L'")
					print("L'")
			elif (p[0] == 5 and p[1] == 1 and p[2] == 2) or (p[0] == 1 and p[1] == 2 and p[2] == 1):
				if [5, 0, 1] not in pos and [0, 2, 1] not in pos:
					m.move_D(cube, False)
					lst_move.append("D'")
					print("D'")
				elif [0,1,2] not in pos and [1,1,0] not in pos:
					m.move_R(cube, True)
					lst_move.append("R")
					print("R")
			elif (p[0] == 5 and p[1] == 2 and p[2] == 1) or (p[0] == 3 and p[1] == 2 and p[2] == 1):
				if [5, 0, 1] not in pos and [0, 2, 1] not in pos:
					m.move_D(cube, True)
					m.move_D(cube, True)
					lst_move.append("D2")
					print("D2")
				elif [2, 2, 1] not in pos and [0, 0, 1] not in pos:
					m.move_B(cube, True)
					m.move_B(cube, True)
					lst_move.append("B2")
					m.move_D(cube, True)
					m.move_D(cube, True)
					lst_move.append("D2")
					print("B2\nD2")
				# ----------------------------------------------
				elif [0,1,2] not in pos and [1,1,0] not in pos:
					m.move_D(cube, False)
					m.move_R(cube, True)
					m.move_D(cube, True)
					lst_move.append("D'")
					lst_move.append("R")
					lst_move.append("D")
					print("D'\nR\nD")
				elif [0,1,0] not in pos and [4,1,2] not in pos:
					m.move_D(cube, True)
					m.move_L(cube, False)
					m.move_D(cube, False)
					lst_move.append("D")
					lst_move.append("L'")
					lst_move.append("D'")
					print("D\nL'\nD'")
				# ----------------------------------------------	
			m.move_F(cube, True)
			lst_move.append("F")
		elif i == -2:
			if (p[0] == 5 and p[1] == 1 and p[2] == 0) or (p[0] == 4 and p[1] == 2 and p[2] == 1):
				if [3,1,2] not in pos and [4,1,0] not in pos:
					m.move_L(cube, True)
					lst_move.append("L")
					print("L")
				elif [0,2,1] not in pos and [3,2,1] not in pos:
					m.move_D(cube, False)
					lst_move.append("D'")
					print("D'")
			elif (p[0] == 4 and p[1] == 0 and p[2] == 1) or (p[0] == 2 and p[1] == 1 and p[2] == 0):
				if [3,1,2] not in pos and [4,1,0] not in pos:
					m.move_L(cube, False)
					lst_move.append("L'")
					print("L'")
				elif [2,0,1] not in pos and [3,0,1] not in pos:
					m.move_U(cube, True)
					lst_move.append("U")
					print("U")
			elif (p[0] == 4 and p[1] == 1 and p[2] == 2) or (p[0] == 0 and p[1] == 1 and p[2] == 0):
				if [3,1,2] not in pos and [4,1,0] not in pos:
					m.move_L(cube, True)
					m.move_L(cube, True)
					lst_move.append("L2")
					print("L2")
				elif [1, 1, 2] not in pos and [3, 1, 0] not in pos:
					m.move_F(cube, True)
					m.move_F(cube, True)
					lst_move.append("F2")
					m.move_R(cube, True)
					m.move_R(cube, True)
					lst_move.append("R2")
					print("F2\nR2")
				# ----------------------------------------------
				elif [2,0,1] not in pos and [3,0,1] not in pos:
					m.move_L(cube, False)
					m.move_U(cube, True)
					m.move_L(cube, True)
					lst_move.append("L'")
					lst_move.append("U")
					lst_move.append("L")
					print("L'\nU\nL")
				elif [5,2,1] not in pos and [3,2,1] not in pos:
					m.move_L(cube, True)
					m.move_D(cube, False)
					m.move_L(cube, False)
					lst_move.append("L")
					lst_move.append("D'")
					lst_move.append("L'")
					print("L\nD'\nL'")
				# ----------------------------------------------
			#
			#--------------------------------------------------#

			#--------------------------------------------------#
			# 				bad edge sur right
			elif (p[0] == 2 and p[1] == 1 and p[2] == 2) or (p[0] == 1 and p[1] == 0 and p[2] == 1):
				if [1, 1, 2] not in pos and [3, 1, 0] not in pos:
					m.move_R(cube, True)
					lst_move.append("R")
					print("R")
				elif [3,0,1] not in pos and [2,0,1] not in pos:
					m.move_U(cube, False)
					lst_move.append("U'")
					print("U'")
			elif (p[0] == 1 and p[1] == 2 and p[2] == 1) or (p[0] == 5 and p[1] == 1 and p[2] == 2):
				if [1, 1, 2] not in pos and [3, 1, 0] not in pos:
					m.move_R(cube, False)
					lst_move.append("R'")
					print("R'")
				elif [5,2,1] not in pos and [3,2,1] not in pos:
					m.move_D(cube, True)
					lst_move.append("D")
					print("D")
			elif (p[0] == 0 and p[1] == 1 and p[2] == 2) or (p[0] == 1 and p[1] == 1 and p[2] == 0):
				if [1, 1, 2] not in pos and [3, 1, 0] not in pos:
					m.move_R(cube, True)
					m.move_R(cube, True)
					lst_move.append("R2")
					print("R2")
				elif [3,1,2] not in pos and [4,1,0] not in pos:
					m.move_F(cube, True)
					m.move_F(cube, True)
					lst_move.append("F2")
					m.move_L(cube, True)
					m.move_L(cube, True)
					lst_move.append("L2")
					print("F2\nL2")
				# ----------------------------------------------
				elif [2,0,1] not in pos and [3,0,1] not in pos:
					m.move_R(cube, False)
					m.move_U(cube, False)
					m.move_R(cube, True)
					lst_move.append("R'")
					lst_move.append("U'")
					lst_move.append("R")
					print("R'\nU'\nR")
				elif [5,2,1] not in pos and [3,2,1] not in pos:
					m.move_R(cube, True)
					m.move_D(cube, True)
					m.move_R(cube, False)
					lst_move.append("R")
					lst_move.append("D")
					lst_move.append("R'")
					print("R\nD\nR'")
				# ----------------------------------------------
			#
			#--------------------------------------------------#

			#--------------------------------------------------#
			# 				bad edge sur up
			elif (p[0] == 4 and p[1] == 0 and p[2] == 1) or (p[0] == 2 and p[1] == 1 and p[2] == 0):
				if [2, 0, 1] not in pos and [3, 0, 1] not in pos:
					m.move_U(cube, True)
					lst_move.append("U")
					print("U")
				elif [4,1,0] not in pos and [3,1,2] not in pos:
					m.move_L(cube, False)
					lst_move.append("L'")
					print("L'")
			elif (p[0] == 1 and p[1] == 0 and p[2] == 1) or (p[0] == 2 and p[1] == 1 and p[1] == 2):
				if [2, 0, 1] not in pos and [3, 0, 1] not in pos:
					m.move_U(cube, False)
					lst_move.append("U'")
					print("U'")
				elif [1,1,2] not in pos and [3,1,0] not in pos:
					m.move_R(cube, True)
					lst_move.append("R")
					print("R")
			elif (p[0] == 2 and p[1] == 2 and p[2] == 1) or (p[0] == 0 and p[1] == 0 and p[2] == 1):
				if [2, 0, 1] not in pos and [3, 0, 1] not in pos:
					m.move_U(cube, True)
					m.move_U(cube, True)
					lst_move.append("U2")
					print("U2")
				elif [5, 2, 1] not in pos and [3, 2, 1] not in pos:
					m.move_F(cube, True)
					m.move_F(cube, True)
					lst_move.append("F2")
					m.move_D(cube, True)
					m.move_D(cube, True)
					lst_move.append("D2")
					print("F2\nD2")
				# ----------------------------------------------
				elif [4,1,0] not in pos and [3,1,2] not in pos:
					m.move_U(cube, True)
					m.move_L(cube, False)
					m.move_U(cube, False)
					lst_move.append("U")
					lst_move.append("L'")
					lst_move.append("U'")
					print("U\nL'\nU'")
				elif [1,2,2] not in pos and [3,1,0] not in pos:
					m.move_U(cube, False)
					m.move_R(cube, True)
					m.move_U(cube, True)
					lst_move.append("U'")
					lst_move.append("R")
					lst_move.append("U")
					print("U'\nR\nU")
				# ----------------------------------------------
			#
			#--------------------------------------------------#
	
			#--------------------------------------------------#
			# 				bad edge sur down
			elif (p[0] == 1 and p[1] == 2 and p[2] == 1) or (p[0] == 5 and p[1] == 1 and p[2] == 2):
				if [5, 2, 1] not in pos and [3, 2, 1] not in pos:
					m.move_D(cube, True)
					lst_move.append("D")
					print("D")
				elif [1,1,2] not in pos and [3,1,0] not in pos:
					m.move_R(cube, False)
					lst_move.append("R'")
					print("R'")
			elif (p[0] == 5 and p[1] == 1 and p[2] == 0) or (p[0] == 4 and p[1] == 2 and p[2] == 1):
				if [5, 2, 1] not in pos and [3, 2, 1] not in pos:
					m.move_D(cube, False)
					lst_move.append("D'")
					print("D'")
				elif [4,1,0] not in pos and [3,1,2] not in pos:
					m.move_L(cube, False)
					lst_move.append("L'")
					print("L'")
			elif (p[0] == 0 and p[1] == 2 and p[2] == 1) or (p[0] == 5 and p[1] == 0 and p[2] == 1):
				if [5, 2, 1] not in pos and [3, 2, 1] not in pos:
					m.move_D(cube, True)
					m.move_D(cube, True)
					lst_move.append("D2")
					print("D2")
				elif [2, 0, 1] not in pos and [3, 0, 1] not in pos:
					m.move_F(cube, True)
					m.move_F(cube, True)
					lst_move.append("F2")
					m.move_U(cube, True)
					m.move_U(cube, True)
					lst_move.append("U2")
					print("F2\nU2")
				# ----------------------------------------------
				elif [4,1,0] not in pos and [3,1,2] not in pos:
					m.move_D(cube, False)
					m.move_L(cube, True)
					m.move_D(cube, True)
					lst_move.append("D'")
					lst_move.append("L")
					lst_move.append("D")
					print("D'\nL\nD")
				elif [1,2,2] not in pos and [3,1,0] not in pos:
					print(p)
					m.move_D(cube, True)
					m.move_R(cube, False)
					m.move_D(cube, False)
					lst_move.append("D")
					lst_move.append("R'")
					lst_move.append("D'")
					print("D\nR'\nD'")
				# ----------------------------------------------
			m.move_B(cube, True)
			lst_move.append("B")
		pos = hta.edge_o_detection(cube)
		p.clear()
		max_ += 1
		if max_ >= 20:
			break
		break

	return cube, lst_move

def	edge_o_four(cube, pos, lst_move):
	print(pos)
	fb_prio = utils.front_or_back(pos)
	i = 0
	max_ = 0
	while len(pos) > 0:
		if fb_prio == "F":
			while i < len(pos):
				if ((pos[i][0] == 0) or (pos[i][0] == 4 and pos[i][1] == 1 and pos[i][2] == 2) \
					or (pos[i][0] == 2 and pos[i][1] == 2 and pos[i][2] == 1) or \
					(pos[i][0] == 1 and pos[i][1] == 1 and pos[i][2] == 0) or \
					(pos[i][0] == 5 and pos[i][1] == 0 and pos[i][2] == 1)):
					i += 1
				else:
					p = pos[i]
					i = 0
					break
			#--------------------------------------------------#
			# 				bad edge sur left
			if not p:
				break
			if (p[0] == 4 and p[1] == 0 and p[2] == 1) or (p[0] == 2 and p[1] == 1 and p[2] == 0):
				if [0,1,0] not in pos and [4,1,2] not in pos:
					m.move_L(cube, True)
					lst_move.append("L")
					print("L")
				elif [0,0,1] not in pos and [2,2,1] not in pos:
					m.move_U(cube, False)
					lst_move.append("U'")
					print("U'")
			elif (p[0] == 4 and p[1] == 2 and p[2] == 1) or (p[0] == 5 and p[1] == 1 and p[2] == 0):
				if [0,1,0] not in pos and [4,1,2] not in pos:
					m.move_L(cube, False)
					lst_move.append("L'")
					print("L'")
				elif [0,2,1] not in pos and [5,0,1] not in pos:
					m.move_D(cube, True)
					lst_move.append("D")
					print("D")
			elif (p[0] == 4 and p[1] == 1 and p[2] == 0) or (p[0] == 3 and p[1] == 1 and p[2] == 2):
				if [0,1,0] not in pos and [4,1,2] not in pos:
					m.move_L(cube, True)
					m.move_L(cube, True)
					lst_move.append("L2")
					print("L2")
				elif [0,1,2] not in pos and [1,1,0] not in pos:
					m.move_B(cube, True)
					m.move_B(cube, True)
					lst_move.append("B2")
					m.move_R(cube, True)
					m.move_R(cube, True)
					lst_move.append("R2")
					print("B2\nR2")
				# ----------------------------------------------
				elif [0,0,1] not in pos and [2,2,1] not in pos:
					m.move_L(cube, True)
					m.move_U(cube, False)
					m.move_L(cube, False)
					lst_move.append("L")
					lst_move.append("U'")
					lst_move.append("L'")
					print("L\nU'\nL'")
				elif [0,2,1] not in pos and [5,0,1] not in pos:
					m.move_L(cube, False)
					m.move_D(cube, True)
					m.move_L(cube, True)
					lst_move.append("L'")
					lst_move.append("D")
					lst_move.append("L")
					print("L'\nD\nL")
				# ----------------------------------------------
			#
			#--------------------------------------------------#

			#--------------------------------------------------#
			# 				bad edge sur right
			elif (p[0] == 1 and p[1] == 2 and p[2] == 1) or (p[0] == 5 and p[1] == 1 and p[2] == 2):
				if [0, 1, 2] not in pos and [1, 1, 0] not in pos:
					m.move_R(cube, True)
					lst_move.append("R")
					print("R")
				elif [0,2,1] not in pos and [5,0,1] not in pos:
					m.move_D(cube, False)
					lst_move.append("D'")
					print("D'")
			elif (p[0] == 1 and p[1] == 0 and p[2] == 1) or (p[0] == 2 and p[1] == 1 and p[2] == 2):
				if [0, 1, 2] not in pos and [1, 1, 0] not in pos:
					m.move_R(cube, False)
					lst_move.append("R'")
					print("R'")
				elif [0,0,1] not in pos and [2,2,1] not in pos:
					m.move_U(cube, True)
					lst_move.append("U")
					print("U")
				elif [4,1,2] not in pos and [0,1,0] not in pos:
					m.move_U(cube, True)
					m.move_U(cube, True)
					lst_move.append("U2")
					print("U2")
					m.move_L(cube, True)
					lst_move.append("L")
					print("L")
					m.move_U(cube, True)
					m.move_U(cube, True)
					lst_move.append("U2")
					print("U2")
			elif (p[0] == 1 and p[1] == 1 and p[2] == 2) or (p[0] == 3 and p[1] == 1 and p[2] == 0):
				if [0, 1, 2] not in pos and [1, 1, 0] not in pos:
					m.move_R(cube, True)
					m.move_R(cube, True)
					lst_move.append("R2")
					print("R2")
				elif [0,1,0] not in pos and [4,1,2] not in pos:
					m.move_B(cube, True)
					m.move_B(cube, True)
					lst_move.append("B2")
					m.move_L(cube, True)
					m.move_L(cube, True)
					lst_move.append("L2")
					print("B2\L2")
				# ----------------------------------------------
				elif [0,0,1] not in pos and [2,2,1] not in pos:
					m.move_R(cube, False)
					m.move_U(cube, True)
					m.move_R(cube, True)
					lst_move.append("R'")
					lst_move.append("U")
					lst_move.append("R")
					print("R'\nU\nR")
				elif [0,2,1] not in pos and [5,0,1] not in pos:
					m.move_R(cube, True)
					m.move_D(cube, False)
					m.move_R(cube, False)
					lst_move.append("R")
					lst_move.append("D'")
					lst_move.append("R'")
					print("R\nD'\nR'")
				# ----------------------------------------------
			#
			#--------------------------------------------------#

			#--------------------------------------------------#
			# 				bad edge sur up
			elif (p[0] == 2 and p[1] == 1 and p[2] == 2) or (p[0] == 1 and p[1] == 0 and p[2] == 1):
				if [2, 2, 1] not in pos and [0, 0, 1] not in pos:
					m.move_U(cube, True)
					lst_move.append("U")
					print("U")
				elif [0,1,2] not in pos and [1,1,0] not in pos:
					m.move_R(cube, False)
					lst_move.append("R'")
					print("R'")
			elif (p[0] == 2 and p[1] == 1 and p[2] == 0) or (p[0] == 4 and p[1] == 0 and p[1] == 1):
				if [2, 2, 1] not in pos and [0, 0, 1] not in pos:
					m.move_U(cube, False)
					lst_move.append("U'")
					print("U'")
				elif [0,1,0] not in pos and [4,1,2] not in pos:
					m.move_L(cube, True)
					lst_move.append("L")
					print("L")
			elif (p[0] == 2 and p[1] == 0 and p[2] == 1) or (p[0] == 3 and p[1] == 0 and p[2] == 1):
				if [2, 2, 1] not in pos and [0, 0, 1] not in pos:
					m.move_U(cube, True)
					m.move_U(cube, True)
					lst_move.append("U2")
					print("U2")
				elif [5, 0, 1] not in pos and [0, 2, 1] not in pos:
					m.move_B(cube, True)
					m.move_B(cube, True)
					lst_move.append("B2")
					m.move_D(cube, True)
					m.move_D(cube, True)
					lst_move.append("D2")
					print("B2\nD2")
				# ----------------------------------------------
				elif [0,1,2] not in pos and [1,1,0] not in pos:
					m.move_U(cube, True)
					m.move_R(cube, False)
					m.move_U(cube, False)
					lst_move.append("U")
					lst_move.append("R'")
					lst_move.append("U'")
					print("U\nR\nU'")
				elif [0,1,0] not in pos and [4,1,2] not in pos:
					m.move_U(cube, False)
					m.move_L(cube, True)
					m.move_U(cube, True)
					lst_move.append("U'")
					lst_move.append("L")
					lst_move.append("U")
					print("U'\nL\nU")
				# ----------------------------------------------
			#
			#--------------------------------------------------#
	
			#--------------------------------------------------#
			# 				bad edge sur down
			elif (p[0] == 5 and p[1] == 1 and p[2] == 0) or (p[0] == 4 and p[1] == 2 and p[2] == 1):
				if [5, 0, 1] not in pos and [0, 2, 1] not in pos:
					m.move_D(cube, True)
					lst_move.append("D")
					print("D")
				elif [0,1,0] not in pos and [4,1,2] not in pos:
					m.move_L(cube, False)
					lst_move.append("L'")
					print("L'")
			elif (p[0] == 5 and p[1] == 1 and p[2] == 2) or (p[0] == 1 and p[1] == 2 and p[2] == 1):
				if [5, 0, 1] not in pos and [0, 2, 1] not in pos:
					m.move_D(cube, False)
					lst_move.append("D'")
					print("D'")
				elif [0,1,2] not in pos and [1,1,0] not in pos:
					m.move_R(cube, True)
					lst_move.append("R")
					print("R")
			elif (p[0] == 5 and p[1] == 2 and p[2] == 1) or (p[0] == 3 and p[1] == 2 and p[2] == 1):
				if [5, 0, 1] not in pos and [0, 2, 1] not in pos:
					m.move_D(cube, True)
					m.move_D(cube, True)
					lst_move.append("D2")
					print("D2")
				elif [2, 2, 1] not in pos and [0, 0, 1] not in pos:
					m.move_B(cube, True)
					m.move_B(cube, True)
					lst_move.append("B2")
					m.move_D(cube, True)
					m.move_D(cube, True)
					lst_move.append("D2")
					print("B2\nD2")
				# ----------------------------------------------
				elif [0,1,2] not in pos and [1,1,0] not in pos:
					m.move_D(cube, False)
					m.move_R(cube, True)
					m.move_D(cube, True)
					lst_move.append("D'")
					lst_move.append("R")
					lst_move.append("D")
					print("D'\nR\nD")
				elif [0,1,0] not in pos and [4,1,2] not in pos:
					m.move_D(cube, True)
					m.move_L(cube, False)
					m.move_D(cube, False)
					lst_move.append("D")
					lst_move.append("L'")
					lst_move.append("D'")
					print("D\nL'\nD'")
				# ----------------------------------------------
			#
			#--------------------------------------------------#
		elif fb_prio == "B":
			while i < len(pos):
				if ((pos[i][0] == 3) or (pos[i][0] == 4 and pos[i][1] == 1 and pos[i][2] == 0) \
					or (pos[i][0] == 2 and pos[i][1] == 0 and pos[i][2] == 1) or \
					(pos[i][0] == 1 and pos[i][1] == 1 and pos[i][2] == 2) or \
					(pos[i][0] == 5 and pos[i][1] == 2 and pos[i][2] == 1)):
					i += 1
				else:
					p = pos[i]
					i = 0
					break
			#--------------------------------------------------#
			# 				bad edge sur left
			if not p:
				break
			if (p[0] == 5 and p[1] == 1 and p[2] == 0) or (p[0] == 4 and p[1] == 2 and p[2] == 1):
				if [3,1,2] not in pos and [4,1,0] not in pos:
					m.move_L(cube, True)
					lst_move.append("L")
					print("L")
				elif [0,2,1] not in pos and [3,2,1] not in pos:
					m.move_D(cube, False)
					lst_move.append("D'")
					print("D'")
			elif (p[0] == 4 and p[1] == 0 and p[2] == 1) or (p[0] == 2 and p[1] == 1 and p[2] == 0):
				if [3,1,2] not in pos and [4,1,0] not in pos:
					m.move_L(cube, False)
					lst_move.append("L'")
					print("L'")
				elif [2,0,1] not in pos and [3,0,1] not in pos:
					m.move_U(cube, True)
					lst_move.append("U")
					print("U")
			elif (p[0] == 4 and p[1] == 1 and p[2] == 2) or (p[0] == 0 and p[1] == 1 and p[2] == 0):
				if [3,1,2] not in pos and [4,1,0] not in pos:
					m.move_L(cube, True)
					m.move_L(cube, True)
					lst_move.append("L2")
					print("L2")
				elif [1, 1, 2] not in pos and [3, 1, 0] not in pos:
					m.move_F(cube, True)
					m.move_F(cube, True)
					lst_move.append("F2")
					m.move_R(cube, True)
					m.move_R(cube, True)
					lst_move.append("R2")
					print("F2\nR2")
				# ----------------------------------------------
				elif [2,0,1] not in pos and [3,0,1] not in pos:
					m.move_L(cube, False)
					m.move_U(cube, True)
					m.move_L(cube, True)
					lst_move.append("L'")
					lst_move.append("U")
					lst_move.append("L")
					print("L'\nU\nL")
				elif [5,2,1] not in pos and [3,2,1] not in pos:
					m.move_L(cube, True)
					m.move_D(cube, False)
					m.move_L(cube, False)
					lst_move.append("L")
					lst_move.append("D'")
					lst_move.append("L'")
					print("L\nD'\nL'")
				# ----------------------------------------------
			#
			#--------------------------------------------------#

			#--------------------------------------------------#
			# 				bad edge sur right
			elif (p[0] == 2 and p[1] == 1 and p[2] == 2) or (p[0] == 1 and p[1] == 0 and p[2] == 1):
				if [1, 1, 2] not in pos and [3, 1, 0] not in pos:
					m.move_R(cube, True)
					lst_move.append("R")
					print("R")
				elif [3,0,1] not in pos and [2,0,1] not in pos:
					m.move_U(cube, False)
					lst_move.append("U'")
					print("U'")
			elif (p[0] == 1 and p[1] == 2 and p[2] == 1) or (p[0] == 5 and p[1] == 1 and p[2] == 2):
				if [1, 1, 2] not in pos and [3, 1, 0] not in pos:
					m.move_R(cube, False)
					lst_move.append("R'")
					print("R'")
				elif [5,2,1] not in pos and [3,2,1] not in pos:
					m.move_D(cube, True)
					lst_move.append("D")
					print("D")
			elif (p[0] == 0 and p[1] == 1 and p[2] == 2) or (p[0] == 1 and p[1] == 1 and p[2] == 0):
				if [1, 1, 2] not in pos and [3, 1, 0] not in pos:
					m.move_R(cube, True)
					m.move_R(cube, True)
					lst_move.append("R2")
					print("R2")
				elif [3,1,2] not in pos and [4,1,0] not in pos:
					m.move_F(cube, True)
					m.move_F(cube, True)
					lst_move.append("F2")
					m.move_L(cube, True)
					m.move_L(cube, True)
					lst_move.append("L2")
					print("F2\nL2")
				# ----------------------------------------------
				elif [2,0,1] not in pos and [3,0,1] not in pos:
					m.move_R(cube, False)
					m.move_U(cube, False)
					m.move_R(cube, True)
					lst_move.append("R'")
					lst_move.append("U'")
					lst_move.append("R")
					print("R'\nU'\nR")
				elif [5,2,1] not in pos and [3,2,1] not in pos:
					m.move_R(cube, True)
					m.move_D(cube, True)
					m.move_R(cube, False)
					lst_move.append("R")
					lst_move.append("D")
					lst_move.append("R'")
					print("R\nD\nR'")
				# ----------------------------------------------
			#
			#--------------------------------------------------#

			#--------------------------------------------------#
			# 				bad edge sur up
			elif (p[0] == 4 and p[1] == 0 and p[2] == 1) or (p[0] == 2 and p[1] == 1 and p[2] == 0):
				if [2, 0, 1] not in pos and [3, 0, 1] not in pos:
					m.move_U(cube, True)
					lst_move.append("U")
					print("U")
				elif [4,1,0] not in pos and [3,1,2] not in pos:
					m.move_L(cube, False)
					lst_move.append("L'")
					print("L'")
			elif (p[0] == 1 and p[1] == 0 and p[2] == 1) or (p[0] == 2 and p[1] == 1 and p[1] == 2):
				if [2, 0, 1] not in pos and [3, 0, 1] not in pos:
					m.move_U(cube, False)
					lst_move.append("U'")
					print("U'")
				elif [1,1,2] not in pos and [3,1,0] not in pos:
					m.move_R(cube, True)
					lst_move.append("R")
					print("R")
			elif (p[0] == 2 and p[1] == 2 and p[2] == 1) or (p[0] == 0 and p[1] == 0 and p[2] == 1):
				if [2, 0, 1] not in pos and [3, 0, 1] not in pos:
					m.move_U(cube, True)
					m.move_U(cube, True)
					lst_move.append("U2")
					print("U2")
				elif [5, 2, 1] not in pos and [3, 2, 1] not in pos:
					m.move_F(cube, True)
					m.move_F(cube, True)
					lst_move.append("F2")
					m.move_D(cube, True)
					m.move_D(cube, True)
					lst_move.append("D2")
					print("F2\nD2")
				# ----------------------------------------------
				elif [4,1,0] not in pos and [3,1,2] not in pos:
					m.move_U(cube, True)
					m.move_L(cube, False)
					m.move_U(cube, False)
					lst_move.append("U")
					lst_move.append("L'")
					lst_move.append("U'")
					print("U\nL'\nU'")
				elif [1,2,2] not in pos and [3,1,0] not in pos:
					m.move_U(cube, False)
					m.move_R(cube, True)
					m.move_U(cube, True)
					lst_move.append("U'")
					lst_move.append("R")
					lst_move.append("U")
					print("U'\nR\nU")
				# ----------------------------------------------
			#
			#--------------------------------------------------#
	
			#--------------------------------------------------#
			# 				bad edge sur down
			elif (p[0] == 1 and p[1] == 2 and p[2] == 1) or (p[0] == 5 and p[1] == 1 and p[2] == 2):
				if [5, 2, 1] not in pos and [3, 2, 1] not in pos:
					m.move_D(cube, True)
					lst_move.append("D")
					print("D")
				elif [1,1,2] not in pos and [3,1,0] not in pos:
					m.move_R(cube, False)
					lst_move.append("R'")
					print("R'")
			elif (p[0] == 5 and p[1] == 1 and p[2] == 0) or (p[0] == 4 and p[1] == 2 and p[2] == 1):
				if [5, 2, 1] not in pos and [3, 2, 1] not in pos:
					m.move_D(cube, False)
					lst_move.append("D'")
					print("D'")
				elif [4,1,0] not in pos and [3,1,2] not in pos:
					m.move_L(cube, False)
					lst_move.append("L'")
					print("L'")
			elif (p[0] == 0 and p[1] == 2 and p[2] == 1) or (p[0] == 5 and p[1] == 0 and p[2] == 1):
				if [5, 2, 1] not in pos and [3, 2, 1] not in pos:
					m.move_D(cube, True)
					m.move_D(cube, True)
					lst_move.append("D2")
					print("D2")
				elif [2, 0, 1] not in pos and [3, 0, 1] not in pos:
					m.move_F(cube, True)
					m.move_F(cube, True)
					lst_move.append("F2")
					m.move_U(cube, True)
					m.move_U(cube, True)
					lst_move.append("U2")
					print("F2\nU2")
				# ----------------------------------------------
				elif [4,1,0] not in pos and [3,1,2] not in pos:
					m.move_D(cube, False)
					m.move_L(cube, True)
					m.move_D(cube, True)
					lst_move.append("D'")
					lst_move.append("L")
					lst_move.append("D")
					print("D'\nL\nD")
				elif [1,2,2] not in pos and [3,1,0] not in pos:
					print(p)
					m.move_D(cube, True)
					m.move_R(cube, False)
					m.move_D(cube, False)
					lst_move.append("D")
					lst_move.append("R'")
					lst_move.append("D'")
					print("D\nR'\nD'")
				# ----------------------------------------------
		pos = hta.edge_o_detection(cube)
		p.clear()
		if (utils.Do_I_move(pos, fb_prio)):
			break
		max_ += 1
		if max_ >= 20:
			break
	m.move_F(cube, True) if fb_prio == "F" else m.move_B(cube, True)
	lst_move.append("F") if fb_prio == "F" else lst_move.append("B")
	c.print_cube(cube)
	return cube, lst_move
