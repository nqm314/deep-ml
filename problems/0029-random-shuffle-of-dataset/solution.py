import numpy as np
import math

def shuffle_data(X, y, seed=None):
	# Your code here
  if seed:
    np.random.seed(seed)

  idx = np.arange(X.shape[0])
  np.random.shuffle(idx)
  return X[idx], y[idx]