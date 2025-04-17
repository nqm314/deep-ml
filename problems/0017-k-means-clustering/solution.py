import numpy as np 

def k_means_clustering(points: list[tuple[float, float]], k: int, initial_centroids: list[tuple[float, float]], max_iterations: int) -> list[tuple[float, float]]:
    def compute_euclidean_dist(point: tuple[float, float], centroid: tuple[float, float]) -> float:
        return ((point[0] - centroid[0])**2 + (point[1] - centroid[1])**2) ** (1/2)

    final_centroids = initial_centroids.copy()

    for _ in range(max_iterations):
        clusters = [[] for _ in range(k)]

        for point in points:
            distances = [compute_euclidean_dist(point, centroid) for centroid in final_centroids]
            neares_centroid_idx = distances.index(min(distances))
            clusters[neares_centroid_idx].append(point) 

        new_centroids = []
        for idx, cluster in enumerate(clusters):
            if len(clusters) > 0:
                new_centroid = tuple(np.mean(np.array(cluster).round(4), axis = 0))
                new_centroids.append(ne