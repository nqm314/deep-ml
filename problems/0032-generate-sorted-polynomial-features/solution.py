import numpy as np
from itertools import combinations_with_replacement

def polynomial_features(X, degree):
    # ✏️  Your code here
    n_samples, n_features = X.shape 

    features_poly = [np.ones(n_samples)]

    for i in range(n_features):
      features_poly.append(X[:, i])

    if degree >= 2:
      for deg in range(2, degree + 1):
        for combination_idx in combinations_with_replacement(range(n_features), deg):
          new_poly_features = np.prod(X[:, list(combination_idx)], axis=1)
          features_poly.append(new_poly_features)
    
    return np.sort(np.array(features_poly).T)