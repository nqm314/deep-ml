def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
	# Your code here
	num_of_features, num_of_observations = len(vectors), len(vectors[0])

	means = [sum(features)/num_of_observations for features in vectors]

	covariance_matrix = [[0 for _ in range(num_of_features)] for _ in range(num_of_features)] 

	for i in range(num_of_features):
		for j in range(num_of_features):
			sum_product = 0
			for k in range(num_of_observations):
				sum_product += (vectors[i][k] - means[i]) * (vectors[j][k] - means[j])
		
			covariance_matrix[i][j] += sum_product/(num_of_observations - 1) 

	return covariance_matrix