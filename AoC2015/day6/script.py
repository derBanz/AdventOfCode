#!/usr/local/bin/python3
import os

# Part 1
print("------- Part 1 -------")

data = list()
script_dir = os.path.dirname(__file__)
with open(os.path.join(script_dir, 'data.txt')) as file:
    for line in file:
        data.append(line)

grid = [[False for x in range(1000)] for x in range(1000)]
for command in data:
    command = command.split()
    if command[0] == 'toggle':
        for x in range(int(command[1].split(',')[0]), int(command[3].split(',')[0]) + 1):
            for y in range(int(command[1].split(',')[1]), int(command[3].split(',')[1]) + 1):
                grid[x][y] = not grid[x][y]
    elif command[1] == 'on':
        for x in range(int(command[2].split(',')[0]), int(command[4].split(',')[0]) + 1):
            for y in range(int(command[2].split(',')[1]), int(command[4].split(',')[1]) + 1):
                grid[x][y] = True
    else:
        for x in range(int(command[2].split(',')[0]), int(command[4].split(',')[0]) + 1):
            for y in range(int(command[2].split(',')[1]), int(command[4].split(',')[1]) + 1):
                grid[x][y] = False

print(f'A total of {sum(x.count(True) for x in grid)} lights are lit.')

# Part 2
print("------- Part 2 -------")

grid = [[0 for x in range(1000)] for x in range(1000)]
for command in data:
    command = command.split()
    if command[0] == 'toggle':
        for x in range(int(command[1].split(',')[0]), int(command[3].split(',')[0]) + 1):
            for y in range(int(command[1].split(',')[1]), int(command[3].split(',')[1]) + 1):
                grid[x][y] += 2
    elif command[1] == 'on':
        for x in range(int(command[2].split(',')[0]), int(command[4].split(',')[0]) + 1):
            for y in range(int(command[2].split(',')[1]), int(command[4].split(',')[1]) + 1):
                grid[x][y] += 1
    else:
        for x in range(int(command[2].split(',')[0]), int(command[4].split(',')[0]) + 1):
            for y in range(int(command[2].split(',')[1]), int(command[4].split(',')[1]) + 1):
                grid[x][y] = max(grid[x][y] - 1, 0)

print(f'The total brightness level is {sum(sum(x) for x in grid)}.')
