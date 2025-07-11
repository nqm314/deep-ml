import numpy as np

def jaccard_index(y_true, y_pred):
	# Write your code here
  intersection, union = 0, 0
  for i in range(len(y_true)):
    intersection += (y_pred[i] == 1 and y_pred[i] == y_true[i])
    union += y_pred[i] == 1 or y_true[i] == 1

  result = intersection / union
  
  return round(result, 3)