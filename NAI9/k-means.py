import random
import math
from collections import Counter

def k_means_data_wrapper(data):
    return [x[:-1] for x in data]

def load_data(filename):
    with open(filename, 'r') as file:
        return [
            [float(x) for x in line.strip().split(',')[1:-1]] + [line.strip().split(',')[-1]]
            for line in file.readlines() if line.strip()
        ]

def calc_centroid(x_cluster: list[list[float]]) -> list[float]:
    return [sum(x[i] for x in x_cluster) / len(x_cluster) for i in range(len(x_cluster[0]))]

def euclidean_distance(a, b):
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))

def k_means(k, dataset):
    centroids = random.sample(dataset, k)
    iteration = 0
    while True:
        iteration += 1
        clusters = [[] for _ in range(k)]
        for point in dataset:
            distances = [euclidean_distance(point[:-1], c) for c in centroids]
            min_idx = distances.index(min(distances))
            clusters[min_idx].append(point)
        total = sum(
            euclidean_distance(point[:-1], centroids[i])
            for i, cluster in enumerate(clusters)
            for point in cluster
        )
        print(f"ITER NUM {iteration}: {total:.2f}")
        new_centroids = []
        for cluster in clusters:
            if cluster:
                new_centroids.append(calc_centroid([x[:-1] for x in cluster]))
            else:
                new_centroids.append(random.choice(dataset))
        if all(
            all(abs(n - o) < 1e-6 for n, o in zip(nc, oc))
            for nc, oc in zip(new_centroids, centroids)
        ):
            break
        centroids = new_centroids
    return clusters

if __name__ == "__main__":
    k = 3
    clusters = k_means(k, load_data("iris.data"))
    for i, cluster in enumerate(clusters):
        class_counter = Counter([x[-1] for x in cluster])
        print(class_counter)
        print(f"GROUP NUM:  {i+1} | CLASS NAME: {max(class_counter)}")
        for point in cluster:
            print(point)
