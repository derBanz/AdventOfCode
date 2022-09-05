# Part 1
print("------- Part 1 -------")

data = []
with open('data.txt') as file:
    for line in file:
        data.append(line.strip())

KEYPAD = [["1", "2", "3"],
          ["4", "5", "6"],
          ["7", "8", "9"]]


def getvalue(coordinates):
    x = coordinates[0]
    y = coordinates[1]
    try:
        kp = KEYPAD[y][x]
        empty = kp == "." or x < 0 or y < 0
    except IndexError:
        empty = True
    return "." if empty else kp


def getnextposition(instructions, current):
    for z in instructions:
        x = current[0]
        y = current[1]
        if z == "U":
            y = y - 1 if getvalue((x, y - 1)) != "." else y
        elif z == "D":
            y = y + 1 if getvalue((x, y + 1)) != "." else y
        elif z == "L":
            x = x - 1 if getvalue((x - 1, y)) != "." else x
        else:
            x = x + 1 if getvalue((x + 1, y)) != "." else x
        current = (x, y)
    return current


def getcode(data):
    code = ""
    position = [1, 1]
    for instructions in data:
        position = getnextposition(instructions, position)
        code += getvalue(position)
    return code


code = getcode(data)
print(f"The code for the bathroom is {code}.")


# Part 2
print("------- Part 2 -------")


KEYPAD = [
    [".", ".", "1", ".", "."],
    [".", "2", "3", "4", "."],
    ["5", "6", "7", "8", "9"],
    [".", "A", "B", "C", "."],
    [".", ".", "D", ".", "."]
]

code = getcode(data)
print(f"The corrected code for the bathroom is {code}.")