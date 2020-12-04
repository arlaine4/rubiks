
def get_corners_pos(c, corners):
	return corners

def get_edges_pos(c, edges):
	return corners

def convert(c):
	corners = {"URF" : False, "UFL" : False, "ULB" : False, "UBR" : False, "DFR" : False, "DLF" : False, "DBL" : False, "DRB" : False}
	corners = get_corners_pos(c, corners)
	edges = {"UR" : False, "UF" : False, "UL" : False, "UB" : False, "DR" : False, "DF" : False, "DL" : False, "DB" : False, "FR" : False, "FL" : False, "BL" : False, "BR" : False}
	edges = get_edges_pos(c, edges)
