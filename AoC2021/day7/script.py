#!/usr/local/bin/python3
import os

# Part 1
print("------- Part 1 -------")

data = list()
script_dir = os.path.dirname(__file__)
with open(os.path.join(script_dir, 'data.txt')) as file:
    for line in file:
        data = [int(x) for x in line.split(',')]

fuel_costs = [sum([abs(x - i) for x in data]) for i in range(max(data))]

print(f'The crabs need to use {min(fuel_costs)} fuel to assemble in position {fuel_costs.index(min(fuel_costs))}.')

# Part 2
print("------- Part 2 -------")

fuel_costs = [sum([int(abs(x - i) * (abs(x - i) + 1) / 2) for x in data]) for i in range(max(data))]

print(f'The crabs need to use {min(fuel_costs)} fuel to assemble in position {fuel_costs.index(min(fuel_costs))}.')
