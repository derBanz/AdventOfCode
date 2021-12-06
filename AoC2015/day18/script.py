#!/usr/local/bin/python3
import os

# Part 1
print("------- Part 1 -------")

data = list()
script_dir = os.path.dirname(__file__)
with open(os.path.join(script_dir, 'data.txt')) as file:
    for line in file:
        data.append([x for x in line.strip()])


def update_lights(grid):
    grid = [[1 if x == '#' else 0 for x in line] for line in grid]
    new_grid = [['.' for x in line] for line in grid]
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            count = 0
            if i == 0:
                if j == 0:
                    count += grid[i + 1][j] + grid[i][j + 1] + grid[i + 1][j + 1]
                elif j == len(grid[i]) - 1:
                    count += grid[i + 1][j] + grid[i][j - 1] + grid[i + 1][j - 1]
                else:
                    count += grid[i + 1][j] + grid[i][j + 1] + grid[i + 1][j + 1] + grid[i][j - 1] + grid[i + 1][j - 1]
            elif i == len(grid) - 1:
                if j == 0:
                    count += grid[i - 1][j] + grid[i][j + 1] + grid[i - 1][j + 1]
                elif j == len(grid[i]) - 1:
                    count += grid[i - 1][j] + grid[i][j - 1] + grid[i - 1][j - 1]
                else:
                    count += grid[i - 1][j] + grid[i][j + 1] + grid[i - 1][j + 1] + grid[i][j - 1] + grid[i - 1][j - 1]
            else:
                if j == 0:
                    count += grid[i - 1][j] + grid[i][j + 1] + grid[i - 1][j + 1] + grid[i + 1][j] + grid[i + 1][j + 1]
                elif j == len(grid[i]) - 1:
                    count += grid[i - 1][j] + grid[i][j - 1] + grid[i - 1][j-+ 1] + grid[i + 1][j] + grid[i + 1][j - 1]
                else:
                    count += grid[i - 1][j - 1] + grid[i - 1][j] + grid[i - 1][j + 1] + grid[i][j - 1] + grid[i][j + 1] + grid[i + 1][j - 1] + grid[i + 1][j] + grid[i + 1][j + 1]
            if grid[i][j]:
                new_grid[i][j] = '#' if count in [2, 3] else '.'
            else:
                new_grid[i][j] = '#' if count == 3 else '.'
    return new_grid


grid = data.copy()
for i in range(100):
    grid = update_lights(grid)


res = sum([len([x for x in line if x == '#']) for line in grid])

print(f'After 100 turns of animation, {res} lights are lit.')

# Part 2
print("------- Part 2 -------")


def update_lights_2(grid):
    grid = [[1 if x == '#' else 0 for x in line] for line in grid]
    new_grid = [['.' for x in line] for line in grid]
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            count = 0
            if i == 0:
                if j == 0 or j == len(grid[i]) - 1:
                    count = 3
                else:
                    count += grid[i + 1][j] + grid[i][j + 1] + grid[i + 1][j + 1] + grid[i][j - 1] + grid[i + 1][j - 1]
            elif i == len(grid) - 1:
                if j == 0 or j == len(grid[i]) - 1:
                    count = 3
                else:
                    count += grid[i - 1][j] + grid[i][j + 1] + grid[i - 1][j + 1] + grid[i][j - 1] + grid[i - 1][j - 1]
            else:
                if j == 0:
                    count += grid[i - 1][j] + grid[i][j + 1] + grid[i - 1][j + 1] + grid[i + 1][j] + grid[i + 1][j + 1]
                elif j == len(grid[i]) - 1:
                    count += grid[i - 1][j] + grid[i][j - 1] + grid[i - 1][j-+ 1] + grid[i + 1][j] + grid[i + 1][j - 1]
                else:
                    count += grid[i - 1][j - 1] + grid[i - 1][j] + grid[i - 1][j + 1] + grid[i][j - 1] + grid[i][j + 1] + grid[i + 1][j - 1] + grid[i + 1][j] + grid[i + 1][j + 1]
            if grid[i][j]:
                new_grid[i][j] = '#' if count in [2, 3] else '.'
            else:
                new_grid[i][j] = '#' if count == 3 else '.'
    return new_grid


grid = data.copy()
grid[0][0] = '#'
grid[0][-1] = '#'
grid[-1][0] = '#'
grid[-1][-1] = '#'
for i in range(100):
    grid = update_lights_2(grid)


res = sum([len([x for x in line if x == '#']) for line in grid])

print(f'After 100 turns of animation, {res} lights are lit.')
