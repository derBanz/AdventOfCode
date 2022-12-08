import os
from math import prod

# Part 1
print("------- Part 1 -------")


data = list()
script_dir = os.path.dirname(__file__)
with open(os.path.join(script_dir, 'data.txt')) as file:
    for line in file:
        data.append([int(c) for c in line.strip()])


def check_all(data, coords):
    value = []
    if check_north(data, coords):
        value.append("N")
    if check_east(data, coords):
        value.append("E")
    if check_south(data, coords):
        value.append("S")
    if check_west(data, coords):
        value.append("W")
    return value


def check_north(data, coords):
    value = data[coords[0]][coords[1]]
    for i in range(0, coords[0]):
        if data[coords[0] - ( i + 1 )][coords[1]] >= value:
            return False
    return True


def check_east(data, coords):
    value = data[coords[0]][coords[1]]
    for i in range(coords[1] + 1, len(data[-1])):
        if data[coords[0]][i] >= value:
            return False
    return True


def check_south(data, coords):
    value = data[coords[0]][coords[1]]
    for i in range(coords[0] + 1, len(data)):
        if data[i][coords[1]] >= value:
            return False
    return True


def check_west(data, coords):
    value = data[coords[0]][coords[1]]
    for i in range(0, coords[1]):
        if data[coords[0]][coords[1] - ( i + 1 )] >= value:
            return False
    return True


def evaluate(data):
    solve = []
    for x, row in enumerate(data):
        solve.append([])
        for y, col in enumerate(row):
            solve[-1].append(check_all(data, (x, y)))
    return solve


def count_visible(solve):
    visible = sum([sum([len(x) > 0 for x in row]) for row in solve])
    return visible


solve = evaluate(data)
print(f"From outside the grid, {count_visible(solve)} trees are visible.")


# Part 2
print("------- Part 2 -------")


def check_all(data, coords):
    value = []
    value.append(check_north(data, coords))
    value.append(check_east(data, coords))
    value.append(check_south(data, coords))
    value.append(check_west(data, coords))
    return value


def check_north(data, coords):
    tree = data[coords[0]][coords[1]]
    value = 0
    i = coords[0]
    while i > 0:
        i -= 1
        value += 1
        if data[i][coords[1]] >= tree:
            break
    return value


def check_east(data, coords):
    tree = data[coords[0]][coords[1]]
    value = 0
    i = coords[1]
    while i < len(data[-1]) - 1:
        i += 1
        value += 1
        if data[coords[0]][i] >= tree:
            break
    return value


def check_south(data, coords):
    tree = data[coords[0]][coords[1]]
    value = 0
    i = coords[0]
    while i < len(data) - 1:
        i += 1
        value += 1
        if data[i][coords[1]] >= tree:
            break
    return value


def check_west(data, coords):
    tree = data[coords[0]][coords[1]]
    value = 0
    i = coords[1]
    while i > 0:
        i -= 1
        value += 1
        if data[coords[0]][i] >= tree:
            break
    return value


def get_scenic_score(solve):
    return [[prod(x) for x in row] for row in solve]


def get_max_scenic_score(scores):
    return max([max([cell for cell in row]) for row in scores])


solve = evaluate(data)
score = get_scenic_score(solve)
maxscore = get_max_scenic_score(score)

print(f"The highest scenic score possible is {maxscore}.")
