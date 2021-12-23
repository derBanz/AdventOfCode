#!/usr/local/bin/python3
import os

# Part 1
print("------- Part 1 -------")

data = list()
script_dir = os.path.dirname(__file__)
with open(os.path.join(script_dir, 'data.txt')) as file:
    for line in file:
        line = line.split('|')
        line = [line[0].split(), line[1].split()]
        data.append(line)

count = 0
for line in data:
    for num in line[1]:
        if len(num) in [2, 3, 4, 7]:
            count += 1


print(f'The values 1, 4, 7, 8 appear {count} times in the output fields.')

# Part 2
print("------- Part 2 -------")


def translate(nums):
    translation = {
        'a': None,
        'b': None,
        'c': None,
        'd': None,
        'e': None,
        'f': None,
        'g': None
    }
    nums = {
        2: [x for x in nums if len(x) == 2],
        3: [x for x in nums if len(x) == 3],
        4: [x for x in nums if len(x) == 4],
        5: [x for x in nums if len(x) == 5],
        6: [x for x in nums if len(x) == 6],
        7: [x for x in nums if len(x) == 7]
    }
    # Comparing Number 1 with Number 7
    for num in nums[3][0]:
        if num not in nums[2][0]:
            translation[num] = 'a'
    # Comparing Number 1 with Number 0, 6, 9
    for num in nums[2][0]:
        if len([x for x in nums[6] if num in x]) == 3:
            translation[num] = 'f'
        else:
            translation[num] = 'c'
    # Comparing Number 4 with Number 0, 6, 9
    for num in nums[4][0]:
        if len([x for x in nums[6] if num in x]) == 3:
            translation[num] = 'b' if not translation[num] else translation[num]
        else:
            translation[num] = 'd' if not translation[num] else translation[num]
    # Finding the last two by checking 0, 6, 9
    for num in 'abcdefg':
        if len([x for x in nums[6] if num in x]) == 3:
            translation[num] = 'g' if not translation[num] else translation[num]
        else:
            translation[num] = 'e' if not translation[num] else translation[num]
    return translation


numbers = {
    'abcefg': 0,
    'cf': 1,
    'acdeg': 2,
    'acdfg': 3,
    'bcdf': 4,
    'abdfg': 5,
    'abdefg': 6,
    'acf': 7,
    'abcdefg': 8,
    'abcdfg': 9
}

s = 0
for line in data:
    num = ''
    translation = translate(line[0])
    for n in line[1]:
        chars = ''
        for x in n:
            chars += translation[x]
        num += str(numbers[''.join(sorted(chars))])
    s += int(num)

print(f'The sum of all output values is {s}.')
