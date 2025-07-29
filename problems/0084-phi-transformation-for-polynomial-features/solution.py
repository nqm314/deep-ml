import numpy as np

def phi_calculate(num: float, degree: int) -> list[float]:
  res = []
  for i in range(degree + 1):
    res.append(num ** i)

  return res

def phi_transform(data: list[float], degree: int) -> list[list[float]]:
  """
	Perform a Phi Transformation to map input features into a higher-dimensional space by generating polynomial features.

	Args:
		data (list[float]): A list of numerical values to transform.
		degree (int): The degree of the polynomial expansion.

	"""
	# Your code here
  res = []
  
  for num in data:
    res.append(phi_calculate(num, degree))

  return res