import numpy as np 
def pca(data: np.ndarray, k: int) -> np.ndarray:
    standardized_data = (data - data.mean(axis=0)) / (data.std(axis=0))

    covarriance_matrix = np.cov(standardized_data, rowvar=False)

    eigenvalues, eigenvectors = np.linalg.eig(covarriance_matrix)
    # print(eigenvalues, eigenvectors)

    sorted_indices = np.argsort(eigenvalues)[::-1] # Returns the indices that would sort an array.
    # print(sorted_indices)

    sorted_eigenvectors = eigenvectors[:, sorted_indices]
    # print(sorted_eigenvectors)

    principal_components = sorted_eigenvectors[:, :k]
    
    return np.round(principal_components, 4)