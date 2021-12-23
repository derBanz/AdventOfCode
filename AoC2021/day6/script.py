#!/usr/local/bin/python3
import os

# Part 1
print("------- Part 1 -------")

population = dict()
script_dir = os.path.dirname(__file__)
with open(os.path.join(script_dir, 'data.txt')) as file:
    for line in file:
        line = line.split(',')
        for x in range(7):
            population[x] = line.count(str(x))

for i in range(80):
    new_population = dict()
    for k, v in population.items():
        if k == 0:
            try:
                new_population[6] += v
            except KeyError:
                new_population[6] = v
            new_population[8] = v
        else:
            try:
                new_population[k - 1] += v
            except KeyError:
                new_population[k - 1] = v
    population = new_population

print(f'After 80 days, there are {sum([v for k, v in population.items()])} lanternfish alive.')

# Part 2
print("------- Part 2 -------")

for i in range(256 - 80):
    new_population = dict()
    for k, v in population.items():
        if k == 0:
            try:
                new_population[6] += v
            except KeyError:
                new_population[6] = v
            new_population[8] = v
        else:
            try:
                new_population[k - 1] += v
            except KeyError:
                new_population[k - 1] = v
    population = new_population

print(f'After 256 days, there are {sum([v for k, v in population.items()])} lanternfish alive.')
