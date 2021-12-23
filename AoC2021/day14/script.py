#!/usr/local/bin/python3
import os


# Part 1
print("------- Part 1 -------")

data = {"template": None, "insertion": {}}
script_dir = os.path.dirname(__file__)
with open(os.path.join(script_dir, "data.txt")) as file:
    template = True
    for line in file:
        if line == "\n":
            template = False
        elif template:
            res = line.strip()
            template = {}
            for i in range(len(res) - 1):
                try:
                    template[res[i] + res[i + 1]] += 1
                except KeyError:
                    template[res[i] + res[i + 1]] = 1
            data["template"] = template
            first = line[0]
            last = line.strip()[-1]
        else:
            line = line.split(" -> ")
            data["insertion"][line[0]] = [
                line[0][0] + line[1].strip(),
                line[1].strip() + line[0][1],
            ]


def pair_insertion(data):
    res = {"template": {}, "insertion": data["insertion"]}
    for k, v in data["template"].items():
        try:
            res["template"][data["insertion"][k][0]] += v
        except KeyError:
            res["template"][data["insertion"][k][0]] = v
        try:
            res["template"][data["insertion"][k][1]] += v
        except KeyError:
            res["template"][data["insertion"][k][1]] = v
    return res


template = data.copy()
for i in range(10):
    template = pair_insertion(template)

res = template["template"]
counts = {
    char: int((sum([v * k.count(char) for k, v in res.items() if char in k]) + 1) / 2)
    for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if sum([v for k, v in res.items() if char in k]) > 0
}
if first == last:
    counts[first] += 1

most = max(counts.items(), key=lambda x: x[1])
least = min(counts.items(), key=lambda x: x[1])
print(
    f"After 10 iterations, the most common element ('{most[0]}', {most[1]} occurences) and the least common element ('{least[0]}', {least[1]} occurences) substract to {most[1] - least[1]}."
)

# Part 2
print("------- Part 2 -------")

template = data.copy()
for i in range(40):
    template = pair_insertion(template)

res = template["template"]
counts = {
    char: int((sum([v * k.count(char) for k, v in res.items() if char in k]) + 1) / 2)
    for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if sum([v for k, v in res.items() if char in k]) > 0
}
if first == last:
    counts[first] += 1

most = max(counts.items(), key=lambda x: x[1])
least = min(counts.items(), key=lambda x: x[1])
print(
    f"After 40 iterations, the most common element ('{most[0]}', {most[1]} occurences) and the least common element ('{least[0]}', {least[1]} occurences) substract to {most[1] - least[1]}."
)
