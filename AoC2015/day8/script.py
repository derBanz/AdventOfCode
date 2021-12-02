#!/usr/local/bin/python3
import os
import re

# Part 1
print("------- Part 1 -------")

data = list()
script_dir = os.path.dirname(__file__)
with open(os.path.join(script_dir, 'data.txt')) as file:
    for line in file:
        line = line.strip()
        data.append(line)

total = 0
for line in data:
    raw_count = len(line)
    line = line.replace(r'\\', 'Z')
    line = line.replace(r'\"', 'A')
    line = re.sub(r'\\x[0-9A-Fa-f]{2}', 'X', line)
    total += raw_count - (len(line) - 2)

print(f'The difference between code characters and memory characters is {total}.')

# Part 2
print("------- Part 2 -------")

total = 0
for line in data:
    raw_count = len(line)
    line = line.replace('\\', 'xx')
    line = line.replace('\"', 'yy')
    new_count = len(line) + 2
    total += new_count - raw_count

print(f'The difference between the newly encoded code characters and the original code characters is {total}.')
