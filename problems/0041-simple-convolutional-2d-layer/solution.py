import numpy as np
import math

def conv(matrix: np.ndarray, kernel: np.nanprod):
	if matrix.shape != kernel.shape:
		print("Mismatched shape.")
	
	sum = 0
	for i in range(matrix.shape[0]):
		for j in range(matrix.shape[1]):
			sum += matrix[i, j] * kernel[i, j]
		
	return sum

def simple_conv2d(input_matrix: np.ndarray, kernel: np.ndarray, padding: int, stride: int):
	input_height, input_width = input_matrix.shape
	# print(input_height, input_width)
	kernel_height, kernel_width = kernel.shape
	# print(kernel_height, kernel_width)

	# Your code here
	padded_input_matrix = np.zeros((int(input_matrix.shape[0]) + padding*2, int(input_matrix.shape[1]) + padding*2))
	if padding > 0:
		padded_input_matrix[padding:-padding, padding:-padding] = input_matrix	
	else:
		padded_input_matrix = input_matrix

	# print(padded_input_matrix)
 
	output_height = math.floor((input_height - kernel_height + 2 * padding) / stride) + 1
	output_width = math.floor((input_width - ker