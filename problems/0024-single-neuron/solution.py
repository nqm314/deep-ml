import math
import numpy as np

def sigmoid(z: float) -> float:
	result = 1 / (1 + math.exp(-z))
	return result.__round__(4)

def single_neuron_model(features: list[list[float]], labels: list[int], weights: list[float], bias: float) -> (list[float], float):
  features_np = np.array(features)
  labels_np = np.array(labels)
  weights_np = np.array(weights)
  bias_np = np.array(bias)

  probabilities = features_np.dot(weights_np) + bias_np 
  probabilities = [sigmoid(prob) for prob in probabilities]
  sum = 0
  for idx, prob in enumerate(probabilities):
    sum += (prob - labels[idx]) ** 2
  
  mse = sum / len(labels)
  
  return probabilities, mse