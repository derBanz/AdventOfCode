# Part 1
print("------- Part 1 -------")

stacks_original = list()
stacknr = 0
commands = list()
with open('data.txt') as file:
    for line in file:
        if line.find("[") >= 0:
            stacks_original.append(line)
        elif line.find(" 1  ") == 0:
            stacknr = int(line.strip()[-1])
        elif len(line.strip()) > 0:
            commands.append(line.strip())



def sort_stacks(stacks, stacknr):
    sortedstacks = list()
    for i in range(0, stacknr):
        sortedstacks.append([])
        for j, level in enumerate(stacks):
            if len(level) >= 4:
                crate = level[:4].strip()
                stacks[j] = level[4:]
                if len(crate) > 0:
                    sortedstacks[-1].insert(0, crate)
            elif len(level) == 3:
                crate = level.strip()
                stacks[j] = ""
                if len(crate) > 0:
                    sortedstacks[-1].insert(0, crate)
                break
    return sortedstacks


def simulate_crane(stacks, commands):
    for command in commands:
        stacks = do_command(stacks, command)
    return stacks


def do_command(stacks, command):
    command = command.split(" ")
    amount = int(command[1])
    origin = int(command[3]) - 1
    target = int(command[5]) - 1
    for i in range(0, amount):
        crate = stacks[origin].pop()
        stacks[target].append(crate)
    return stacks


def get_top_crates(stacks):
    top = ""
    for stack in stacks:
        try:
            top += stack[-1][1]
        except IndexError:
            top += " "
    return top


stacks = stacks_original[:]
sortedstacks = sort_stacks(stacks, stacknr)
simulatedstacks = simulate_crane(sortedstacks, commands)
top = get_top_crates(simulatedstacks)

print(f"The top crates of each stack are {top}.")

# Part 2
print("------- Part 2 -------")


def do_command(stacks, command):
    command = command.split(" ")
    amount = int(command[1])
    origin = int(command[3]) - 1
    target = int(command[5]) - 1
    original_stack_size = len(stacks[target])
    for i in range(0, amount):
        crate = stacks[origin].pop()
        stacks[target].insert(original_stack_size, crate)
    return stacks

stacks = stacks_original[:]
sortedstacks = sort_stacks(stacks, stacknr)
simulatedstacks = simulate_crane(sortedstacks, commands)
top = get_top_crates(simulatedstacks)

print(f"The top crates of each stack are {top}.")