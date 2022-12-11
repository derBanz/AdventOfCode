import os
from monkey import Monkey
from item import Item

# Part 1
print("------- Part 1 -------")


data = []
script_dir = os.path.dirname(__file__)
with open(os.path.join(script_dir, 'data.txt')) as file:
    for line in file:
        line = line.strip()
        if line[:6] == "Monkey":
            data.append([line])
        elif line != "":
            data[-1].append(line)


def interpret_data(data):
    for monkey in data:
        name = monkey[0][:-1]
        items = []
        for item in monkey[1][16:].split(", "):
            items.append(Item(int(item)))
        operation = monkey[2][17:]
        test = [int(monkey[3][19:]), monkey[4][18:].capitalize(), monkey[5][19:].capitalize()]
        Monkey(name, items, operation, test)


def do_round():
    for monkey in Monkey.monkeys.values():
        monkey.do_round()


def do_rounds(rounds):
    for r in range(rounds):
        # print("Calculatin round ", r)
        do_round()


# interpret_data(data)
# do_rounds(20)
# print(f"We reached a monkey business level of {Monkey.get_monkey_business()}.")


# Part 2
print("------- Part 2 -------")


interpret_data(data)
do_rounds(10000)
print(f"We reached a monkey business level of {Monkey.get_monkey_business()}.")