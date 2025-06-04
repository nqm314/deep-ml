import numpy as np

def divide_on_feature(X, feature_i, threshold):
	# Your code here
  subset_1, subset_2 = [], []
  for sample in X:
    if sample[feature_i] >= threshold:
      subset_1.append(sample)
    else: subset_2.append(sample)

  return subset_1, subset_2