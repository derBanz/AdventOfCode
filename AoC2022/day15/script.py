import os

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