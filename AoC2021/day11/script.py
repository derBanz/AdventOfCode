#!/usr/local/bin/python3
import os

# Part 1
print("------- Part 1 -------")

data = list()
script_dir = os.path.dirname(__file__)
with open(os.path.join(script_dir, "data.txt")) as file:
    for line in file:
        data.append([])
        for char in line.strip():
            data[-1].append(int(char))


def flash(grid, x_flash, y_flash):
    for x in range(max(x_flash - 1, 0), min(x_flash + 2, len(data[0]))):
        for y in range(max(y_flash - 1, 0), min(y_flash + 2, len(data))):
            if (x, y) == (x_flash, y_flash):
                continue
            grid[y][x] += 1
    return grid, (x_flash, y_flash)


def step(grid):
    grid = [[cell + 1 for cell in row] for row in grid]
    flashes = any([any(True if cell > 9 else False for cell in row) for row in grid])
    flashed = list()
    while flashes:
        for y, row in enumerate(grid):
            for x, cell in enumerate(row):
                if cell > 9 and (x, y) not in flashed:
                    grid, f = flash(grid, x, y)
                    flashed.append(f)
        flashes = any(
            [
                any(
                    True if (cell > 9 and (x, y) not in flashed) else False
                    for x, cell in enumerate(row)
                )
                for y, row in enumerate(grid)
            ]
        )
    return [[cell if cell < 10 else 0 for cell in row] for row in grid], len(flashed)


grid = [[x for x in sub] for sub in data]
flashes = 0
for i in range(100):
    grid, f = step(grid)
    flashes += f

print(f"After 100 steps, {flashes} dumbo octopuses flashed for us.")

# Part 2
print("------- Part 2 -------")

grid = [[x for x in sub] for sub in data]
steps = 0
while True:
    steps += 1
    grid, f = step(grid)
    if all([all(cell == grid[0][0] for cell in row) for row in grid]):
        break

print(f"After {steps} steps, all octopuses are flashing simultaneously.")
