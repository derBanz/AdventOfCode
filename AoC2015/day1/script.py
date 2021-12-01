#!/usr/local/bin/python3

# Part 1
print("------- Part 1 -------")

data = ''
with open('data.txt') as file:
    for line in file:
        data += line

floor = data.count('(') - data.count(')')
print(f'Santa has to go to floor {floor}.')

# Part 2
print("------- Part 2 -------")

floor = 0
position = 0
for i, char in enumerate(data):
    floor += (char == '(') - (char == ')')
    if floor < 0:
        break
print(f'The position of the character that sends Santa into the basement for the first time is {i + 1}.')
