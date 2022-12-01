import os

from command import Command
from bot import Bot


# Part 1
print("------- Part 1 -------")


data = []
script_dir = os.path.dirname(__file__)
with open(os.path.join(script_dir, 'data.txt')) as file:
    for line in file:
        data.append(line.strip())

check = [17, 61]
bots = Bot.bots

for command in data:
    Command(command, check)


print(f"The bot comparing the important microchips {check} is {Bot.winner}.")