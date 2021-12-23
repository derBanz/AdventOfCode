#!/usr/local/bin/python3
import os

# Part 1
print("------- Part 1 -------")

data = list()
script_dir = os.path.dirname(__file__)
with open(os.path.join(script_dir, "data.txt")) as file:
    for line in file:
        data.append(line.strip())

syntax_score = {")": 3, "]": 57, "}": 1197, ">": 25137}
brackets = {"(": ")", "[": "]", "{": "}", "<": ">"}
score = 0
for line in data:
    opened = list()
    for char in line:
        if char in ["(", "[", "{", "<"]:
            opened.append(char)
        elif brackets[opened[-1]] == char:
            opened.pop()
        else:
            score += syntax_score[char]
            break


print(f"The total syntax error score is {score}.")

# Part 2
print("------- Part 2 -------")

syntax_score = {")": 1, "]": 2, "}": 3, ">": 4}
scores = list()
for line in data:
    opened = list()
    for char in line:
        if char in ["(", "[", "{", "<"]:
            opened.append(char)
        elif brackets[opened[-1]] == char:
            opened.pop()
        else:
            break
    else:
        if not len(opened):
            break
        score = 0
        opened.reverse()
        for char in opened:
            score *= 5
            score += syntax_score[brackets[char]]
        scores.append(score)

res = sorted(scores)
print(f"The middle score is {res[int(len(res) / 2)]}.")
