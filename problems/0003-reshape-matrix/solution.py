import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method
	#1. Check if new_shape is compatible
	rows, cols = len(a), len(a[0])
	new_rows, new_cols = new_shape
	if rows*cols != new_rows*new_cols:
		print('Incompatible shape')

	#2. Flatten the original matrix
	flat_matrix = []
	for row in range(rows):
		for col in range(cols):
			flat_matrix.append(a[row][col])

	#3. Build the reshaped matrix
	reshaped_matrix = []
	index = 0
	for row in range(new_rows):
		reshaped_row = []
		for col in range(new_cols):
			reshaped_row.append(flat_matrix[index]) 
			index += 1
		reshaped_matrix.append(reshaped_row)
	
	return reshaped_matrix