#!/usr/local/bin/python3
import os

# Part 1
print("------- Part 1 -------")

data = dict()
script_dir = os.path.dirname(__file__)
with open(os.path.join(script_dir, "data.txt")) as file:
    for line in file:
        line = line.split(": ")
        data[line[0]] = int(line[1])

weapons = {
    "Dagger": [8, 4, 0],
    "Shortsword": [10, 5, 0],
    "Warhammer": [25, 6, 0],
    "Longsword": [40, 7, 0],
    "Greataxe": [74, 8, 0],
}
armor = {
    "None": [0, 0, 0],
    "Leather": [13, 0, 1],
    "Chainmail": [31, 0, 2],
    "Splintmail": [53, 0, 3],
    "Bandedmail": [75, 0, 4],
    "Platemail": [102, 0, 5],
}
rings = {
    "None": [0, 0, 0],
    "Damage +1": [25, 1, 0],
    "Damage +2": [50, 2, 0],
    "Damage +3": [100, 3, 0],
    "Defense +1": [20, 0, 1],
    "Defense +2": [40, 0, 2],
    "Defense +3": [80, 0, 3],
}


def fight(dmg_score, armor_score):
    player = 100
    boss = data["Hit Points"]
    i = 1
    while True:
        if i % 2:
            damage = dmg_score - data["Armor"]
            boss -= damage if damage > 0 else 1
        else:
            damage = data["Damage"] - armor_score
            player -= damage if damage > 0 else 1
        if boss <= 0:
            return True
        elif player <= 0:
            return False
        i += 1


combinations = []
for w, weapon in weapons.items():
    for a, arm in armor.items():
        for r1, ring1 in rings.items():
            for r2, ring2 in rings.items():
                if r2 > r1 or r1 == "None":
                    cost = weapon[0] + arm[0] + ring1[0] + ring2[0]
                    dmg_score = weapon[1] + arm[1] + ring1[1] + ring2[1]
                    armor_score = weapon[2] + arm[2] + ring1[2] + ring2[2]
                    if fight(dmg_score, armor_score):
                        combinations.append(
                            (
                                {"Weapon": w, "Armor": a, "Ring 1": r2, "Ring 2": r1},
                                cost,
                            )
                        )

res = min(combinations, key=lambda x: x[1])
print(f"The cheapest setup to win involves {res[0]} and costs {res[1]} gold.")

# Part 2
print("------- Part 2 -------")

combinations = []
for w, weapon in weapons.items():
    for a, arm in armor.items():
        for r1, ring1 in rings.items():
            for r2, ring2 in rings.items():
                if r2 > r1 or r1 == "None":
                    cost = weapon[0] + arm[0] + ring1[0] + ring2[0]
                    dmg_score = weapon[1] + arm[1] + ring1[1] + ring2[1]
                    armor_score = weapon[2] + arm[2] + ring1[2] + ring2[2]
                    if not fight(dmg_score, armor_score):
                        combinations.append(
                            (
                                {"Weapon": w, "Armor": a, "Ring 1": r2, "Ring 2": r1},
                                cost,
                            )
                        )

res = max(combinations, key=lambda x: x[1])
print(f"The most expensive setup to lose involves {res[0]} and costs {res[1]} gold.")
