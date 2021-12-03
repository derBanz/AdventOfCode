#!/usr/local/bin/python3
import os
import itertools

# Part 1
print("------- Part 1 -------")

data = dict()
script_dir = os.path.dirname(__file__)
with open(os.path.join(script_dir, 'data.txt')) as file:
    for line in file:
        line = line.strip()[:-1]
        line = line.split()
        if line[2] == 'gain':
            line = [line[0], line[-1], int(line[3])]
        else:
            line = [line[0], line[-1], int(line[3]) * -1]
        if not data.get(line[0]):
            data[line[0]] = dict()
        data[line[0]][line[1]] = line[2]


def calculate_seating_arrangements(data):
    arrangements = list()
    for combination in itertools.permutations(data, len(data)):
        combination = list(combination)
        known = False
        for i in range(len(data)):
            if combination not in itertools.chain(*arrangements):
                temp_combo = combination[1:]
                temp_combo.append(combination[0])
                combination = temp_combo
            else:
                known = True
                break
        if known:
            break
        happiness = 0
        for i, person in enumerate(combination):
            temp_happiness = 0
            try:
                temp_happiness += data[person][combination[i + 1]]
                temp_happiness += data[person][combination[i - 1]]
                happiness += temp_happiness
            except IndexError:
                temp_happiness += data[person][combination[0]]
                temp_happiness += data[person][combination[i - 1]]
                happiness += temp_happiness
        arrangements.append((combination, happiness))
    return arrangements


best = max(calculate_seating_arrangements(data), key=lambda x: x[1])
print(f'The optimal arrangement has a happiness value of {best[1]}. The seating order is as follows: {best[0]}.')

# Part 2
print("------- Part 2 -------")

data['myself'] = dict()
for person in data:
    data[person]['myself'] = 0
    data['myself'][person] = 0

best = max(calculate_seating_arrangements(data), key=lambda x: x[1])
print(f'The optimal arrangement including myself has a happiness value of {best[1]}. The seating order is as follows: {best[0]}.')
