from collections import Counter
import math

def extract_data(filename : str) -> list[list[str]]:
    with open(filename, 'r') as fp:
        return [x.strip('\n').split(',') for x in fp.readlines()]
    
def conditional_probablilty(a, b_if_a, b) -> float:
    return (a * b_if_a)/b

def train(data_set):
    class_probabilities = dict(Counter(x[0] for x in data_set))
    total = sum([i for i in class_probabilities.values()])

    for _,y in class_probabilities.items():
        class_probabilities[_] = y/total
    
    attribute_cluster = []

    for column_index in range(1,len(data_set[0])):
        attribute_cluster.append(dict(Counter([z[column_index] for z in data_set])))
        
    classes = class_probabilities.keys()
    n_attr = len(data_set[0]) - 1

    cond_counts = {c: [Counter() for _ in range(n_attr)] for c in classes}
    for sample in data_set:
        c = sample[0]
        for i, val in enumerate(sample[1:]):
            cond_counts[c][i][val] += 1

    class_counts = {c: sum(1 for s in data_set if s[0] == c) for c in classes}

    V = {i: len(set(s[i+1] for s in data_set)) for i in range(n_attr)}

    cond_probs = {}
    for c in classes:
        cond_probs[c] = []
        N_c = class_counts[c]
        for i in range(n_attr):
            counts = cond_counts[c][i]
            d = V[i]
            probs = {val: (cnt + 1) / (N_c + d) for val, cnt in counts.items()}
            probs['_unknown_'] = 1 / (N_c + d)
            cond_probs[c].append(probs)

    return class_probabilities, cond_probs, class_counts, V
        
def predict(sample, priors, cond_probs, class_counts, V):
    scores = {}
    for c, prior in priors.items():
        logp = math.log(prior)
        for i, val in enumerate(sample[1:]):
            probs = cond_probs[c][i]
            logp += math.log(probs.get(val, probs['_unknown_']))
        scores[c] = logp
    return max(scores, key=scores.get)

def evaluate(test_set, priors, cond_probs, class_counts, V):
    tp = fp = tn = fn = 0
    positive = list(priors.keys())[0]

    for sample in test_set:
        true = sample[0]
        pred = predict(sample, priors, cond_probs, class_counts, V)
        
        for sample in test_set:
            true = sample[0]
            pred = predict(sample, priors, cond_probs, class_counts, V)
            print(f"Sample: {sample} | Expected: {true}, Predicted: {pred}", 
                "CORRECT" if pred == true else "INCORRECT")

        if true == positive:
            if pred == positive: tp += 1
            else:                fn += 1
        else:
            if pred == positive: fp += 1
            else:                tn += 1

    accuracy  = (tp + tn) / (tp + tn + fp + fn)
    precision = tp / (tp + fp) if tp + fp > 0 else 0
    recall    = tp / (tp + fn) if tp + fn > 0 else 0
    f1        = 2 * precision * recall / (precision + recall) if precision + recall > 0 else 0

    print(f"Accuracy:  {accuracy:.4f}") 
    print(f"Precision: {precision:.4f}")
    print(f"Recall:    {recall:.4f}")
    print(f"F1-score:  {f1:.4f}")
          
data = extract_data("agaricus-lepiota.data")
priors, cond_probs, class_counts, V = train(data)
test_data = extract_data("agaricus-lepiota.test.data")
evaluate(test_data, priors, cond_probs, class_counts, V)