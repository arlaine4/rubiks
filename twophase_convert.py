import cube as c
import twophase as tp
import twophase_enum as tpe

def get_corners_pos(c, corners):
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
	return corners

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
		if current == old_c:
			return(k)

def get_UDSlice_coordinate(edges):
	enum = {0 : "UR", 1 : "UF", 2 : "UL", 3 : "UB", 4 : "DR", 5 : "DF", 6 : "DL", 7 : "DB", 8 : "FR", 9 : "FL", 10 : "BL", 11 : "BR"}
	tmp = []
	UDSlice = 0
	for i in range(len(edges)):
		k = 0
		tmp.clear
		if i >= 0 and i < 4:
			tmp.append(edges[enum[0]])
			tmp.append(edges[enum[1]])
			tmp.append(edges[enum[2]])
			tmp.append(edges[enum[3]])
			k = get_k(i, tmp)
			UDSlice += C(i, k)
		elif i >= 4 and i < 8:
			tmp.append(edges[enum[4]])
			tmp.append(edges[enum[5]])
			tmp.append(edges[enum[6]])
			tmp.append(edges[enum[7]])
			k = get_k(i, tmp)
			UDSlice += C(i, k)
		elif i >= 8 and i <= 11:
			tmp.append(edges[enum[8]])
			tmp.append(edges[enum[9]])
			tmp.append(edges[enum[10]])
			tmp.append(edges[enum[11]])
			k = get_k(i, tmp)
			UDSlice += C(i, k)
	return 0

def convert(c):
	corners = {"URF" : False, "UFL" : False, "ULB" : False, "UBR" : False, "DFR" : False, "DLF" : False, "DBL" : False, "DRB" : False}
	corners = get_corners_pos(c, corners) # 8 corners
	print(corners)
	edges = {"UR" : False, "UF" : False, "UL" : False, "UB" : False, "DR" : False, "DF" : False, "DL" : False, "DB" : False, "FR" : False, "FL" : False, "BL" : False, "BR" : False}
	edges = get_edges_pos(c, edges) # 12 edges
	print(edges)
	UDSlice = get_UDSlice_coordinate(edges)
