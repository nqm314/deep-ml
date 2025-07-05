import numpy as np

def dice_score(y_true, y_pred):
	# Write your code here
  TP, FP, FN = 0, 0, 0
  for i in range(len(y_true)):
    TP += y_pred[i] == 1 and y_true[i] == 1
    FP += y_pred[i] == 1 and y_true[i] == 0
    FN += y_pred[i] == 0 and y_true[i] == 1
  
  if (2 * TP + FP + FN) == 0:
    return 0.0
  res = (2 * TP) / (2 * TP + FP + FN)
  return round(res, 3)
