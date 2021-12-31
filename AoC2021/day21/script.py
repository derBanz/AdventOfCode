#!/usr/local/bin/python3
import os

# Part 1
print("------- Part 1 -------")

data = {}
script_dir = os.path.dirname(__file__)
with open(os.path.join(script_dir, "data.txt")) as file:
    for line in file:
        line = line.split()
        data[int(line[1])] = int(line[4])

turn = 0
det_die = 0
players = {k: [v] for k, v in data.items()}
while True:
    turn += 1
    count = 0
    for x in range(3):
        det_die = det_die + 1 if det_die < 100 else 1
        count += det_die
    players[(turn - 1) % 2 + 1].append(
        (players[(turn - 1) % 2 + 1][-1] + count - 1) % 10 + 1
    )
    if sum(players[(turn - 1) % 2 + 1][1:]) >= 1000:
        break

print(f"The resulting score is {min([sum(x[1:]) for x in players.values()])*turn*3}.")

# Part 2
print("------- Part 2 -------")

dice = {3: 1, 4: 3, 5: 6, 6: 7, 7: 6, 8: 3, 9: 1}
current = [0, 0, {k: [[1, 0, v]] for k, v in data.items()}]
turn = 0
while sum([len(x) for x in current[2].values()]) > 0:
    turn += 1
    situations = []
    for situation in current[2][(turn - 1) % 2 + 1]:
        for k, v in dice.items():
            new_field = (situation[2] + k - 1) % 10 + 1
            if situation[1] + new_field >= 21:
                current[(turn - 1) % 2] += situation[0] * v
            else:
                situations.append(
                    [situation[0] * v, situation[1] + new_field, new_field]
                )
    try:
        new_situations = sum([x[0] for x in situations]) / sum(
            [x[0] for x in current[2][(turn - 1) % 2 + 1]]
        )
    except ZeroDivisionError:
        new_sitations = 1
    current[2][(turn - 1) % 2 + 1] = situations
    current[2][turn % 2 + 1] = [
        [x[0] * new_situations, x[1], x[2]] for x in current[2][turn % 2 + 1]
    ]

print(f"The better player wins in {int(max(current[:2]))} universes.")
