import numpy as np

def accuracy_score(y_true, y_pred):
	# Your code here
  sum_corrected = 0
  for i in range(len(y_true)):
    sum_corrected += y_true[i] == y_pred[i]
  
  return sum_corrected / len(y_true)