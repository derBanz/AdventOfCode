import os
import json

# Part 1
print("------- Part 1 -------")

data = []
script_dir = os.path.dirname(__file__)
with open(os.path.join(script_dir, 'data.txt')) as file:
    for line in file:
        data.append([])
        for coords in line.strip().split(" -> "):
            coords = coords.split(",")
            data[-1].append(("r", int(coords[0]), int(coords[1])))


def build_rocks(data):
    blockage = list()
    for line in data:
        for i in range(len(line) - 1):
            start = line[i]
            end = line[i + 1]
            blockage.append(start)
            try:
                dx = int((end[1] - start[1]) / abs(end[1] - start[1]))
            except ZeroDivisionError:
                dx = 0
            try:
                dy = int((end[2] - start[2]) / abs(end[2] - start[2]))
            except ZeroDivisionError:
                dy = 0
            while blockage[-1] != end:
                prev = blockage[-1]
                blockage.append(("r", prev[1] + dx, prev[2] + dy))
    return list(set(blockage))


def drop_sand(blockage):
    sand = ("s", 500, 0)
    stopped = False
    freefalling = False
    while True:
        fall = ("s", sand[1], sand[2] + 1)
        if fall in blockage or ("r", fall[1], fall[2]) in blockage:
            fallleft = ("s", fall[1] - 1, fall[2])
            if fallleft in blockage or ("r", fallleft[1], fallleft[2]) in blockage:
                fallright = ("s", fall[1] + 1, fall[2])
                if fallright in blockage or ("r", fallright[1], fallright[2]) in blockage:
                    blockage.append(sand)
                    return "s"
                else:
                    sand = fallright
            else:
                sand = fallleft
        else:
            sand = fall
        freefalling = all(block[2] < sand[2] if block[1] == sand[1] else True for block in blockage)
        if freefalling:
            return "f"


blockage = build_rocks(data)

counter = 0
while True:
    if drop_sand(blockage) == "f":
        break
    counter += 1

print(f"After {counter} units of sand fall, it starts flowing into the abyss.")


# Part 2
print("------- Part 2 -------")


def drop_sand(blockage, floor):
    sand = ("s", 500, 0)
    stopped = False
    freefalling = False
    while True:
        fall = ("s", sand[1], sand[2] + 1)
        if fall[2] == floor:
            blockage.append(sand)
            return False
        elif fall in blockage or ("r", fall[1], fall[2]) in blockage:
            fallleft = ("s", fall[1] - 1, fall[2])
            if fallleft in blockage or ("r", fallleft[1], fallleft[2]) in blockage:
                fallright = ("s", fall[1] + 1, fall[2])
                if fallright in blockage or ("r", fallright[1], fallright[2]) in blockage:
                    blockage.append(sand)
                    if sand == ("s", 500, 0):
                        return True
                    return False
                else:
                    sand = fallright
            else:
                sand = fallleft
        else:
            sand = fall


blockage = build_rocks(data)

counter = 0
floor = max(blockage, key=lambda block: block[2])[2] + 2
while True:
    counter += 1
    if drop_sand(blockage, floor):
        break

print(f"After {counter} units of sand fall, no more sand can follow.")