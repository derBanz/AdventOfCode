#!/usr/local/bin/python3
import os
import math

# Part 1
print("------- Part 1 -------")

script_dir = os.path.dirname(__file__)
with open(os.path.join(script_dir, "data.txt")) as file:
    for line in file:
        data = int(line)

i = 1
while True:
    gifts = 0
    for x in range(1, int(math.sqrt(i) + 1)):
        if not i % x:
            gifts += x * 10
            gifts += int(i / x) * 10
    if gifts >= data:
        break
    i += 1

print(
    f"The first house to get at least {data} presents is house {i} with {gifts} presents."
)

# Part 2
print("------- Part 2 -------")

i = 1
while True:
    gifts = 0
    for x in range(1, int(math.sqrt(i) + 1)):
        if not i % x:
            gifts += x * 11 if i / x <= 50 else 0
            gifts += int(i / x) * 11 if x <= 50 and x ** 2 != i else 0
    if gifts >= data:
        break
    i += 1

print(
    f"The first house to get at least {data} presents is house {i} with {gifts} presents."
)
