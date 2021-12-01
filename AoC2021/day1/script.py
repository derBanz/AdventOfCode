#!/usr/local/bin/python3

# Part 1
print("------- Part 1 -------")

data = list()
with open('data.txt') as file:
    for line in file:
        data.append(int(line))

counter = 0
for i in range(len(data) - 1):
    counter += data[i + 1] > data[i]
print(f'{counter} measurements are greater than the previous.\n')

# Part 2
print("------- Part 2 -------")

previous = sum(data[:3])
counter = 0
for i in range(1, len(data) - 2):
    current = sum(data[i:i+3])
    counter += current > previous
    previous = current
print(f'{counter} measurement-windows are greater than the previous.\n')
