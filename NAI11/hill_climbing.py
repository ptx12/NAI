import random

def fitness(solution, weights, values, capacity):
    total_weight = sum(w * bit for w, bit in zip(weights, solution))
    if total_weight > capacity:
        return -1
    return sum(v * bit for v, bit in zip(values, solution))


def neighbors(solution):
    for i in range(len(solution)):
        nb = solution.copy()
        nb[i] = 1 - nb[i]
        yield nb


def hill_climb(weights, values, capacity, restarts=10):

    n = len(weights)
    best_solution = None
    best_value = -1

    for _ in range(restarts):
        current = [random.randint(0, 1) for _ in range(n)]
        while sum(w * bit for w, bit in zip(weights, current)) > capacity:
            i = random.choice([idx for idx, bit in enumerate(current) if bit == 1])
            current[i] = 0

        improved = True
        while improved:
            improved = False
            current_val = fitness(current, weights, values, capacity)
            for nb in neighbors(current):
                nb_val = fitness(nb, weights, values, capacity)
                if nb_val > current_val:
                    current, current_val = nb, nb_val
                    improved = True
                    break

        if current_val > best_value:
            best_value = current_val
            best_solution = current

    total_weight = sum(w * bit for w, bit in zip(weights, best_solution))
    return best_value, total_weight, best_solution


if __name__ == "__main__":
    weights = [3,1,6,10,1,4,9,1,7,2,6,1,6,2,2,4,8,1,7,3,6,2,9,5,3,3,4,7,3,5,30,50]
    values  = [7,4,9,18,9,15,4,2,6,13,18,12,12,16,19,19,10,16,14,3,14,4,15,7,5,10,10,13,19,9,8,5]
    capacity = 75
    best_val, best_wt, solution = hill_climb(weights, values, capacity, restarts=10)
    print(f"Hill Climbing result: value={best_val}, weight={best_wt}")
    print("Solution vector:", solution)
