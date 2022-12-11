import os

# Part 1
print("------- Part 1 -------")


data = list()
script_dir = os.path.dirname(__file__)
with open(os.path.join(script_dir, 'data.txt')) as file:
    for line in file:
        line = line.strip()
        data.append(line.split(" "))


def do_noop(values):
    values.append(values[-1])
    return values


def do_addx(values, value):
    values.append(values[-1])
    value += values[-1]
    values.append(value)
    return values


def execute(data):
    values = [1]
    for command in data:
        if command[0] == "noop":
            values = do_noop(values)
        elif command[0] == "addx":
            value = int(command[1])
            values = do_addx(values, value)
    return values


def get_selected_strengths(values, cycles):
    out = list()
    for cycle in cycles:
        out.append(values[cycle - 1] * cycle)
    return out


values = execute(data)
strengths = get_selected_strengths(values, [20, 60, 100, 140, 180, 220])
print(f"The sum of the six selected signal strengths is {sum(strengths)}.")


# Part 2
print("------- Part 2 -------")


def draw(values):
    crt = ""
    for cycle, value in enumerate(values):
        cycle = cycle % 40
        if value in range(cycle - 1, cycle + 2):
            crt += "#"
        else:
            crt += " "
        if cycle == 39:
            crt += "\n"
    return crt

print(draw(values))
