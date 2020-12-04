import cube as c

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

def get_UDSlice_coordinate(corners, edges):
	return 0

def convert(c):
	corners = {"URF" : False, "UFL" : False, "ULB" : False, "UBR" : False, "DFR" : False, "DLF" : False, "DBL" : False, "DRB" : False}
	corners = get_corners_pos(c, corners)
	print(corners)
	edges = {"UR" : False, "UF" : False, "UL" : False, "UB" : False, "DR" : False, "DF" : False, "DL" : False, "DB" : False, "FR" : False, "FL" : False, "BL" : False, "BR" : False}
	edges = get_edges_pos(c, edges)
	print(edges)
	UDSliceC = get_UDSlice_coordinate(corners, edges)
