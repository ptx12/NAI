import math

def nodeRSS(x_values : list[int], threshold : float, y_values : list[int]) -> float:
    group_1 = []
    group_2 = []

    for i in range(0, len(x_values)):
        group_1.append(y_values[i]) if x_values[i] > threshold else group_2.append(y_values[i])

    return sum([math.pow(sum(group_2)/len(group_2) - element, 2) for element in group_2]) + sum([math.pow(sum(group_1)/len(group_2) - element, 2) for element in group_1])

print(nodeRSS(
    x_values=[1, 1, 2, 4],
    y_values=[1, 2, 3, 5],
    threshold=1.5
))
    
