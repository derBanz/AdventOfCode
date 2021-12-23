#!/usr/local/bin/python3
import os

# Part 1
print("------- Part 1 -------")

target = ()
script_dir = os.path.dirname(__file__)
with open(os.path.join(script_dir, "data.txt")) as file:
    line = file.readline().split()
    x_range = line[2].split("..")
    y_range = line[3].split("..")
    x_range[0] = int(x_range[0][2:])
    x_range[1] = int(x_range[1][:-1])
    y_range[0] = int(y_range[0][2:])
    y_range[1] = int(y_range[1])
    target = [
        (x, y)
        for x in range(x_range[0], x_range[1] + 1)
        for y in range(y_range[0], y_range[1] + 1)
    ]

position = (0, 0)
if x_range[0] >= 0:
    starting_velocity = (0, y_range[0])
else:
    starting_velocity = (x_range[0], y_range[0])
valid_velocities = []
x = 0
while True:
    y = 0
    while True:
        current_max = 0
        current_position = position
        impossible = False
        current_velocity = (starting_velocity[0] + x, starting_velocity[1] + y)
        while True:
            current_position = (
                current_position[0] + current_velocity[0],
                current_position[1] + current_velocity[1],
            )
            current_max = max(current_position[1], current_max)
            if current_velocity[0] > 0:
                current_velocity = (current_velocity[0] - 1, current_velocity[1] - 1)
            elif current_velocity[0] < 0:
                current_velocity = (current_velocity[0] + 1, current_velocity[1] - 1)
            else:
                current_velocity = (0, current_velocity[1] - 1)
            if (current_position[0] > x_range[1] and current_velocity[0] >= 0) or (
                current_position[0] < x_range[0] and current_velocity[0] <= 0
            ):
                break
            elif current_position[1] < y_range[0]:
                break
            elif current_position in target:
                valid_velocities.append(
                    (starting_velocity[0] + x, starting_velocity[1] + y, current_max)
                )
        if impossible or starting_velocity[1] + y > y_range[0] * (-1):
            break
        y += 1
    x += 1
    if x > x_range[1]:
        break

res = max(valid_velocities, key=lambda x: x[2])
print(
    f"The highest y position of {res[2]} can be found with a starting velocity of {(res[0], res[1])}."
)

# Part 2
print("------- Part 2 -------")

print(
    f"There are a total of {len(set(valid_velocities))} different trajectories that land the probe in the target area."
)
