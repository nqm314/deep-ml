import numpy as np
import math

def sigmoid(z: float) -> float:
	result = 1 / (1 + math.exp(-z))
	return round(result, 4)
 
def derivative_sigmoid(z: float) -> float:
	return round((math.exp(-z) / (1 + math.exp(-z))**2), 4)
 
def train_neuron(features: np.ndarray, labels: np.ndarray, initial_weights: np.ndarray, initial_bias: float, learning_rate: float, epochs: int) -> (np.ndarray, float, list[float]):
	# Your code here
	features = np.array(features)
	labels = np.array(labels)
	initial_weights = np.array(initial_weights)
	updated_weights, updated_bias = initial_weights, initial_bias 
	mse_values = []

	for epoch in range(epochs):
		outputs = features.dot(updated_weights) + updated_bias 
		sigmoid_outputs = np.array([sigmoid(val) for val in outputs])
		error_term = sigmoid_outputs - labels
		mse = np.mean(error_term ** 2)
		mse_values.append(round(mse, 4)) 
		temp = error_term * (np.array([derivative_sigmoid(val) for val in outputs]))
		grad_weights = (2 / len(