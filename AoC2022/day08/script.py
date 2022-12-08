import os

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
        try:
            if data[coords[0] - ( i + 1 )][coords[1]] >= value:
                return False
        except IndexError:
            break
    return True


def check_east(data, coords):
    value = data[coords[0]][coords[1]]
    for i in range(0, coords[1]):
        try:
            if data[coords[0]][coords[1] - ( i + 1 )] >= value:
                return False
        except IndexError:
            break
    return True


def check_south(data, coords):
    value = data[coords[0]][coords[1]]
    for i in range(0, coords[0]):
        try:
            if data[coords[0] + ( i + 1 )][coords[1]] >= value:
                return False
        except IndexError:
            break
    return True


def check_west(data, coords):
    value = data[coords[0]][coords[1]]
    for i in range(0, coords[1]):
        try:
            if data[coords[0]][coords[1] + ( i + 1 )] >= value:
                return False
        except IndexError:
            break
    return True


def evaluate(data):
    solve = []
    for x, row in enumerate(data):
        solve.append([])
        for y, col in enumerate(row):
            solve[-1].append(check_all(data, (x, y)))
    return solve


print(evaluate(data))
