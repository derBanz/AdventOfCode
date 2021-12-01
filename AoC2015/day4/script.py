#!/usr/local/bin/python3
import os
from hashlib import md5

# Part 1
print("------- Part 1 -------")

data = ''
script_dir = os.path.dirname(__file__)
with open(os.path.join(script_dir, 'data.txt')) as file:
    for line in file:
        data += line

index = 0
while True:
    inpt = data + str(index)
    if md5(inpt.encode()).hexdigest()[:5] == '00000':
        break
    index += 1

print(f'The lowest number to start with five zeroes is {index}.')

# Part 2
print("------- Part 2 -------")

index = 0
while True:
    inpt = data + str(index)
    if md5(inpt.encode()).hexdigest()[:6] == '000000':
        break
    index += 1

print(f'The lowest number to start with six zeroes is {index}.')
