import numpy as np

def rref(matrix):
  matrix = matrix.astype(float)
  n, m = matrix.shape

  left = 0

  for row in range(n):
    if left >= m:
      return matrix

    i = row
    while matrix[i][left] == 0:
      i += 1

      if i >= n:
        i = row
        left += 1

        if left >= m:
          return matrix

    # print(matrix[row], matrix[i])

    temp = matrix[i].copy()
    matrix[i] = matrix[row]
    matrix[row] = temp

    # print(matrix[row], matrix[i])

    pivot = matrix[row][left]
    # print(pivot)

    matrix[row] = [x / pivot for x in matrix[row]]

    # print(matrix)

    for i in range(n):
      if i != row:
        pivot = matrix[i][left]
        matrix[i] = [matrix[i][j] - pivot * matrix[row][j] for j in range(m)]

    # print(matrix)
    left += 1

  return matrix