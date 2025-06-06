import numpy as np

def to_categorical(x, n_col=None):
	# Your code here
  num_unique_vals = len(np.unique(x))
  num_cols = n_col if n_col else num_unique_vals
  one_hot_encoded_res = []
  for i in range(x.shape[0]):
    one_hot_encoded_row = []
    for _ in range(num_cols):
        one_hot_encoded_row.append(0)
    one_hot_encoded_row[x[i]] = 1

    one_hot_encoded_res.append(one_hot_encoded_row)
  
  return one_hot_encoded_res