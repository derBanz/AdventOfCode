#!/usr/local/bin/python3
import os


# Part 1
print("------- Part 1 -------")

task1 = []
script_dir = os.path.dirname(__file__)
with open(os.path.join(script_dir, "data.txt")) as file:
    for line in file:
        task1.append([])
        for char in line.strip():
            task1[-1].append(int(char))


def get_path_score(path):
    score = 0
    for node in path[1:]:
        score += task1[node[1]][node[0]]
    return score


def get_reference():
    x = 0
    y = 0
    path = [(0, 0)]
    while True:
        if (x + y) % 2:
            x += 1
        else:
            y += 1
        path.append((x, y))
        if x == len(task1[0]) - 1 and y == len(task1) - 1:
            break
    return {(x, y): (get_path_score(path), path)}


current_paths = get_reference()
current_paths[(0, 0)] = (0, [(0, 0)])
while True:
    paths = {}
    for end, path in current_paths.items():
        if end == (len(task1[0]) - 1, len(task1) - 1):
            paths[end] = (
                paths[end] if paths.get(end) and path[0] > paths[end][0] else path
            )
            continue
        x = end[0]
        y = end[1]
        for new_coords in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
            if any(
                [
                    new_coords[0] >= len(task1[0]),
                    new_coords[1] >= len(task1),
                    new_coords[0] < 0,
                    new_coords[1] < 0,
                    new_coords in path[1],
                ]
            ):
                continue
            tmp_path = path[1].copy()
            tmp_path.append(new_coords)
            tmp_score = get_path_score(tmp_path)
            if tmp_score < current_paths[(len(task1[0]) - 1, len(task1) - 1)][0]:
                paths[new_coords] = (
                    paths[new_coords]
                    if paths.get(new_coords) and tmp_score > paths[new_coords][0]
                    else (tmp_score, tmp_path)
                )
    current_best = paths.get((len(task1[0]) - 1, len(task1) - 1), [0, []])
    best_score = current_best[0]
    print(len(current_paths), best_score)
    current_paths = {k: v for k, v in paths.items() if v[0] <= best_score}
    if len(current_paths) == 1:
        break

print(f"The total risk of the least risky path is {best_score}.")


# Part 2
print("------- Part 2 -------")

task2 = []
for y in range(len(task1) * 5):
    task2.append([])
    for x in range(len(task1[0]) * 5):
        new = (
            task1[y % len(task1)][x % len(task1[0])]
            + int(y / len(task1))
            + int(x / len(task1[0]))
        )
        task2[-1].append(new if new <= 9 else new - 9)
print(task2)


def get_path_score(path):
    score = 0
    for node in path[1:]:
        score += task2[node[1]][node[0]]
    return score


def get_reference():
    x = 0
    y = 0
    path = [(0, 0)]
    while True:
        if (x + y) % 2:
            x += 1
        else:
            y += 1
        path.append((x, y))
        if x == len(task2[0]) - 1 and y == len(task2) - 1:
            break
    return {(x, y): (get_path_score(path), path)}


current_paths = get_reference()
current_paths[(0, 0)] = (0, [(0, 0)])
while True:
    paths = {}
    for end, path in current_paths.items():
        if end == (len(task2[0]) - 1, len(task2) - 1):
            paths[end] = (
                paths[end] if paths.get(end) and path[0] > paths[end][0] else path
            )
            continue
        x = end[0]
        y = end[1]
        for new_coords in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
            if any(
                [
                    new_coords[0] >= len(task2[0]),
                    new_coords[1] >= len(task2),
                    new_coords[0] < 0,
                    new_coords[1] < 0,
                    new_coords in path[1],
                ]
            ):
                continue
            tmp_path = path[1].copy()
            tmp_path.append(new_coords)
            tmp_score = get_path_score(tmp_path)
            if tmp_score < current_paths[(len(task2[0]) - 1, len(task2) - 1)][0]:
                paths[new_coords] = (
                    paths[new_coords]
                    if paths.get(new_coords) and tmp_score > paths[new_coords][0]
                    else (tmp_score, tmp_path)
                )
    current_best = paths.get((len(task2[0]) - 1, len(task2) - 1), [0, []])
    best_score = current_best[0]
    print(len(current_paths), best_score)
    current_paths = {k: v for k, v in paths.items() if v[0] <= best_score}
    if len(current_paths) == 1:
        break

print(f"The total risk of the least risky path is {best_score}.")
