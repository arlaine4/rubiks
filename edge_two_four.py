import move as m
import cube as c
import visual as visu
import utils
import hta

def	edge_o_two(cube, pos):
	lst_moves = []
	nb_mooves = []
	#for p in pos:
		#select_move_lst, nb_moove = utils.select_best_move_f_b(cube, p)
		#lst_move.append(select_move_lst) ; nb_mooves.append(nb_moove)
	return cube, lst_moves

def	edge_o_four(cube, pos):
	lst_move = []
	nb_mooves = []
	fb_prio = utils.front_or_back(pos)
	for p in pos:
		if fb_prio == "F":
			if ((p[0] == 0) or (p[0] == 4 and p[1] == 1 and p[2] == 2) \
				or (p[0] == 2 and p[1] == 2 and p[2] == 1) or \
				(p[0] == 1 and p[1] == 1 and p[2] == 0) or \
				(p[0] == 5 and p[1] == 0 and p[2] == 1)):
					continue
			#--------------------------------------------------#
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
				elif [0,0,1] not in pos and [2,2,1] not in pos:
					m.move_U(cube, True)
					lst_move.append("U")
					print("U")
			elif (p[0] == 1 and p[1] == 0 and p[2] == 1) or (p[0] == 2 and p[1] == 1 and p[2] == 2):
				if [0, 1, 2] not in pos and [1, 1, 0] not in pos:
					m.move_R(cube, False)
					lst_move.append("R'")
					print("R'")
				elif [0,2,1] not in pos and [5,0,1] not in pos:
					m.move_D(cube, False)
					lst_move.append("D'")
					print("D'")
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
			if ((p[0] == 3) or (p[0] == 4 and p[1] == 1 and p[2] == 0) \
				or (p[0] == 2 and p[1] == 0 and p[2] == 1) or \
				(p[0] == 1 and p[1] == 1 and p[2] == 2) or \
				(p[0] == 5 and p[1] == 2 and p[2] == 1)):
					continue
			#--------------------------------------------------#
			# 				bad edge sur left
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
					m.move_D(cube, True)
					m.move_R(cube, False)
					m.move_D(cube, False)
					lst_move.append("D")
					lst_move.append("R'")
					lst_move.append("D'")
					print("D\nR'\nD'")
				# ----------------------------------------------
		pos = hta.edge_o_detection(cube)
	m.move_F(cube, True) if fb_prio == "F" else m.move_B(cube, True)
	lst_move.append("F") if fb_prio == "F" else lst_move.append("B")
	c.print_cube(cube)
	return cube, lst_move
