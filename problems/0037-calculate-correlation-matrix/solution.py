import numpy as np

def calculate_covariance_matrix(X, Y):
	# Your code here
  if Y is None:
    Y = X
  
  num_of_features, num_of_observations = len(X[0]), len(X)
#   print(num_of_features, num_of_observations)
  
  mean_X = [sum(features)/num_of_observations for features in X.T]
#   print(mean_X)

  mean_Y = [sum(features)/num_of_observations for features in Y.T]
#   print(mean_Y)
  
  covariance_matrix = [[0 for _ in range(num_of_features)] for _ in range(num_of_features)] 
#   print(covariance_matrix)
  
  for i in range(num_of_features):
    for j in range(num_of_features):
      sum_product = 0
      for k in range(num_of_observations):
        sum_product += (X[k][i] - mean_X[i]) * (Y[k][j] - mean_Y[j])
      
      covariance_matrix[i][j] += sum_product/(num_of_observations - 1) 
    #   print(covariance_matrix)
        
  return covariance_matrix

def calculate_correlation_matrix(X, Y=None):
  if Y is None:
    Y = X 

  num_of_features, num_