from collections import Counter

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
        



    for _ in attribute_cluster:
        print(_)
    

data = extract_data("agaricus-lepiota.data")
train(data_set=data)