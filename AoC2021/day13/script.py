#!/usr/local/bin/python3
import os
import pandas


# Part 1
print("------- Part 1 -------")

data = []
folds = []
script_dir = os.path.dirname(__file__)
with open(os.path.join(script_dir, "data.txt")) as file:
    grid = True
    for line in file:
        if line == "\n":
            grid = False
        elif grid:
            line = line.split(",")
            data.append((int(line[0]), int(line[1])))
        else:
            line = line[11:].strip()
            line = line.split("=")
            folds.append((line[0], int(line[1])))

grid = [
    [1 for x in range(max(data, key=lambda x: x[0])[0] + 1)]
    for y in range(max(data, key=lambda x: x[1])[1] + 1)
]
for coords in data:
    grid[coords[1]][coords[0]] = 0

fold = folds[0]
if fold[0] == "x":
    new_grid = [
        [
            grid[y][x]
            if x < 2 * fold[1] - len(grid[y]) + 1
            else grid[y][x] * grid[y][len(grid[y]) - (x - (2 * fold[1] - len(grid[y])))]
            for x in range(fold[1])
        ]
        for y in range(len(grid))
    ]
elif fold[0] == "y":
    new_grid = [
        [
            grid[y][x]
            if y < 2 * fold[1] - len(grid) + 1
            else grid[y][x] * grid[len(grid) - (y - (2 * fold[1] - len(grid)))][x]
            for x in range(len(grid[y]))
        ]
        for y in range(fold[1])
    ]
grid = new_grid

print(f"After folding once, there are {sum([x.count(0) for x in grid])} dots visible.")

# Part 2
print("------- Part 2 -------")

grid = [
    [1 for x in range(max(data, key=lambda x: x[0])[0] + 1)]
    for y in range(max(data, key=lambda x: x[1])[1] + 1)
]
for coords in data:
    grid[coords[1]][coords[0]] = 0

for fold in folds:
    if fold[0] == "x":
        new_grid = [
            [
                grid[y][x]
                if x < 2 * fold[1] - len(grid[y]) + 1
                else grid[y][x]
                * grid[y][len(grid[y]) - (x - (2 * fold[1] - len(grid[y])))]
                for x in range(fold[1])
            ]
            for y in range(len(grid))
        ]
    elif fold[0] == "y":
        new_grid = [
            [
                grid[y][x]
                if y < 2 * fold[1] - len(grid) + 1
                else grid[y][x] * grid[len(grid) - (y - (2 * fold[1] - len(grid)))][x]
                for x in range(len(grid[y]))
            ]
            for y in range(fold[1])
        ]
    grid = new_grid

print(f"The following is the entry code to activate the camera system.")
print(pandas.DataFrame([[" " if x == 1 else "*" for x in row] for row in grid]))
