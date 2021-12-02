#!/usr/local/bin/python3
import os
import numpy as np

# Part 1
print("------- Part 1 -------")

data = list()
script_dir = os.path.dirname(__file__)
with open(os.path.join(script_dir, 'data.txt')) as file:
    for line in file:
        line = line.split(' -> ')
        line[0] = line[0].split(' ')
        line[-1] = line[-1].strip()
        data.append(line)

task1 = sorted(sorted(data, key=lambda x: x[1]), key=lambda x: len(x[1]))
wires = dict()
while len(task1):
    for i, command in enumerate(task1):
        if len(command[0]) == 1:
            try:
                wires[command[1]] = np.array(int(command[0][0]), dtype='uint16')
            except ValueError:
                try:
                    wires[command[1]] = np.array(wires[command[0][0]], dtype='uint16')
                except KeyError:
                    continue
        elif len(command[0]) == 2:
            try:
                wires[command[1]] = np.array(~ wires[command[0][1]], dtype='uint16')
            except KeyError:
                continue
        else:
            if command[0][1] == 'AND':
                try:
                    wires[command[1]] = np.array(wires[command[0][0]] & wires[command[0][2]], dtype='uint16')
                except KeyError:
                    try:
                        wires[command[1]] = np.array(int(command[0][0]) & wires[command[0][2]], dtype='uint16')
                    except KeyError:
                        continue
            elif command[0][1] == 'OR':
                try:
                    wires[command[1]] = np.array(wires[command[0][0]] | wires[command[0][2]], dtype='uint16')
                except KeyError:
                    continue
            elif command[0][1] == 'LSHIFT':
                try:
                    wires[command[1]] = np.array(wires[command[0][0]] << int(command[0][2]), dtype='uint16')
                except KeyError:
                    continue
            else:
                try:
                    wires[command[1]] = np.array(wires[command[0][0]] >> int(command[0][2]), dtype='uint16')
                except KeyError:
                    continue
        task1.pop(i)
        break

print(f'Wire A receives the signal {wires["a"]}.')

# Part 2
print("------- Part 2 -------")

data = list()
script_dir = os.path.dirname(__file__)
with open(os.path.join(script_dir, 'data2.txt')) as file:
    for line in file:
        line = line.split(' -> ')
        line[0] = line[0].split(' ')
        line[-1] = line[-1].strip()
        data.append(line)

task2 = sorted(sorted(data, key=lambda x: x[1]), key=lambda x: len(x[1]))
wires = dict()
while len(task2):
    for i, command in enumerate(task2):
        if len(command[0]) == 1:
            try:
                wires[command[1]] = np.array(int(command[0][0]), dtype='uint16')
            except ValueError:
                try:
                    wires[command[1]] = np.array(wires[command[0][0]], dtype='uint16')
                except KeyError:
                    continue
        elif len(command[0]) == 2:
            try:
                wires[command[1]] = np.array(~ wires[command[0][1]], dtype='uint16')
            except KeyError:
                continue
        else:
            if command[0][1] == 'AND':
                try:
                    wires[command[1]] = np.array(wires[command[0][0]] & wires[command[0][2]], dtype='uint16')
                except KeyError:
                    try:
                        wires[command[1]] = np.array(int(command[0][0]) & wires[command[0][2]], dtype='uint16')
                    except KeyError:
                        continue
            elif command[0][1] == 'OR':
                try:
                    wires[command[1]] = np.array(wires[command[0][0]] | wires[command[0][2]], dtype='uint16')
                except KeyError:
                    continue
            elif command[0][1] == 'LSHIFT':
                try:
                    wires[command[1]] = np.array(wires[command[0][0]] << int(command[0][2]), dtype='uint16')
                except KeyError:
                    continue
            else:
                try:
                    wires[command[1]] = np.array(wires[command[0][0]] >> int(command[0][2]), dtype='uint16')
                except KeyError:
                    continue
        task2.pop(i)
        break

print(f'Wire A receives the new signal {wires["a"]}.')
