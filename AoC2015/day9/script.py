#!/usr/local/bin/python3
import os

# Part 1
print("------- Part 1 -------")

data = dict()
script_dir = os.path.dirname(__file__)
with open(os.path.join(script_dir, 'data.txt')) as file:
    for line in file:
        line = line.strip()
        line = line.split(' = ')
        line[0] = line[0].split(' to ')
        if not data.get(line[0][0]):
            data[line[0][0]] = dict()
        data[line[0][0]][line[0][1]] = int(line[1])
        if not data.get(line[0][1]):
            data[line[0][1]] = dict()
        data[line[0][1]][line[0][0]] = int(line[1])

possibilities = list()
for start in data:
    for target1 in data[start]:
        for target2 in data[target1]:
            if target2 not in [start]:
                for target3 in data[target2]:
                    if target3 not in [start, target1]:
                        for target4 in data[target3]:
                            if target4 not in [start, target1, target2]:
                                for target5 in data[target4]:
                                    if target5 not in [start, target1, target2, target3]:
                                        for target6 in data[target5]:
                                            if target6 not in [start, target1, target2, target3, target4]:
                                                for end in data[target6]:
                                                    if end not in [start, target1, target2, target3, target4, target5]:
                                                        route = [start, target1, target2, target3, target4, target5, target6, end]
                                                        distance = 0
                                                        for step in range(7):
                                                            distance += data[route[step]][route[step + 1]]
                                                        possibilities.append((route, distance))
shortest = min(possibilities, key=lambda x: x[1])

print(f'The shortest distance is {shortest[1]} by following this route: {shortest[0]}.')

# Part 2
print("------- Part 2 -------")

longest = max(possibilities, key=lambda x: x[1])

print(f'The longest distance is {longest[1]} by following this route: {longest[0]}.')
