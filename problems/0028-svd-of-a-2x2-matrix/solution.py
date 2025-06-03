import numpy as np

def svd_2x2(A: np.ndarray) -> tuple:
	# Your code here
    A = np.array(A)
    U, S, V = np.linalg.svd(A)
    return U,S,V