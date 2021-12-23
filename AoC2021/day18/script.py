#!/usr/local/bin/python3
import os
from math import ceil

# Part 1
print("------- Part 1 -------")

data = list()
script_dir = os.path.dirname(__file__)
with open(os.path.join(script_dir, "data.txt")) as file:
    for line in file:
        data.append(eval(line))


def add_numbers(num1, num2):
    new_number = str([num1, num2])
    while True:
        counter = 0
        explosion = False
        recent = None
        for i, char in enumerate(new_number):
            try:
                recent = [int(char), i]
                if new_number[i - 1].isnumeric():
                    recent = [int(new_number[i - 1 : i + 1]), i - 1]
            except ValueError:
                if char == "[":
                    counter += 1
                elif char == "]":
                    counter -= 1
                if counter == 5:
                    explosion = True
                    new_number = explode(new_number, recent, i)
                    break
        if explosion:
            continue
        splt = False
        recent = False
        for i, char in enumerate(new_number):
            try:
                int(char)
                if recent:
                    splt = True
                    new_number = split(new_number, i - 1)
                    break
                else:
                    recent = True
            except ValueError:
                recent = False
        if splt:
            continue
        break
    return eval(new_number)


def explode(num, recent, index):
    target = eval(num[index : num[index:].find("]") + index + 1])
    res = ""
    next = None
    for j, char in enumerate(str(num)):
        if recent and j == recent[1]:
            res += str(target[0] + recent[0])
        elif recent and recent[0] >= 10 and j == recent[1] + 1:
            continue
        elif j == index:
            res += "0"
        elif next and j in next:
            continue
        elif not next and j > num[index:].find("]") + index and char.isnumeric():
            if num[j + 1].isnumeric():
                res += str(int(num[j : j + 2]) + target[1])
                next = [j, j + 1]
            else:
                res += str(int(char) + target[1])
                next = [j]
        elif j < index or j > num[index:].find("]") + index:
            res += char
    return res


def split(num, index):
    target = int(num[index : index + 2])
    res = ""
    for j, char in enumerate(str(num)):
        if j == index:
            res += str([int(target / 2), ceil(target / 2)])
        elif j < index or j > index + 1:
            res += char
    return res


def get_magnitude(num):
    mag = 0
    if type(num[0]) == int:
        mag += 3 * num[0]
    else:
        mag += 3 * get_magnitude(num[0])
    if type(num[1]) == int:
        mag += 2 * num[1]
    else:
        mag += 2 * get_magnitude(num[1])
    return mag


current_number = None
for number in data:
    if not current_number:
        current_number = number
    else:
        current_number = add_numbers(current_number, number)

print(f"The magnitude of the final sum is {get_magnitude(current_number)}.")

# Part 2
print("------- Part 2 -------")

res = 0
for num1 in data:
    for num2 in data:
        if num1 != num2:
            res = max(res, get_magnitude(add_numbers(num1, num2)))

print(f"The largest magnitude of any sum is {res}.")
