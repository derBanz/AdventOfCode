#!/usr/local/bin/python3
from genericpath import exists
import os
# from math import prod

# Part 1
print("------- Part 1 -------")

data = list()
script_dir = os.path.dirname(__file__)
with open(os.path.join(script_dir, "data.txt")) as file:
    for line in file:
        words = line.split()
        row = words[words.index("row") + 1]
        column = words[words.index("column") + 1]
        data = [int(row[:-1]), int(column[:-1])]

def getnr(r,c):
    return int((r-1)*r/2+1 + (c-1)*r + (c-1)*c/2)

def getcode(data, code):
    nr = getnr(data[0], data[1])
    for i in range(1, nr):
        code = code * 252533 % 33554393
    return code


code = getcode(data, 20151125)
print(f"The code in row {data[0]} and column {data[1]} is {code}.")