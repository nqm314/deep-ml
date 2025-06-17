import numpy as np

def gradient_descent(X, y, weights, learning_rate, n_iterations, batch_size=1, method='batch'):
	# Your code here
  m, n = X.shape
  if method == 'batch':
    # print(method)
    for _ in range(n_iterations):
      pred = X.dot(weights)
      error = pred - y
      grad = (2/m) * (error.dot(X))
      weights = weights - learning_rate * grad
  elif method == 'stochastic':
    # print(method)
    for _ in range(n_iterations):
      for i in range(m):
        pred = X[i].dot(weights)
        error = pred - y[i]
        grad = 2 * (error * (X[i]))
        weights = weights - learning_rate * grad 
  elif method == 'mini_batch':
    # print(method)
    for _ in range(n_iterations):
      for i in range(0,m,batch_size):
        pred = X[i:i+batch_size].dot(weights)
        # print("Pred: ", pred)
        error = pred - y[i:i+batch_size]
        # print("Error: ", error)
        grad = (2/(batch_size)) * (error.dot(X[i:i+batch_size]))
        # 