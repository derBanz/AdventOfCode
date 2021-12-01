#!/usr/local/bin/python3
import os

# Part 1
print("------- Part 1 -------")

data = ''
script_dir = os.path.dirname(__file__)
with open(os.path.join(script_dir, 'data.txt')) as file:
    for line in file:
        data += line

position = (0, 0)
visited = [(0, 0)]
for char in data:
    if char == '^':
        position = (position[0], position[1] + 1)
    elif char == '>':
        position = (position[0] + 1, position[1])
    elif char == 'v':
        position = (position[0], position[1] - 1)
    elif char == '<':
        position = (position[0] - 1, position[1])
    visited.append(position)

print(f'At the end of the night, Santa visited {len(set(visited))} different houses.')

# Part 2
print("------- Part 2 -------")

santa = (0, 0)
robo_santa = (0, 0)
visited = [(0, 0)]
for i, char in enumerate(data):
    position = robo_santa if i % 2 else santa
    if char == '^':
        position = (position[0], position[1] + 1)
    elif char == '>':
        position = (position[0] + 1, position[1])
    elif char == 'v':
        position = (position[0], position[1] - 1)
    elif char == '<':
        position = (position[0] - 1, position[1])
    if i % 2:
        robo_santa = position
    else:
        santa = position
    visited.append(position)

print(f'At the end of the night, Santa and Robo-Santa visited {len(set(visited))} different houses.')
