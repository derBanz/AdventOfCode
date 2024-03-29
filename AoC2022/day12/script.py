import os
from node import Node
import sys

sys.setrecursionlimit(10000)

# Part 1
print("------- Part 1 -------")

data = [[]]
script_dir = os.path.dirname(__file__)
with open(os.path.join(script_dir, 'data.txt')) as file:
    for line in file:
        for char in line:
            if char == "\n":
                data.append([])
            else:
                data[-1].append(char)


for y, row in enumerate(data):
    for x, char in enumerate(row):
        Node(x, y, char)


print(f"The shortest path from Start to End takes {Node.find_shortest_path('S')} steps.")


# Part 2
print("------- Part 2 -------")

print(f"The location with the shortest path to End takes {Node.find_shortest_path('a')} steps.")