import move as m
import cube as c
import visual as visu
import utils
import hta

def	edge_o_two(cube, pos):
	lst_move = []
	nb_mooves = []
	#for p in pos:
		#select_move_lst, nb_moove = utils.select_best_move_f_b(cube, p)
		#lst_move.append(select_move_lst) ; nb_mooves.append(nb_moove)
	return cube

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
					print("BONSOIR ", p)
					continue # ?
			#--------------------------------------------------#
			# 				bad edge sur left
			elif [0,1,0] not in pos or [4,1,2] not in pos:
				print("FL is clear")
				if (p[0] == 4 and p[1] == 0 and p[2] == 1) or (p[0] == 2 and p[1] == 1 and p[2] == 0):
					m.move_L(cube, True)
					lst_move.append("L")
					print("L")
				if (p[0] == 4 and p[1] == 2 and p[2] == 1) or (p[0] == 5 and p[1] == 1 and p[2] == 0):
					m.move_L(cube, False)
					lst_move.append("L'")
					print("L'")
				if (p[0] == 4 and p[1] == 1 and p[2] == 0) or (p[0] == 3 and p[1] == 1 and p[2] == 2):
					m.move_L(cube, True)
					m.move_L(cube, True)
					lst_move.append("L2")
					print("L2")
			#
			#--------------------------------------------------#

			#--------------------------------------------------#
			# 				bad edge sur right
			elif [0, 1, 2] not in pos or [1, 1, 0] not in pos:
				print("FR is clear")
				if (p[0] == 1 and p[1] == 2 and p[2] == 1) or (p[0] == 5 and p[1] == 1 and p[2] == 2):
					m.move_R(cube, True)
					lst_move.append("R")
					print("R")
				if (p[0] == 1 and p[1] == 0 and p[2] == 1) or (p[0] == 2 and p[1] == 1 and p[2] == 2):
					m.move_R(cube, False)
					lst_move.append("R'")
					print("R'")
				if (p[0] == 1 and p[1] == 1 and p[2] == 2) or (p[0] == 3 and p[1] == 1 and p[2] == 0):
					m.move_R(cube, True)
					m.move_R(cube, True)
					lst_move.append("R2")
					print("R2")
			#
			#--------------------------------------------------#

			#--------------------------------------------------#
			# 				bad edge sur up
			elif [2, 2, 1] not in pos or [0, 0, 1] not in pos:
				print("UF is clear")
				if (p[0] == 2 and p[1] == 1 and p[2] == 2) or (p[0] == 1 and p[1] == 0 and p[2] == 1):
					m.move_U(cube, True)
					lst_move.append("U")
					print("U")
				if (p[0] == 2 and p[1] == 1 and p[2] == 0) or (p[0] == 4 and p[1] == 0 and p[1] == 1):
					m.move_U(cube, False)
					lst_move.append("U'")
					print("U'")
				if (p[0] == 2 and p[1] == 0 and p[2] == 1) or (p[0] == 3 and p[1] == 0 and p[2] == 1):
					m.move_U(cube, True)
					m.move_U(cube, True)
					lst_move.append("U2")
					print("U2")
			#
			#--------------------------------------------------#
	
			#--------------------------------------------------#
			# 				bad edge sur down
			elif [5, 0, 1] not in pos or [0, 2, 1] not in pos:
				print("DF is clear")
				if (p[0] == 5 and p[1] == 1 and p[2] == 0) or (p[0] == 4 and p[1] == 2 and p[2] == 1):
					m.move_D(cube, True)
					lst_move.append("D")
					print("D")
				if (p[0] == 5 and p[1] == 1 and p[2] == 2) or (p[0] == 1 and p[1] == 2 and p[2] == 1):
					m.move_D(cube, False)
					lst_move.append("D'")
					print("D'")
				if (p[0] == 5 and p[1] == 2 and p[2] == 1) or (p[0] == 3 and p[1] == 2 and p[2] == 1):
					m.move_D(cube, True)
					m.move_D(cube, True)
					lst_move.append("D2")
					print("D2")
			#
			#--------------------------------------------------#
	
		elif fb_prio == "B":
			if ((p[0] == 3) or (p[0] == 4 and p[1] == 1 and p[2] == 0) \
				or (p[0] == 2 and p[1] == 0 and p[2] == 1) or \
				(p[0] == 1 and p[1] == 1 and p[2] == 2) or \
				(p[0] == 5 and p[1] == 2 and p[2] == 1)):
					print("BONSOIR ", p)
					continue
			#--------------------------------------------------#
			# 				bad edge sur left
			if [3,1,2] not in pos or [4,1,0] not in pos:
				print("FL is clear")
				if (p[0] == 5 and p[1] == 1 and p[2] == 0) or (p[0] == 4 and p[1] == 2 and p[2] == 1):
					m.move_L(cube, True)
					lst_move.append("L")
					print("L")
				if (p[0] == 4 and p[1] == 0 and p[2] == 1) or (p[0] == 2 and p[1] == 1 and p[2] == 0):
					m.move_L(cube, False)
					lst_move.append("L'")
					print("L'")
				if (p[0] == 4 and p[1] == 1 and p[2] == 2) or (p[0] == 0 and p[1] == 1 and p[2] == 0):
					m.move_L(cube, True)
					m.move_L(cube, True)
					lst_move.append("L2")
					print("L2")
			#
			#--------------------------------------------------#

			#--------------------------------------------------#
			# 				bad edge sur right
			elif [1, 1, 2] not in pos or [3, 1, 0] not in pos:
				print("FR is clear")
				if (p[0] == 2 and p[1] == 1 and p[2] == 2) or (p[0] == 1 and p[1] == 0 and p[2] == 1):
					m.move_R(cube, True)
					lst_move.append("R")
					print("R")
				if (p[0] == 1 and p[1] == 2 and p[2] == 1) or (p[0] == 5 and p[1] == 1 and p[2] == 2):
					m.move_R(cube, False)
					lst_move.append("R'")
					print("R'")
				if (p[0] == 0 and p[1] == 1 and p[2] == 2) or (p[0] == 1 and p[1] == 1 and p[2] == 0):
					m.move_R(cube, True)
					m.move_R(cube, True)
					lst_move.append("R2")
					print("R2")
			#
			#--------------------------------------------------#

			#--------------------------------------------------#
			# 				bad edge sur up
			elif [2, 0, 1] not in pos or [3, 0, 1] not in pos:
				print("UF is clear")
				if (p[0] == 4 and p[1] == 0 and p[2] == 1) or (p[0] == 2 and p[1] == 1 and p[2] == 0):
					m.move_U(cube, True)
					lst_move.append("U")
					print("U")
				if (p[0] == 1 and p[1] == 0 and p[2] == 1) or (p[0] == 2 and p[1] == 1 and p[1] == 2):
					m.move_U(cube, False)
					lst_move.append("U'")
					print("U'")
				if (p[0] == 2 and p[1] == 2 and p[2] == 1) or (p[0] == 0 and p[1] == 0 and p[2] == 1):
					m.move_U(cube, True)
					m.move_U(cube, True)
					lst_move.append("U2")
					print("U2")
			#
			#--------------------------------------------------#
	
			#--------------------------------------------------#
			# 				bad edge sur down
			elif [5, 2, 1] not in pos or [3, 2, 1] not in pos:
				print("DF is clear")
				if (p[0] == 1 and p[1] == 2 and p[2] == 1) or (p[0] == 5 and p[1] == 1 and p[2] == 2):
					m.move_D(cube, True)
					lst_move.append("D")
					print("D")
				if (p[0] == 5 and p[1] == 1 and p[2] == 0) or (p[0] == 4 and p[1] == 2 and p[2] == 1):
					m.move_D(cube, False)
					lst_move.append("D'")
					print("D'")
				if (p[0] == 0 and p[1] == 2 and p[2] == 1) or (p[0] == 5 and p[1] == 0 and p[2] == 1):
					m.move_D(cube, True)
					m.move_D(cube, True)
					lst_move.append("D2")
					print("D2")
		pos = hta.edge_o_detection(cube)
	m.move_F(cube, True) if fb_prio == "F" else m.move_B(cube, True)
	lst_move.append("F") if fb_prio == "F" else lst_move.append("B")
	c.print_cube(cube)
	return cube
