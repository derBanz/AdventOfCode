import os

# Part 1
print("------- Part 1 -------")


data = list()
script_dir = os.path.dirname(__file__)
with open(os.path.join(script_dir, 'data.txt')) as file:
    for line in file:
        data.append(line.strip())


def do_steps(data):
    head = (0, 0)
    tail = (0, 0)
    visited = [(0, 0)]
    for step in data:
        head, tail = move_head(step, head, tail, visited)
    return visited


def move_head(step, head, tail, visited):
    step = step.split(" ")
    direction = step[0]
    steps = int(step[1])
    while steps > 0:
        steps -= 1
        if direction == "U":
            head = (head[0], head[1] + 1)
        elif direction == "R":
            head = (head[0] + 1, head[1])
        elif direction == "D":
            head = (head[0], head[1] - 1)
        else:
            head = (head[0] - 1, head[1])
        tail = move_tail(head, tail, visited)
    return head, tail



def move_tail(head, tail, visited):
    dx = 0
    dy = 0
    if head[0] == tail[0]:
        if abs(head[1] - tail[1]) > 1:
            dy = (head[1] - tail[1]) / abs(head[1] - tail[1])
    elif head[1] == tail[1]:
        if abs(head[0] - tail[0]) > 1:
            dx = (head[0] - tail[0]) / abs(head[0] - tail[0])
    elif abs(head[1] - tail[1]) + abs(head[0] - tail[0]) > 2:
        dx = (head[0] - tail[0]) / abs(head[0] - tail[0])
        dy = (head[1] - tail[1]) / abs(head[1] - tail[1])
    tail = (tail[0] + dx, tail[1] + dy)
    visited.append(tail)
    return tail


visited = do_steps(data)
print(f"The tail visited {len(set(visited))} locations at least once.")

# Part 2
print("------- Part 2 -------")


def do_steps(data, knots):
    rope = []
    for knot in range(knots):
        rope.append((0, 0))
    visited = [(0, 0)]
    for step in data:
        rope = move_head(step, rope, visited)
    return visited


def move_head(step, rope, visited):
    step = step.split(" ")
    direction = step[0]
    steps = int(step[1])
    head = rope[0]
    while steps > 0:
        steps -= 1
        if direction == "U":
            head = (head[0], head[1] + 1)
        elif direction == "R":
            head = (head[0] + 1, head[1])
        elif direction == "D":
            head = (head[0], head[1] - 1)
        else:
            head = (head[0] - 1, head[1])
        rope[0] = head
        rope = move_tail(rope, visited)
    return rope



def move_tail(rope, visited):
    for i, knot in enumerate(rope[1:]):
        dx = 0
        dy = 0
        if rope[i][0] == knot[0]:
            if abs(rope[i][1] - knot[1]) > 1:
                dy = (rope[i][1] - knot[1]) / abs(rope[i][1] - knot[1])
        elif rope[i][1] == knot[1]:
            if abs(rope[i][0] - knot[0]) > 1:
                dx = (rope[i][0] - knot[0]) / abs(rope[i][0] - knot[0])
        elif abs(rope[i][1] - knot[1]) + abs(rope[i][0] - knot[0]) > 2:
            dx = (rope[i][0] - knot[0]) / abs(rope[i][0] - knot[0])
            dy = (rope[i][1] - knot[1]) / abs(rope[i][1] - knot[1])
        rope[i + 1] = (knot[0] + dx, knot[1] + dy)
    visited.append(rope[-1])
    return rope


visited = do_steps(data, 10)
print(f"The tail visited {len(set(visited))} locations at least once.")