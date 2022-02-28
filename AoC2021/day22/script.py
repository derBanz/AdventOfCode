#!/usr/local/bin/python3
import os

# Part 1
print("------- Part 1 -------")

data = []
script_dir = os.path.dirname(__file__)
with open(os.path.join(script_dir, "data.txt")) as file:
    for line in file:
        data.append([])
        line = line.split()
        data[-1].append(line[0])
        line[1] = line[1].split(",")
        for x in line[1]:
            x = x[2:].split("..")
            data[-1].append((int(x[0]), int(x[1])))


border = (-50, 50)
task1 = {}

for line in data:
    print(data.index(line))
    for x in range(max(line[1][0], border[0]), min(line[1][1], border[1]) + 1):
        for y in range(max(line[2][0], border[0]), min(line[2][1], border[1]) + 1):
            for z in range(max(line[3][0], border[0]), min(line[3][1], border[1]) + 1):
                task1[(x, y, z)] = line[0]


print(
    f'Only considering the cubes between x,y,z=-50..50, a total of {sum([x.count("on") for x in task1.values()])} cubes are on.'
)

# Part 2
print("------- Part 2 -------")

task2 = {}
for line in data:
    print(data.index(line))
    for x in range(line[1][0], line[1][1] + 1):
        for y in range(line[2][0], line[2][1] + 1):
            for z in range(line[3][0], line[3][1] + 1):
                task2[(x, y, z)] = line[0]

print(
    f'Considering all cubes, a total of {sum([x.count("on") for x in task2.values()])} cubes are on.'
)
