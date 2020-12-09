import cube as c
import twophase_enum as tpe

def sort_corners_names(corners_pos, key, pos):
	if "U" in pos and "R" in pos and "F" in pos:
		corners_pos[key] = "URF"
	if "U" in pos and "F" in pos and "L" in pos:
		corners_pos[key] = "UFL"
	if "U" in pos and "L" in pos and "B" in pos:
		corners_pos[key] = "ULB"
	if "U" in pos and "B" in pos and "R" in pos:
		corners_pos[key] = "UBR"
	if "D" in pos and "F" in pos and "R" in pos:
		corners_pos[key] = "DFR"
	if "D" in pos and "L" in pos and "F" in pos:
		corners_pos[key] = "DLF"
	if "D" in pos and "B" in pos and "L" in pos:
		corners_pos[key] = "DBL"
	if "D" in pos and "R" in pos and "B" in pos:
		corners_pos[key] = "DRB"
	return corners_pos

def get_corners_pos(c, corners):
	corners_pos = {}
	if c.cube[0][0][2] == 0 and c.cube[1][0][0] == 1 and c.cube[2][2][2] == 2:
		corners["URF"] = True
	if c.cube[2][2][0] == 2 and c.cube[0][0][0] == 0 and c.cube[4][0][2] == 4:
		corners["UFL"] = True
	if c.cube[2][0][0] == 2 and c.cube[4][0][0] == 4 and c.cube[3][0][2] == 3:
		corners["ULB"] = True
	if c.cube[2][0][2] == 2 and c.cube[3][0][0] == 3 and c.cube[1][0][2] == 1:
		corners["UBR"] = True
	if c.cube[5][0][2] == 5 and c.cube[0][2][2] == 0 and c.cube[1][2][0] == 1:
		corners["DFR"] = True
	if c.cube[5][0][0] == 5 and c.cube[4][2][2] == 4 and c.cube[0][2][0] == 0:
		corners["DLF"] = True
	if c.cube[5][2][0] == 5 and c.cube[3][2][2] == 3 and c.cube[4][2][0] == 4:
		corners["DBL"] = True
	if c.cube[5][2][2] == 5 and c.cube[1][2][2] == 1 and c.cube[3][2][0] == 3:
		corners["DRB"] = True
	corners_pos["URF"] = str(tpe.intFace(c.cube[0][0][2])) + str(tpe.intFace(c.cube[1][0][0])) + str(tpe.intFace(c.cube[2][2][2]))
	corners_pos["UFL"] = str(tpe.intFace(c.cube[2][2][0])) + str(tpe.intFace(c.cube[0][0][0])) + str(tpe.intFace(c.cube[4][0][2]))
	corners_pos["ULB"] = str(tpe.intFace(c.cube[2][0][0])) + str(tpe.intFace(c.cube[4][0][0])) + str(tpe.intFace(c.cube[3][0][2]))
	corners_pos["UBR"] = str(tpe.intFace(c.cube[2][0][2])) + str(tpe.intFace(c.cube[3][0][0])) + str(tpe.intFace(c.cube[1][0][2]))
	corners_pos["DFR"] = str(tpe.intFace(c.cube[5][0][2])) + str(tpe.intFace(c.cube[0][2][2])) + str(tpe.intFace(c.cube[1][2][0]))
	corners_pos["DLF"] = str(tpe.intFace(c.cube[5][0][0])) + str(tpe.intFace(c.cube[4][2][2])) + str(tpe.intFace(c.cube[0][2][0]))
	corners_pos["DBL"] = str(tpe.intFace(c.cube[5][2][0])) + str(tpe.intFace(c.cube[3][2][2])) + str(tpe.intFace(c.cube[4][2][0]))
	corners_pos["DRB"] = str(tpe.intFace(c.cube[5][2][2])) + str(tpe.intFace(c.cube[1][2][2])) + str(tpe.intFace(c.cube[3][2][0]))
	corners_pos = sort_corners_names(corners_pos, "URF", corners_pos["URF"].replace("intFace.", ""))
	corners_pos = sort_corners_names(corners_pos, "UFL", corners_pos["UFL"].replace("intFace.", ""))
	corners_pos = sort_corners_names(corners_pos, "ULB", corners_pos["ULB"].replace("intFace.", ""))
	corners_pos = sort_corners_names(corners_pos, "UBR", corners_pos["UBR"].replace("intFace.", ""))
	corners_pos = sort_corners_names(corners_pos, "DFR", corners_pos["DFR"].replace("intFace.", ""))
	corners_pos = sort_corners_names(corners_pos, "DLF", corners_pos["DLF"].replace("intFace.", ""))
	corners_pos = sort_corners_names(corners_pos, "DBL", corners_pos["DBL"].replace("intFace.", ""))
	corners_pos = sort_corners_names(corners_pos, "DRB", corners_pos["DRB"].replace("intFace.", ""))
	return corners, corners_pos

