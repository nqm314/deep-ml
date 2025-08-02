import numpy as np

def compressed_col_sparse_matrix(dense_matrix):
  dense_matrix = np.array(dense_matrix).T
  values_arr, col_indices_arr, row_pointer_arr = [], [], [0]
  for row in dense_matrix:
    num_non_zero_ele = 0
    for index, ele in enumerate(row):
      if ele != 0:
        values_arr.append(ele)
        col_indices_arr.append(index)
        num_non_zero_ele += 1
    row_pointer_arr.append(row_pointer_arr[-1] + num_non_zero_ele)

  return values_arr, col_indices_arr, row_pointer_arr
