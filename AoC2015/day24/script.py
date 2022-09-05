#!/usr/local/bin/python3
import os
# from math import prod

# Part 1
print("------- Part 1 -------")

data = list()
script_dir = os.path.dirname(__file__)
with open(os.path.join(script_dir, "data.txt")) as file:
    for line in file:
        data.append(int(line))

def get_relative_weight(data):
    return sum(data) / COMPARTMENTS

def generate_combinations(data):
    combinations = []
    current = []
    minimum = len(data)
    data.sort(reverse=True)
    i = 0
    while i < len(data):
        if sum(current) + data[i] < RELATIVE_WEIGHT:
            current.append(data[i])
            i += 1
        elif sum(current) + data[i] == RELATIVE_WEIGHT:
            current.append(data[i])
            combinations.append(current.copy())
            i = data.index(current[-1]) + 1
            current.pop()
        else:
            i += 1
        while i >= len(data):
            if len(current) == 0:
                break
            i = data.index(current[-1]) + 1
            current.pop()
    return combinations


def get_valid_combinations(possibilities):
    valid = []
    for x in possibilities:
        setx = set(x)
        for y in possibilities:
            sety = set(y)
            if len(setx.intersection(sety)) == 0:
                valid.append(x)
                break
    return valid


def get_smallest_package_amount_combinations(valid_possibilities):
    smallestamount = len(min(valid_possibilities, key=lambda pos: len(pos)))
    return [pos for pos in valid_possibilities if len(pos) == smallestamount]


def get_smallest_quantum_entanglement(optimal_possibilities):
    optimum = -1
    for pos in optimal_possibilities:
        value = 1
        for x in pos:
            value *= x
        optimum = value if optimum == -1 else min(value, optimum)
    return optimum
    # return min([prod(x) for x in optimal_possibilities])

COMPARTMENTS = 4
RELATIVE_WEIGHT = get_relative_weight(data)
original_data = sorted([x for x in data])
print(f"Original data:\n{original_data}")
possibilities = generate_combinations(original_data)
print(f"Possible package combinations to achieve an average of {RELATIVE_WEIGHT}:\n{len(possibilities)}")
# valid = get_valid_combinations(possibilities)
# print(f"Valid combinations:\n{len(valid)}")
optimalpossibilities = get_smallest_package_amount_combinations(possibilities)
print(f"Optimal combinations, i.e. smallest amount of packages: \n{optimalpossibilities}")
optimum = get_smallest_quantum_entanglement(optimalpossibilities)

print(f"The optimal quantum entanglement in Santa's cabin is {optimum}.") # 10723906903
