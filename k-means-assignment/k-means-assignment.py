import numpy as np 

def k_means_assignment(points: list, centroids: list) -> list:
    """
    Returns the nearest-centroid index for every point.
    """
    nearest_centroid = []
    points = np.array(points)
    centroids = np.array(centroids)

    for point in points:
        min_dis = float("inf")
        centroid_idx = -1

        for i, centroid in enumerate(centroids):
            dis = np.sqrt(np.dot(point - centroid, point - centroid))

            if dis < min_dis:
                min_dis = dis
                centroid_idx = i

        nearest_centroid.append(centroid_idx)

    return nearest_centroid