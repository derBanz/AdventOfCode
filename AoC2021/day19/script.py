#!/usr/local/bin/python3
import os
from math import sqrt

# Part 1
print("------- Part 1 -------")

data = dict()
script_dir = os.path.dirname(__file__)
with open(os.path.join(script_dir, "data.txt")) as file:
    current = 0
    for line in file:
        if line.find("scanner") >= 0:
            current = int(line[12:14])
            data[current] = []
            continue
        try:
            line = line.split(",")
            data[current].append([int(x) for x in line])
        except ValueError:
            continue

scannerfields = {
    scanner: [
        [
            sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 + (a[2] - b[2]) ** 2)
            for b in beacons
        ]
        for a in beacons
    ]
    for scanner, beacons in data.items()
}

unknown = [x for x in data.keys()]
known = []
beacons = []
scanners = []
new_scannerfield = []
while unknown:
    new_scannerfield = [
        [
            sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 + (a[2] - b[2]) ** 2)
            for b in beacons
        ]
        for a in beacons
    ]
    index = unknown[0]
    if not beacons:
        beacons = [tuple(x) for x in data[index]]
        known.append(unknown.pop(0))
        scanners.append((0, 0, 0))
        continue
    found = []
    for i, distances in enumerate(scannerfields[index]):
        for j, beacon in enumerate(new_scannerfield):
            x = distances + beacon
            if len(x) - len(set(x)) >= 12:
                found.append((data[index][i], beacons[j]))
    if found:
        diff = [None, None, None]
        for x in range(3):
            if len(set([beacon[0][x] - beacon[1][x] for beacon in found])) == 1:
                diff[x] = ((1, x), found[0][0][x] - found[0][1][x])
            elif len(set([beacon[0][x] + beacon[1][x] for beacon in found])) == 1:
                diff[x] = ((-1, x), found[0][0][x] + found[0][1][x])
            elif len(set([beacon[0][x - 1] - beacon[1][x] for beacon in found])) == 1:
                diff[x] = ((1, x - 1), found[0][0][x - 1] - found[0][1][x])
            elif len(set([beacon[0][x - 1] + beacon[1][x] for beacon in found])) == 1:
                diff[x] = ((-1, x - 1), found[0][0][x - 1] + found[0][1][x])
            elif len(set([beacon[0][x - 2] - beacon[1][x] for beacon in found])) == 1:
                diff[x] = ((1, x - 2), found[0][0][x - 2] - found[0][1][x])
            elif len(set([beacon[0][x - 2] + beacon[1][x] for beacon in found])) == 1:
                diff[x] = ((-1, x - 2), found[0][0][x - 2] + found[0][1][x])
        for beacon in data[index]:
            beacons.append(
                tuple(
                    [
                        (beacon[diff[x][0][1]] - diff[x][1]) * diff[x][0][0]
                        for x in range(3)
                    ]
                )
            )
        scanners.append(tuple([-diff[x][1] * diff[x][0][0] for x in range(3)]))
        beacons = list(set(beacons))
        known.append(unknown.pop(unknown.index(index)))
    else:
        unknown.append(unknown.pop(unknown.index(index)))

print(f"There is a total of {len(beacons)} different beacons.")

# Part 2
print("------- Part 2 -------")

print(
    f"The largest Manhattan distance between any two scanners is {max([sum([abs(a[x] - b[x]) for x in range(3)]) for i, a in enumerate(scanners)for b in scanners[i + 1 :]])}."
)
