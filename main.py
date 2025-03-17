import math
import argparse
from collections import Counter

class ImproperVectorLength(Exception):
    "Cannot operate on vectors of different length"
    pass

class DistClass:
    def __init__(self, distance, classificator):
        self.distance = distance
        self.classificator = classificator

def euclidean_distance(vec_a, vec_b):
    if len(vec_a) != len(vec_b):
        raise ImproperVectorLength("Vector lengths do not match")
    return math.sqrt(sum((float(a) - float(b))**2 for a, b in zip(vec_a, vec_b)))

def calc_distances(train_data, test_example):
    return [DistClass(euclidean_distance(vec[:-1], test_example), vec[-1]) for vec in train_data]

def classify(k, distances):
    nearest_classes = [x.classificator for x in sorted(distances, key=lambda x: x.distance)[:k]]
    return Counter(nearest_classes).most_common(1)[0][0]

def load_data(filename):
    with open(filename, 'r') as file:
        return [
            [float(x) for x in line.strip().split(',')[1:-1]] + [line.strip().split(',')[-1]]
            for line in file.readlines()
        ]

def knn_classifier(train_file, test_file, k):
    train_data = load_data(train_file)
    test_data = load_data(test_file)
    
    correct = 0
    total = len(test_data)
    
    for test_example in test_data:
        expected = test_example[-1]
        predicted = classify(k, calc_distances(train_data, test_example[:-1]))
        if predicted == expected:
            correct += 1
        print(f"EXPECTED: {expected} | PREDICTED: {predicted}")
    
    accuracy = (correct / total) * 100
    print(f"Total Accuracy: {accuracy:.2f}%")

def main():
    parser = argparse.ArgumentParser(description="k-NN Classifier")
    parser.add_argument("-l", "--learndata", required=True, help="path to training data file")
    parser.add_argument("-t", "--testdata", required=True, help="path to test data file")
    parser.add_argument("-k", type=int, default=3, help="Number of neighbors (default: 3)")
    
    args = parser.parse_args()
    knn_classifier(args.learndata, args.testdata, args.k)

if __name__ == "__main__":
    main()
