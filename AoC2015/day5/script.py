#!/usr/local/bin/python3
import os

# Part 1
print("------- Part 1 -------")

data = list()
script_dir = os.path.dirname(__file__)
with open(os.path.join(script_dir, 'data.txt')) as file:
    for line in file:
        data.append(line)

nice_strings = list()
for s in data:
    nice = True
    if sum(map(s.count, ['a','e','i','o','u'])) < 3:
        nice = False
    if sum(map(s.count, ['aa', 'bb', 'cc', 'dd', 'ee', 'ff', 'gg', 'hh', 'ii', 'jj', 'kk', 'll', 'mm', 'nn', 'oo', 'pp', 'qq', 'rr', 'ss', 'tt', 'uu', 'vv', 'ww', 'xx', 'yy', 'zz'])) == 0:
        nice = False
    if sum(map(s.count, ['ab', 'cd', 'pq', 'xy'])) > 0:
        nice = False
    if nice:
        nice_strings.append(s)

print(f'There are {len(nice_strings)} nice strings.')

# Part 2
print("------- Part 2 -------")

nice_strings = list()
for s in data:
    nice1 = False
    nice2 = False
    for i in range(len(s) - 1):
        if not nice1:
            if s[i] == s[i + 1]:
                nice1 = s.count(2 * s[i]) - s.count(3 * s[i]) > 1
            else:
                nice1 = s.count(s[i] + s[i + 1]) > 1
        if not nice2:
            try:
                nice2 = s[i] == s[i + 2]
            except IndexError:
                break
    if all([nice1, nice2]):
        nice_strings.append(s)

print(f'There are {len(nice_strings)} nice strings.')

