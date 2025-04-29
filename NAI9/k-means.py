import random

def k_means_data_wrapper(data):
    return [x[:-1] for x in data]

def load_data(filename):
    with open(filename, 'r') as file:
        return [
            [float(x) for x in line.strip().split(',')[1:-1]] + [line.strip().split(',')[-1]]
            for line in file.readlines()
        ]

def calc_centroid(x_cluster : list[list[float]]) -> list[float]]:
    return [sum([x[i] for x in x_cluster])/len(x_cluster) for i in range(0,len(x_cluster[0]))]

def k_means(k, dataset : list) -> None:
    # get initial centroids
    init_centroids = [random.choice(dataset) for _ in range(0,k)]
    print(init_centroids)


k_means(10, dataset=k_means_data_wrapper(load_data("iris.data")))

print(calc_centroid([[4,8,4,3],[4,6,3,6],[7,7,2,3]]))