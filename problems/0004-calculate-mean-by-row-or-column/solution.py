def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	rows, cols = len(matrix), len(matrix[0])

	list_of_means = []
	if mode == 'row':
		for row in range(rows):
			rowSum = 0
			for col in range(cols):
				rowSum += matrix[row][col]

			list_of_means.append(rowSum / cols)		
	else:
		for col in range(cols):
			colSum = 0
			for row in range(rows):
				colSum += matrix[row][col]

			list_of_means.append(colSum / rows)

	return list_of_means