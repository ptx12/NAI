import random
def perceptron(learning_rate, epochs, learn_data, test_data, theta=None, starting_weight=None):
    if theta is None:
        theta = 0
    if starting_weight is None:
        starting_weight = random.uniform(-0.01, 0.01)
    num_features = len(learn_data[0]) - 1
    weights = [random.uniform(-0.01, 0.01) for _ in range(num_features)]
    for epoch in range(epochs):
        for sample in learn_data:
            x = sample[:-1]
            target = int(sample[-1])
            activation_value = sum(w * xi for w, xi in zip(weights, x)) - theta
            prediction = 1 if activation_value > 0 else 0
            if prediction != target:
                for i in range(num_features):
                    weights[i] += learning_rate * (target - prediction) * x[i]
                theta -= learning_rate * (target - prediction)
        if (epoch + 1) % 100 == 0:
            correct_predictions = 0
            for sample in test_data:
                x = sample[:-1]
                target = int(sample[-1])
                activation_value = sum(w * xi for w, xi in zip(weights, x)) - theta
                prediction = 1 if activation_value > 0 else 0
                if prediction == target:
                    correct_predictions += 1
            acc = correct_predictions / len(test_data) * 100
            print(f"Epoch {epoch + 1} debug accuracy: {acc:.2f}%")
    correct_predictions = 0
    for sample in test_data:
        x = sample[:-1]
        target = int(sample[-1])
        activation_value = sum(w * xi for w, xi in zip(weights, x)) - theta
        prediction = 1 if activation_value > 0 else 0
        if prediction == target:
            correct_predictions += 1
    accuracy = correct_predictions / len(test_data) * 100
    return weights, theta, accuracy