def get_edges_pos(c, edges):
	if c.cube[2][1][2] == 2 and c.cube[1][0][1] == 1:
		edges["UR"] = True
	if c.cube[2][2][1] == 2 and c.cube[0][0][1] == 0:
		edges["UF"] = True
	if c.cube[2][1][0] == 2 and c.cube[4][0][1] == 4:
		edges["UL"] = True
	if c.cube[2][0][1] == 2 and c.cube[3][0][1] == 3:
		edges["UB"] = True
	if c.cube[5][1][2] == 5 and c.cube[1][2][1] == 1:
		edges["DR"] = True
	if c.cube[5][0][1] == 5 and c.cube[0][2][1] == 0:
		edges["DF"] = True
	if c.cube[5][1][0] == 5 and c.cube[4][2][1] == 4:
		edges["DL"] = True
	if c.cube[5][2][1] == 5 and c.cube[3][2][1] == 3:
		edges["DB"] = True
	if c.cube[0][1][2] == 0 and c.cube[1][1][0] == 1:
		edges["FR"] = True
	if c.cube[0][1][0] == 0 and c.cube[4][1][2] == 4:
		edges["FL"] = True
	if c.cube[3][1][2] == 3 and c.cube[4][1][0] == 4:
		edges["BL"] = True
	if c.cube[3][1][0] == 3 and c.cube[1][1][2] == 1:
		edges["BR"] = True
	return edges

def c(n, k):
	if n < k:
		return 0
	if k > n // 2:
		k = n - k
	s, i, j = 1, n, 1
	while i != n - k:
		s *= i
		s //= j
		i -= 1
		j += 1
	return s

def get_k(old_c, tmp):
	current = old_c
	k = 0
	if tmp[current]:
		current -= 1
		if current < 0:
			current = 3
		if not tmp[current]:
			k += 1
		else:
			return 0
		current -= 1
		if current < 0:
			current = 3
		if not tmp[current]:
			k += 1
		current -= 1
		if current < 0:
			current = 3
		if not tmp[current]:
			k += 1
		return k
	return 0

def get_UDSlice_coordinate(edges):
	tmp = []
	UDSlice = 0
	for i in range(len(edges)):
		k = 0
		tmp.clear()
		if i >= 0 and i < 4:
			tmp.append(edges["UR"])
			tmp.append(edges["UF"])
			tmp.append(edges["UL"])
			tmp.append(edges["UB"])
			k = get_k(i, tmp)
			UDSlice += c(i, k)
		elif i >= 4 and i < 8:
			tmp.append(edges["DR"])
			tmp.append(edges["DF"])
			tmp.append(edges["DL"])
			tmp.append(edges["DB"])
			k = get_k(i - 4, tmp)
			UDSlice += c(i, k)
		elif i >= 8 and i <= 11:
			tmp.append(edges["FR"])
			tmp.append(edges["FL"])
			tmp.append(edges["BL"])
			tmp.append(edges["BR"])
			k = get_k(i - 8, tmp)
			UDSlice += c(i, k)
	return UDSlice

def get_o(key, value):
	if key == value:
		return 0
	elif key[0] == value[0]:
		return 1
	elif key != value:
		return 2

def get_corners_coord(corners, corners_pos):
	s = 0
	p = 6
	for key in corners_pos:
		o = get_o(key, corners_pos[key])
		if key == "DRB":
			break
		s += (o*3**p)
		p -= 1
	return s

def get_edges_coord(corners):
	return 0

def convert(c):
	corners = {"URF" : False, "UFL" : False, "ULB" : False, "UBR" : False, "DFR" : False, "DLF" : False, "DBL" : False, "DRB" : False}
	corners, corners_pos = get_corners_pos(c, corners) # 8 corners
	corners_coord = get_corners_coord(corners, corners_pos)
	print(corners_coord)
	edges = {"UR" : False, "UF" : False, "UL" : False, "UB" : False, "DR" : False, "DF" : False, "DL" : False, "DB" : False, "FR" : False, "FL" : False, "BL" : False, "BR" : False}
	edges = get_edges_pos(c, edges) # 12 edges
	edges_coord = get_edges_coord(edges)
	print(edges)
	UDSlice = get_UDSlice_coordinate(edges)
	print("UDSlice: ", UDSlice)
	return [corners_coord, edges_coord, UDSlice]

def phase_one(c):
	coord = convert(c)

	return c
