import numpy as np

def l1_regularization_gradient_descent(X: np.array, y: np.array, alpha: float = 0.1, learning_rate: float = 0.01, max_iter: int = 1000, tol: float = 1e-4) -> tuple:
  n_samples, n_features = X.shape
#   print(n_samples, n_features)

  weights = np.zeros(n_features)
  bias = 0
  # grad_weights = np.zeros(n_features)
  # Your code here
  for _ in range(max_iter):
    pred = X.dot(weights) + bias
    # print(pred)
    error = pred - y
    grad_weights = (1/n_samples) * (error.dot(X)) + alpha * np.sign(weights)

    grad_bias = (1/n_samples) * np.sum(error)

    weights = weights - learning_rate * grad_weights
    bias = bias - learning_rate * grad_bias

    # print(grad_weights)
    # if np.linalg.norm(grad_weights, ord=1) < tol:
    #   break

    if np.sum(grad_weights ** 2) ** (1/2) < tol: # L1 Norm of a matrix
      break

  return weights, bias