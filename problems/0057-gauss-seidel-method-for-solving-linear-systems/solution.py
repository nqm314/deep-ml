import numpy as np

def gauss_seidel(A, b, n, x_ini=None):
  if not x_ini:
    x_ini = np.zeros(A.shape[1])
  
  for _ in range(n):
    for i in range(A.shape[0]):
      x_ini[i] = (1/A[i][i]) * (b[i] - np.sum(A[i][:i] * x_ini[:i]) - np.sum(A[i][i+1:] * x_ini[i+1:]))

  return x_ini