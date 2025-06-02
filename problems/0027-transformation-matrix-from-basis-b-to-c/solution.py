import numpy as np
import math

def transform_basis(B: list[list[int]], C: list[list[int]]) -> list[list[float]]:
  b_np = np.array(B)
  c_np = np.array(C)

  return np.linalg.inv(c_np).dot(b_np)