#!/usr/local/bin/python3
import os

# Part 1
print("------- Part 1 -------")

data = list()
script_dir = os.path.dirname(__file__)
with open(os.path.join(script_dir, 'data.txt')) as file:
    for line in file:
        data.append(int(line))


def search_next_container(index, containers, count):
    for i, x in enumerate(containers[index:]):
        if count + x <= 150:
            return index + i, x, count + x
    return None


containers = data.copy()
current_result = list()
result = list()
count = 0
index = 0
while True:
    try:
        index, res, count = search_next_container(index, containers, count)
        current_result.append((index, res, count))
        if count == 150:
            result.append(current_result.copy())
            current_result.pop()
            count = current_result[-1][2]
    except TypeError:
        try:
            index = current_result[-1][0]
            current_result.pop()
            try:
                count = current_result[-1][2]
            except IndexError:
                count = 0
        except IndexError:
            index = 0
    index += 1
    if index >= len(containers) and not current_result:
        break


print(f'There are {len(result)} different combinations to fit the eggnog.')

# Part 2
print("------- Part 2 -------")

res = [len(x) for x in result]
print(f'The minimum amount of containers required is {min(res)}. There are {res.count(min(res))} possible combinations.')
