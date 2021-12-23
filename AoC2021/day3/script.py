#!/usr/local/bin/python3
import os

# Part 1
print("------- Part 1 -------")

data = list()
script_dir = os.path.dirname(__file__)
with open(os.path.join(script_dir, 'data.txt')) as file:
    for line in file:
        data.append(line.strip())

nums = [{'0': 0, '1': 0} for char in data[0]]
for num in data:
    for i, char in enumerate(num):
        nums[i][char] += 1

gamma = ''
epsilon = ''
for char in nums:
    if char['0'] >= 500:
        gamma += '0'
        epsilon += '1'
    else:
        gamma += '1'
        epsilon += '0'

print(f'The power consumption of the submarine is {int(gamma, 2) * int(epsilon, 2)}.')

# Part 2
print("------- Part 2 -------")

oxygen = data
co2_scrubber = data
for i in range(len(data[0])):
    if len(oxygen) > 1:
        data_o_0 = list(filter(lambda x: x[i] == '0', oxygen))
        data_o_1 = list(filter(lambda x: x[i] == '1', oxygen))
        oxygen = data_o_1 if len(data_o_1) >= len(data_o_0) else data_o_0
    if len(co2_scrubber) > 1:
        data_c_0 = list(filter(lambda x: x[i] == '0', co2_scrubber))
        data_c_1 = list(filter(lambda x: x[i] == '1', co2_scrubber))
        co2_scrubber = data_c_0 if len(data_c_1) >= len(data_c_0) else data_c_1
    if len(oxygen) == len(co2_scrubber) == 1:
        break

print(f'The life support rating of the submarine is {int(oxygen[0], 2) * int(co2_scrubber[0], 2)}.')
