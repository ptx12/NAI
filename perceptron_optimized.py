import random
import operator

def net(vec_1, weight, theta) -> int:
    return int(sum(map(operator.mul, vec_1, weight)) >= theta)

def delta_weight(old_weight, alpha, expected_out, real_out, x):
    if len(old_weight) != len(x):
        raise ValueError("Vector length mismatch")

    delta = alpha * (expected_out - real_out)
    return list(map(operator.add, old_weight, (delta * i for i in x)))

def delta_theta(old_theta, alpha, expected_out, real_out):
    return old_theta - alpha * (expected_out - real_out)

def perceptron(learning_rate, epochs, test_data, learn_data, theta=None, starting_weight=None):
    theta = theta or random.random()
    num_features = len(learn_data[0]) - 1

    weights = [random.random() if starting_weight is None else starting_weight for _ in range(num_features)]

    unique_labels = {sample[-1] for sample in learn_data}
    label_map = {label: i for i, label in enumerate(unique_labels)}

    for _ in range(epochs):
        for sample in learn_data:
            x, expected_out = sample[:-1], label_map[sample[-1]]
            real_out = net(x, weights, theta)

            weights = delta_weight(weights, learning_rate, expected_out, real_out, x)
            theta = delta_theta(theta, learning_rate, expected_out, real_out)
          
    correct = sum(
        net(sample[:-1], weights, theta) == label_map.get(sample[-1], -1)
        for sample in test_data
    )

    accuracy = (correct / len(test_data)) * 100

    return [weights, theta, accuracy]
