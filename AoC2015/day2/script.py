#!/usr/local/bin/python3
import os

# Part 1
print("------- Part 1 -------")

data = list()
script_dir = os.path.dirname(__file__)
with open(os.path.join(script_dir, 'data.txt')) as file:
    for line in file:
        temp_data = line.strip().split('x')
        data.append([int(x) for x in temp_data])
area = 0
for present in data:
    areas = [
        present[0] * present[1],
        present[1] * present[2],
        present[2] * present[0],
    ]
    area += 2 * sum(areas) + min(areas)

print(f'The elves need to order {area} square feet of wrapping paper.')

# Part 2
print("------- Part 2 -------")

ribbon = 0
for present in data:
    sides = sorted(present)
    ribbon += 2 * (sides[0] + sides[1]) + sides[0] * sides[1] * sides[2]

print(f'The elves need to order {ribbon} feet of ribbon.')
