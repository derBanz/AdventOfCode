#!/usr/local/bin/python3
import os

# Part 1
print("------- Part 1 -------")

data = []
script_dir = os.path.dirname(__file__)
with open(os.path.join(script_dir, 'data.txt')) as file:
    for line in file:
        line = line.replace(':', '').replace(',', '').split()
        data.append([line[1], {}])
        for i in [2, 4, 6]:
            data[-1][1][line[i]] = int(line[i + 1])

inpt = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1
}
for aunt in data:
    for k, v in aunt[1].items():
        if inpt[k] != v:
            break
    else:
        break
print(f'Aunt {aunt[0]} is the one to give the gift.')

# Part 2
print("------- Part 2 -------")

for aunt in data:
    for k, v in aunt[1].items():
        if k in ['cats', 'trees']:
            if inpt[k] >= v:
                break
        elif k in ['pomeranians', 'goldfish']:
            if inpt[k] <= v:
                break
        else:
            if inpt[k] != v:
                break
    else:
        break

print(f'Aunt {aunt[0]} is the correct aunt after the updated instructions.')
