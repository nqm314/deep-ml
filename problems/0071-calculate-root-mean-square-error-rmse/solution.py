import numpy as np

def rmse(y_true, y_pred):
	# Write your code here
  if len(y_true) != len(y_pred):
    return -1
  elif len(y_true) == 0 or len(y_pred) == 0:
    return -1

  rmse_res = np.sqrt(np.mean((y_true - y_pred)**2))
  
  return round(rmse_res,3)