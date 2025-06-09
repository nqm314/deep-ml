import numpy as np

def log_softmax(scores: list) -> np.ndarray:
	# Your code here
  sum_exp = np.sum(np.exp(scores))
  softmax_scores = np.array([np.exp(score) / sum_exp for score in scores]) 
  return np.log(softmax_scores)