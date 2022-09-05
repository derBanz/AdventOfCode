# Part 1
print("------- Part 1 -------")

data = []
with open('data.txt') as file:
    for line in file:
        data = line.split(", ")

coords = (0, 0)
facing = 0  # north=0, east=1, south=2, west=3

def turn(facing, turning):
    if turning == "R" and facing == 3:
        facing = 0
    elif turning == "L" and facing == 0:
        facing = 3
    else:
        facing = facing + 1 % 4 if turning == "R" else facing - 1 % 4
    return facing


def walk(data, coords, facing):
    for x in data:
        turning = x[0]
        walking = int(x[1:])
        facing = turn(facing, turning)
        x = coords[0]
        y = coords[1]
        if facing == 0:
            y += walking
        elif facing == 1:
            x += walking
        elif facing == 2:
            y -= walking
        else:
            x -= walking
        coords = (x, y)
    return coords


def calcdistance(coords):
    distance = 0
    for x in coords:
        distance += abs(x)
    return distance


destination = walk(data, coords, facing)
distance = calcdistance(destination)

print(f"The shortest path to the Easter Bunny Headquarters at {destination} is {distance}.")


# Part 2
print("------- Part 2 -------")

def walk(data, coords, facing):
    visited = []
    for x in data:
        turning = x[0]
        steps = int(x[1:])
        facing = turn(facing, turning)
        x = coords[0]
        y = coords[1]
        walking = [0, 0]
        if facing == 0:
            walking[1] = 1
        elif facing == 1:
            walking[0] = 1
        elif facing == 2:
            walking[1] = -1
        else:
            walking[0] = -1
        for y in range(steps):
            coords = [sum(x) for x in zip(coords, walking)]
            if coords in visited:
                return coords
            else:
                visited.append(coords)


coords = (0, 0)
facing = 0
destination = walk(data, coords, facing)
distance = calcdistance(destination)

print(f"The shortest path to the actual Easter Bunny Headquarters at {destination} is {distance}.")