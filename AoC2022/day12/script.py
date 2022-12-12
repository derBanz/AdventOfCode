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

for node in Node.nodes.values():
    node.find_sources()

print(f"The shortest path takes {Node.find_shortest_path()} steps.")

# res = ""
# for node in sorted(Node.nodes.values(), key=lambda x: x.y):
#     if node.x == 0:
#         res += "\n"
#     res += str(node.shortest_path) + " "
# print(res)