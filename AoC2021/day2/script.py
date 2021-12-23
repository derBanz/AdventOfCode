#!/usr/local/bin/python3
import os

# Part 1
print("------- Part 1 -------")

data = list()
script_dir = os.path.dirname(__file__)
with open(os.path.join(script_dir, 'data.txt')) as file:
    for line in file:
        data.append(line.split())
h = 0
d = 0
for command in data:
    if command[0] == 'forward':
        h += int(command[1])
    elif command[0] == 'up':
        d -= int(command[1])
    elif command[0] == 'down':
        d += int(command[1])

print(f'The final position is:\nHorizontal: {h}\nDepth: {d}\nProduct: {h * d}')

# Part 2
print("------- Part 2 -------")

h = 0
d = 0
a = 0
for command in data:
    if command[0] == 'forward':
        h += int(command[1])
        d += int(command[1]) * a
    elif command[0] == 'up':
        a -= int(command[1])
    elif command[0] == 'down':
        a += int(command[1])

print(f'The final position is:\nHorizontal: {h}\nDepth: {d}\nProduct: {h * d}')
