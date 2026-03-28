def phi_corr(x: list[int], y: list[int]) -> float:
	"""
	Calculate the Phi coefficient between two binary variables.

	Args:
	x (list[int]): A list of binary values (0 or 1).
	y (list[int]): A list of binary values (0 or 1).

	Returns:
	float: The Phi coefficient rounded to 4 decimal places.
	"""
	# Your code here
	num_00, num_01, num_10, num_11 = 0, 0, 0, 0
	for idx, val in enumerate(x):
		num_00 += (val == 0) and (y[idx] == 0)
		num_01 += (val == 0) and (y[idx] == 1)
		num_10 += (val == 1) and (y[idx] == 0)
		num_11 += (val == 1) and (y[idx] == 1)
	
	val = ((num_00*num_11) - (num_01*num_10)) / (((num_00+num_01)*(num_10+num_11)*(num_00+num_10)*(num_01+num_11))**(1/2))
	return round(val,4)