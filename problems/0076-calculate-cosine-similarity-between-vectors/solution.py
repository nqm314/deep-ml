import numpy as np

def cosine_similarity(v1, v2):
  # Implement your code here
  dot_prod = v1.dot(v2)
  l1_v1 = np.sqrt(np.sum(v1**2))
  l1_v2 = np.sqrt(np.sum(v2**2))

  return round(dot_prod / (l1_v2 * l1_v1), 3)