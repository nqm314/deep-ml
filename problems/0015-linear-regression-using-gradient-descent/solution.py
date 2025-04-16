import numpy as np
def linear_regression_gradient_descent(X: np.ndarray, y: np.ndarray, alpha: float, iterations: int) -> np.ndarray:
	# Your code here, make sure to round
	m, n = X.shape
	theta = np.zeros(n)

    for _ in range(iterations):
        # compute the hypothesis function
        h = X.dot(theta)

        # compute the error
        error = h - y

        # compute the gradient
        grad = alpha * (1 / m) * error.dot(X)

        # update theta
        theta = theta - grad

	return theta