import numpy as np

def make_diagonal(x):
	# Your code here
  n = x.shape[0]
  diag_matrix = []
  for i in range(n):
    diag_matrix_row = []
    for j in range(n):
      diag_matrix_row.append(x[i]) if i == j else diag_matrix_row.append(0)

    diag_matrix.append(diag_matrix_row)

  return diag_matrix 