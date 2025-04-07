import random
import matplotlib.pyplot as plt
import multiprocessing

class ImproperVectorLength(Exception):
    "Cannot operate on vectors of different length"
    pass

def load_data(filename):
    with open(filename, 'r') as file:
        return [
            [float(x) for x in line.strip().split(',')[1:-1]] + [line.strip().split(',')[-1]]
            for line in file.readlines()
        ]

def net(vec_1, weight, theta) -> int:
    return 1 if sum([x * y for x, y in zip(vec_1, weight)]) - theta >= 0 else 0


def delta_weight(old_weight, alpha, expected_out, real_out, x) -> list:
    if len(old_weight) != len(x): raise ImproperVectorLength

    return [j + k for j, k in zip(old_weight, [alpha * (expected_out - real_out) * i for i in x])]

def delta_theta(old_theta, alpha, expected_out, real_out) -> float:
    return old_theta - (alpha * (expected_out - real_out))

def perceptron(learning_rate, epohs, test_data, learn_data,theta=None, starting_weight=None):
    theta = theta if theta is not None else random.random()

    weights = [random.random() if starting_weight is None else starting_weight for _ in range(len(learn_data[0]) - 1)]

    unique_labels = list(set(sample[-1] for sample in learn_data))
    label_map = {label: i for i, label in enumerate(unique_labels)}

    for _ in range(epohs):
        for sample in learn_data:
            x, expected_out = sample[:-1], label_map[sample[-1]]
            real_out = net(x, weights, theta)

            weights = delta_weight(weights, learning_rate, expected_out, real_out, x)
            theta = delta_theta(theta, learning_rate, expected_out, real_out)

    # TEST PART
    correct = 0
    for sample in test_data:
        x, expected_out_label = sample[:-1], sample[-1]
        expected_out = label_map.get(expected_out_label, -1)
        real_out = net(x, weights, theta)

        if real_out == expected_out:
            correct += 1

    accuracy = correct / len(test_data) * 100
    #print(f"ACCURACY: {accuracy:.2f}%")
    #print(f"LABEL MAP: {label_map}")

    return [weights, theta, accuracy]

#weights, theta = perceptron(learning_rate=0.5, epohs=10000, learn_data=load_data("perceptron.test.data"), test_data=load_data("perceptron.data"),starting_weight=0.5)
#print("FINAL WEIGHTS", weights)
#rint("THETA:", theta)


#learn_data = load_data("perceptron.test.data")
#test_data = load_data("perceptron.data")

def run_perceptron(epoch):
    _, _, accuracy = perceptron(learning_rate=0.5, epohs=epoch, learn_data=learn_data, test_data=test_data, theta=0, starting_weight=0.01)
    print(f"EPOCH COUNT: {epoch}, ACCURACY: {accuracy}")
    return epoch, accuracy


if __name__ == "__main__":
    accuracies_epohs = {}
    graph_range = range(10, 10000, 10)

    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        results = pool.map(run_perceptron, graph_range)

    accuracies_epohs = {epoch: acc for epoch, acc in results}

    accuracies = [accuracies_epohs[i] for i in graph_range]

    plt.figure(figsize=(10, 5))

    plt.plot(graph_range, accuracies, marker='o', markersize=3, linestyle='-', linewidth=1, alpha=0.7) 

    plt.xlabel('Epochs', fontsize=12)
    plt.ylabel('Accuracy (%)', fontsize=12)
    plt.title('Accuracy over Epohs', fontsize=14)

    plt.grid(True, linestyle='--', alpha=0.6)
    plt.ylim(min(accuracies) - 0.5, max(accuracies) + 0.5)

    plt.show()
