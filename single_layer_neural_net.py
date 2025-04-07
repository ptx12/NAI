import re
import math
import random
from collections import Counter
from perceptron_optimized import perceptron

zero_dict = {chr(i): 0 for i in range(ord('a'), ord('z') + 1)}
def loadfile(filename: str) -> list:
    with open(filename, 'r', errors='ignore') as f:
        result = []
        for line in f:
            parts = line.split(",", 1)
            if len(parts) > 1:
                lang = parts[0].strip().lower()
                text = re.sub(r'[^a-zA-Z]', '', parts[1].strip().lower())
                result.append((lang, text))
        return result
    
def normalize_vector(vec):
    norm = math.sqrt(sum(x * x for x in vec))
    return [x / norm if norm > 0 else 0 for x in vec]

def prepare_dataset(filename, target_language):
    data = loadfile(filename)
    dataset = []
    for lang, text in data:
        letter_count = dict(Counter(text))
        merged = dict(zero_dict)
        merged.update(letter_count)
        sorted_letters = sorted(merged.items())
        letter_vec = [x[1] for x in sorted_letters]
        normalized_vec = normalize_vector(letter_vec)
        label = "1" if lang == target_language else "0"
        dataset.append(normalized_vec + [label])
    return dataset
def activation(x, weights, theta):
    return sum(a * b for a, b in zip(x, weights)) - theta

train_file = 'lang.train.csv'
test_file = 'lang.test.csv'
languages = ['english', 'german', 'polish', 'spanish']
models = {}
epochs = 1000
learning_rate = 0.5

for lang in languages:
    print(f"\n{lang}")
    train_dataset = prepare_dataset(train_file, lang)
    test_dataset = prepare_dataset(test_file, lang)
    weights, theta, acc = perceptron(learning_rate=learning_rate, epochs=epochs, learn_data=train_dataset, test_data=test_dataset, theta=0, starting_weight=0.01)
    print(f"{lang} TRAINED WITH ACC:{acc:.2f}%")
    models[lang] = (weights, theta)
test_data_raw = loadfile(test_file)
correct = 0
print("\nTEST PREDICTS")
for idx, sample in enumerate(test_data_raw):
    letter_count = dict(Counter(sample[1]))
    merged = dict(zero_dict)
    merged.update(letter_count)
    sorted_letters = sorted(merged.items())
    letter_vec = [x[1] for x in sorted_letters]
    normalized_vec = normalize_vector(letter_vec)
    activations = {}
    for lang in languages:
        weights, theta = models[lang]
        activations[lang] = activation(normalized_vec, weights, theta)
    predicted = max(activations, key=activations.get)
    print(f"TEST #{idx}: true language: {sample[0]} | predicted: {predicted} | activations: {activations}")
    if predicted == sample[0]:
        correct += 1
accuracy = correct / len(test_data_raw) * 100
print(f"\nTOTAL ACCURACY: {accuracy:.2f}%")
def classify_text():
    user_input = ""
    while user_input != "end":
        user_input = input("test: ")
        letter_count = dict(Counter(user_input))
        merged = dict(zero_dict)
        merged.update(letter_count)
        sorted_letters = sorted(merged.items())
        letter_vec = [x[1] for x in sorted_letters]
        normalized_vec = normalize_vector(letter_vec)
        activations = {}
        for lang in languages:
            weights, theta = models[lang]
            activations[lang] = activation(normalized_vec, weights, theta)
        predicted = max(activations, key=activations.get)
        print(f"PREDICTED LANG: {predicted} | ACTIVATIONS: {activations}")

if __name__ == "__main__":
    classify_text()
