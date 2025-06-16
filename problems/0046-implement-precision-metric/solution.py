import numpy as np
def precision(y_true, y_pred):
	# Your code here
  true_positives = 0
  false_positives = 0
  for i in range(len(y_true)):
    true_positives += y_pred[i] == 1 and y_pred[i] == y_true[i]
    false_positives += y_pred[i] == 1 and y_pred[i] != y_true[i]
  
  return true_positives / (true_positives + false_positives)