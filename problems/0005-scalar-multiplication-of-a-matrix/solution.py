def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	rows, cols = len(matrix), len(matrix[0])
	for row in range(rows):
		for col in range(cols):
			matrix[row][col] *= scalar

	return matrix