#!/usr/local/bin/python3
import os

# Part 1
print("------- Part 1 -------")

data = list()
script_dir = os.path.dirname(__file__)
with open(os.path.join(script_dir, 'data.txt')) as file:
    for line in file:
        line = line.split(' -> ')
        line = [line[0].split(','), line[1].split(',')]
        if int(line[0][0]) < int(line[1][0]) or int(line[0][1]) < int(line[1][1]):
            data.append(((int(line[0][0]), int(line[0][1])), (int(line[1][0]), int(line[1][1]))))
        else:
            data.append(((int(line[1][0]), int(line[1][1])), (int(line[0][0]), int(line[0][1]))))

vents = [['-' for i in range(1000)] for i in range(1000)]
for point in data:
    if point[0][0] == point[1][0]:
        for i in range(point[0][1], point[1][1] + 1):
            if vents[i][point[0][0]] == '-':
                vents[i][point[0][0]] = 1
            else:
                vents[i][point[0][0]] += 1
    elif point[0][1] == point[1][1]:
        for i in range(point[0][0], point[1][0] + 1):
            if vents[point[0][1]][i] == '-':
                vents[point[0][1]][i] = 1
            else:
                vents[point[0][1]][i] += 1

danger = [point for line in vents for point in line if point != '-' and point > 1]
print(f'There are {len(danger)} areas where at least two lines overlap.')

# Part 2
print("------- Part 2 -------")

vents = [['-' for i in range(1000)] for i in range(1000)]
for point in data:
    if point[0][0] == point[1][0]:
        for i in range(point[0][1], point[1][1] + 1):
            if vents[i][point[0][0]] == '-':
                vents[i][point[0][0]] = 1
            else:
                vents[i][point[0][0]] += 1
    elif point[0][1] == point[1][1]:
        for i in range(point[0][0], point[1][0] + 1):
            if vents[point[0][1]][i] == '-':
                vents[point[0][1]][i] = 1
            else:
                vents[point[0][1]][i] += 1
    else:
        dx = (point[1][0] - point[0][0]) / abs(point[1][0] - point[0][0])
        dy = (point[1][1] - point[0][1]) / abs(point[1][1] - point[0][1])
        for i in range(abs(point[1][0] - point[0][0]) + 1):
            if vents[int(point[0][1] + i * dy)][int(point[0][0] + i * dx)] == '-':
                vents[int(point[0][1] + i * dy)][int(point[0][0] + i * dx)] = 1
            else:
                vents[int(point[0][1] + i * dy)][int(point[0][0] + i * dx)] += 1


danger = [point for line in vents for point in line if point != '-' and point > 1]
print(f'There are now {len(danger)} areas where at least two lines overlap.')
