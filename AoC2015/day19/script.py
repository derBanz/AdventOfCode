#!/usr/local/bin/python3
import os

# Part 1
print("------- Part 1 -------")

data = {'mol': None, 'replacements': {}}
script_dir = os.path.dirname(__file__)
with open(os.path.join(script_dir, 'data.txt')) as file:
    switch = False
    for line in file:
        if line == '\n':
            switch = True
        elif switch:
            data['mol'] = line.strip()
        else:
            line = line.split(' => ')
            if data['replacements'].get(line[0]):
                data['replacements'][line[0]].append(line[1].split()[0])
            else:
                data['replacements'][line[0]] = [line[1].split()[0]]


def find_mutations(molecule):
    mutations = []
    for k in data['replacements']:
        for i in range(len(molecule) - (len(k) - 1)):
            if molecule[i:i + len(k)] == k:
                for mut in data['replacements'][k]:
                    mutations.append(molecule[:i] + mut + molecule[i + len(k):])
    return mutations


result = find_mutations(data['mol'])
print(f'Based on the given molecule, there are {len(set(result))} replacements possible.')

# Part 2
print("------- Part 2 -------")

atoms = 0
for x in data['mol']:
    if x.upper() == x:
        atoms += 1
rn = data['mol'].count('Rn')
ar = data['mol'].count('Ar')
y = data['mol'].count('Y')

print(f'It will take at least {atoms - rn - ar - 2 * y - 1} steps to create the correct molecule.')
