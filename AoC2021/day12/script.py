#!/usr/local/bin/python3
import os

# Part 1
print("------- Part 1 -------")

data = dict()
script_dir = os.path.dirname(__file__)
with open(os.path.join(script_dir, "data.txt")) as file:
    for line in file:
        line = line.split("-")
        line[1] = line[1].strip()
        if data.get(line[0]):
            data[line[0]].append(line[1])
        else:
            data[line[0]] = [line[1]]
        if data.get(line[1]):
            data[line[1]].append(line[0])
        else:
            data[line[1]] = [line[0]]


def visit_neighbours(data, current, visited, paths):
    for destination in data[current[-1]]:
        new_current = current.copy()
        new_current.append(destination)
        new_visited = visited.copy()
        new_visited.append(destination)
        if destination == "end":
            paths.append(new_current)
        elif destination.lower() == destination and destination in visited:
            pass
        else:
            paths = visit_neighbours(data, new_current, new_visited, paths)
    return paths


paths = list()
paths = visit_neighbours(data, ["start"], ["start"], paths)

print(
    f"There are {len(paths)} paths through this cave system that visit small caves at most once."
)

# Part 2
print("------- Part 2 -------")


def visit_neighbours_2(data, current, visited, paths):
    for destination in data[current[-1]]:
        new_current = current.copy()
        new_current.append(destination)
        new_visited = visited.copy()
        new_visited.append(destination)
        if destination == "end":
            paths.append(new_current)
        elif destination.lower() == destination and destination in visited:
            if new_visited[0] == True or destination in ["start", "end"]:
                pass
            else:
                new_visited[0] = True
                paths = visit_neighbours_2(data, new_current, new_visited, paths)

        else:
            paths = visit_neighbours_2(data, new_current, new_visited, paths)
    return paths


paths = list()
paths = visit_neighbours_2(data, ["start"], [False, "start"], paths)

print(
    f"There are {len(paths)} paths through this cave system that visit one small cave at most twice."
)
