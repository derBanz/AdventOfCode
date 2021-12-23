#!/usr/local/bin/python3
import os

# Part 1
print("------- Part 1 -------")

data = list()
script_dir = os.path.dirname(__file__)
with open(os.path.join(script_dir, "data.txt")) as file:
    for line in file:
        data.append([])
        for num in line.strip():
            data[-1].append(int(num))

low_points = [[None for j in range(len(data[0]))] for i in range(len(data))]
for i, row in enumerate(data):
    for j, cell in enumerate(row):
        if cell == 9:
            low_points[i][j] = cell
            continue
        if i == 0:
            if j == 0:
                if all([data[i][j + 1] > cell, data[i + 1][j] > cell]):
                    low_points[i][j] = cell
            elif j == len(row) - 1:
                if all([data[i][j - 1] > cell, data[i + 1][j] > cell]):
                    low_points[i][j] = cell
            else:
                if all([data[i][j - 1] > cell, data[i + 1][j] > cell, data[i][j + 1] > cell]):
                    low_points[i][j] = cell
        elif i == len(data) - 1:
            if j == 0:
                if all([data[i][j + 1] > cell, data[i - 1][j] > cell]):
                    low_points[i][j] = cell
            elif j == len(row) - 1:
                if all([data[i][j - 1] > cell, data[i - 1][j] > cell]):
                    low_points[i][j] = cell
            else:
                if all([data[i][j - 1] > cell, data[i - 1][j] > cell, data[i][j + 1] > cell]):
                    low_points[i][j] = cell
        else:
            if j == 0:
                if all([data[i - 1][j] > cell, data[i][j + 1] > cell, data[i + 1][j] > cell]):
                    low_points[i][j] = cell
            elif j == len(row) - 1:
                if all([data[i - 1][j] > cell, data[i][j - 1] > cell, data[i + 1][j] > cell]):
                    low_points[i][j] = cell
            else:
                if all([data[i][j - 1] > cell, data[i - 1][j] > cell, data[i][j + 1] > cell, data[i + 1][j] > cell]):
                    low_points[i][j] = cell

res = [x for sub in low_points for x in sub if x is not None and x != 9]
print(f'The sum of risk levels of all low points on the heightmap is {sum(res) + len(res)}.')

# Part 2
print("------- Part 2 -------")

import numpy as np
from scipy.ndimage.measurements import label

array = np.array([[0 if x == 9 else 1 for x in sub] for sub in data])
structure = np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]])

labeled, ncomponents = label(array, structure)
unique, counts = np.unique(labeled, return_counts=True)
res = dict(zip(unique, counts))
res = [v for k, v in sorted(res.items(), key=lambda x: x[1], reverse=True) if k != 0]
print(f'The product of the three largest basins is {res[0] * res[1] * res[2]}.')
