import os
import json

# Part 1
print("------- Part 1 -------")

data = [[]]
script_dir = os.path.dirname(__file__)
with open(os.path.join(script_dir, 'data.txt')) as file:
    for line in file:
        if line == "\n":
            data.append([])
        else:
            data[-1].append(json.loads(line.strip()))


def compare_lists(lists):
    l1 = lists[0]
    l2 = lists[1]
    for i in range(max(len(l1), len(l2))):
        v1 = 0
        v2 = 0
        try:
            v1 = l1[i]
        except IndexError:
            return True
        try:
            v2 = l2[i]
        except IndexError:
            return False
        if type(v1) == int:
            if type(v2) == int:
                if v1 != v2:
                    return v1 < v2
            else:
                check = compare_lists([[v1], v2])
                if check != None:
                    return check
        else:
            if type(v2) == int:
                check = compare_lists([v1, [v2]])
                if check != None:
                    return check
            else:
                check = compare_lists([v1, v2])
                if check != None:
                    return check
    return None


def check_data(data):
    right = list()
    for i, pair in enumerate(data, 1):
        if compare_lists(pair):
            right.append(i)
    return sum(right)


print(check_data(data))


# Part 2
print("------- Part 2 -------")

dividers = [[[2]], [[6]]]
newdata = dividers[:]
for pair in data:
    newdata.append(pair[0])
    newdata.append(pair[1])

def bubble_sort(data):
    n = len(data)
    for i in range(n):
        check = True
        for j in range(n - i - 1):
            if compare_lists([data[j], data[j + 1]]) == False:
                data[j], data[j + 1] = data[j + 1], data[j]
                check = False
        if check:
            break

def find_decoder_key(data):
    bubble_sort(data)
    return (data.index(dividers[0]) + 1) * (data.index(dividers[1]) + 1)


print(find_decoder_key(newdata))