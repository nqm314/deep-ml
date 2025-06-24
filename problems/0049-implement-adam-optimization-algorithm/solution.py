import numpy as np

def adam_optimizer(f, grad, x0, learning_rate=0.001, beta1=0.9, beta2=0.999, epsilon=1e-8, num_iterations=10):
	# Your code here
  m, v = 0, 0
  for i in range(num_iterations):
    m = beta1 * m + (1 - beta1) * grad(x0)
    v = beta2 * v + (1 - beta2) * grad(x0) ** 2
    # print(m, v)
    m_corrected = m / (1 - beta1 ** (i+1))
    v_corrected = v / (1 - beta2 ** (i+1))
    # print(m_corrected, v_corrected)

    x0 = x0 - learning_rate * m_corrected / (v_corrected ** (1/2) + epsilon)

  return x0