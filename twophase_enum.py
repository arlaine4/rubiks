from enum import IntEnum

class Corner(IntEnum):
	"""The names of the corner positions of the cube. Corner URF e.g. has an U(p), a R(ight) and a F(ront) facelet."""
	URF = 0
	UFL = 1
	ULB = 2
	UBR = 3
	DFR = 4
	DLF = 5
	DBL = 6
	DRB = 7

class Edge(IntEnum):
	"""The names of the edge positions of the cube. Edge UR e.g. has an U(p) and R(ight) facelet."""
	UR = 0
	UF = 1
	UL = 2
	UB = 3
	DR = 4
	DF = 5
	DL = 6
	DB = 7
	FR = 8
	FL = 9
	BL = 10
	BR = 11
