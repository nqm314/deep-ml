import numpy as np
from functools import reduce

def gini_impurity(y):
  """
	Calculate Gini Impurity for a list of class labels.

	:param y: List of class labels
	:return: Gini Impurity rounded to three decimal places
	"""
  classes = set(y)
  freq = [0] * len(classes)
  for i in range(len(y)):
    freq[y[i]] = freq[y[i]] + 1

  # print(classes)
  val = 0
  for i in range(len(freq)):
    prob = freq[i] / len(y)
    val += prob * (1 - prob)
  
  return round(val,3)