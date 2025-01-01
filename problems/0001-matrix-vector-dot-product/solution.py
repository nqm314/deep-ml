def matrix_dot_vector(a:list[list[int|float]],b:list[int|float])-> list[int|float]:
	if len(a[0]) != len(b):
		return -1
	
	res_list = []

	for row in range(len(a)):
		value = 0
		for col in range(len(b)):
			value += (a[row][col] * b[col])
		
		res_list.append(value)

	return res_list
