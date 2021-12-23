#!/usr/local/bin/python3
import os

# Part 1
print("------- Part 1 -------")

data = list()
script_dir = os.path.dirname(__file__)
with open(os.path.join(script_dir, "data.txt")) as file:
    for line in file:
        data.append(int(line))

RELATIVE_WEIGHT = sum(data) / 3


def generate_combinations(data, current):
    combinations = []
    while True:
        present = data.pop()
        if sum(current) + present < RELATIVE_WEIGHT:
            new = [x for x in current]
            new.append(present)
            generate_combinations(data, new)
        if sum(current) + present == RELATIVE_WEIGHT:
            combinations.append()
            combinations[-1] = [x for x in current]
            combinations[-1].append(present)
        if sum(current) + present < RELATIVE_WEIGHT:


possibilities = []
while True:
    current = []
    current_data = sorted([x for x in data])
