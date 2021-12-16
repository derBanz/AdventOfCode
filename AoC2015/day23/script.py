#!/usr/local/bin/python3
import os

# Part 1
print("------- Part 1 -------")

data = list()
script_dir = os.path.dirname(__file__)
with open(os.path.join(script_dir, "data.txt")) as file:
    for line in file:
        if line[:3] in ["jio", "jie"]:
            data.append((line[:3], line[4], int(line[7:])))
        elif line[:3] == "jmp":
            data.append((line[:3], int(line[4:])))
        elif line[:3] in ["hlf", "tpl", "inc"]:
            data.append((line[:3], line[4]))
        else:
            data.append(None)


def run_program(registers):
    index = 0
    while index < len(data):
        if data[index][0] == "hlf":
            registers[data[index][1]] = int(registers[data[index][1]] / 2)
            index += 1
        elif data[index][0] == "tpl":
            registers[data[index][1]] *= 3
            index += 1
        elif data[index][0] == "inc":
            registers[data[index][1]] += 1
            index += 1
        elif data[index][0] == "jmp":
            index += data[index][1]
        elif data[index][0] == "jie":
            if registers[data[index][1]] % 2:
                index += 1
            else:
                index += data[index][2]
        elif data[index][0] == "jio":
            if registers[data[index][1]] != 1:
                index += 1
            else:
                index += data[index][2]
        else:
            break
    return registers


registers = run_program({"a": 0, "b": 0})
print(
    f'Register b has the value {registers["b"]} once the program has run successfully.'
)

# Part 2
print("------- Part 2 -------")

registers = run_program({"a": 1, "b": 0})
print(
    f'Register b has the value {registers["b"]} once the program has run successfully with a starting as 1.'
)
