def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
	rows = len(a)
	cols = len(a[0])
	res = [[None] * rows for _ in range(cols)]
	for col in range(cols):
		for row in range(rows):
			res[col][row] = a[row][col]
	
	return res