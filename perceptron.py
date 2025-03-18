import random


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


def delta_weight(old_weight, alpha, expected_out, real_out, x) -> []:
    if len(old_weight) != len(x): raise ImproperVectorLength

    return [j + k for j, k in zip(old_weight, [alpha * (expected_out - real_out) * i for i in x])]

def delta_theta(old_theta, alpha, expected_out, real_out) -> float:
    return old_theta - (alpha * (expected_out - real_out))

def perceptron(learning_rate, epohs, test_data, learn_data, alpha = random.random(),theta = random.random(), starting_weight = -1):
    weights = [
        [random.random() if starting_weight == -1 else starting_weight for i in range(len(learn_data[0]) - 1)] for x in learn_data
    ]


    for i in range(epohs):
        for v in range(len(learn_data)):
            predict = net(learn_data[v],weights[v],theta=theta)





print(delta_weight([2,-1,4,1],0.5,0,net([2,-1,4,1],[2,0,2,8],3),[2,0,2,8]))

#print(load_data("perceptron.test.data"))