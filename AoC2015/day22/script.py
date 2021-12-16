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


def fight(player, boss, active_effects, turn, log, status, hard_difficulty=False):
    turn += 1
    if turn % 2:
        log += f"Turn {turn} - Player turn\n"
        if hard_difficulty:
            log += f"Player loses 1 hp due to the difficulty setting, dropping to {player[0]-1} Hit Points."
            if player[0] == 1:
                log += f"Player dies, Boss is victorious."
                return [(player, boss, active_effects, turn, log, "over")]
            player = (player[0] - 1, player[1], player[2], player[3])
    else:
        log += f"Turn {turn} - Boss turn\n"
    if active_effects[0]:
        if active_effects[0] == 1:
            player = (player[0], player[1], player[2], 0)
            active_effects = (None, active_effects[1], active_effects[2])
            log += "Shield effect ended\n"
        else:
            active_effects = (
                active_effects[0] - 1,
                active_effects[1],
                active_effects[2],
            )
            log += f"Remaining turns on Shield: {active_effects[0]}\n"
    if active_effects[1]:
        player = (player[0], player[1] + 101, player[2], player[3])
        log += f"Player regenerates 101 Mana through the Recharge effect.\n"
        if active_effects[1] == 1:
            active_effects = (active_effects[0], None, active_effects[2])
            log += "Recharge effect ended\n"
        else:
            active_effects = (
                active_effects[0],
                active_effects[1] - 1,
                active_effects[2],
            )
            log += f"Remaining turns on Recharge: {active_effects[1]}\n"
    if active_effects[2]:
        boss = (boss[0] - 3, boss[1], boss[2])
        log += f"Boss takes 3 damage through the Poison effect.\n"
        if boss[0] <= 0:
            log += "Boss dies from the Poison effect. Player is victorious."
            active_effects = (active_effects[0], active_effects[1], None)
            return [(player, boss, active_effects, turn, log, "over")]
        if active_effects[2] == 1:
            active_effects = (active_effects[0], active_effects[1], None)
            log += "Poison effect ended\n"
        else:
            active_effects = (
                active_effects[0],
                active_effects[1],
                active_effects[2] - 1,
            )
            log += f"Remaining turns on Poison: {active_effects[2]}\n"
    if turn % 2:
        possibilities = []
        for action in range(5):
            if action == 0 and player[1] >= 53:
                p = (player[0], player[1] - 53, player[2] + 53, player[3])
                b = (boss[0] - 4, boss[1], boss[2])
                ae = (active_effects[0], active_effects[1], active_effects[2])
                l = (
                    log
                    + f"Player ({p[0]}) casts Arcane Missile, dealing 4 damage and reducing the Boss's health to {b[0]} hit points.\n"
                )
            elif action == 1 and player[1] >= 73:
                p = (player[0] + 2, player[1] - 73, player[2] + 73, player[3])
                b = (boss[0] - 2, boss[1], boss[2])
                ae = (active_effects[0], active_effects[1], active_effects[2])
                l = (
                    log
                    + f"Player ({p[0]}) casts Drain, dealing 2 damage and reducing the Boss's health to {b[0]} hit points while healing themself by 2 hit points.\n"
                )
            elif action == 2 and player[1] >= 113 and not active_effects[0]:
                p = (player[0], player[1] - 113, player[2] + 113, 7)
                b = boss
                ae = (6, active_effects[1], active_effects[2])
                l = (
                    log
                    + f"Player ({p[0]}) casts Shield on themself, increasing their armor by 7 for 6 turns.\n"
                )
            elif action == 3 and player[1] >= 173 and not active_effects[2]:
                p = (player[0], player[1] - 173, player[2] + 173, player[3])
                b = boss
                ae = (active_effects[0], active_effects[1], 6)
                l = (
                    log
                    + f"Player ({p[0]}) casts Poison on the Boss, dealing 3 damage each turn for 6 turns.\n"
                )
            elif action == 4 and player[1] >= 229 and not active_effects[1]:
                p = (player[0], player[1] - 229, player[2] + 229, player[3])
                b = boss
                ae = (active_effects[0], 5, active_effects[2])
                l = (
                    log
                    + f"Player ({p[0]}) casts Recharge on themself, recharging 101 Mana each turn for 5 turns.\n"
                )
            else:
                continue
            if b[0] <= 0:
                l += "Player is victorious"
                s = "over"
            else:
                s = status
            possibilities.append((p, b, ae, turn, l, s))
        if not possibilities:
            possibilities = [
                (
                    player,
                    boss,
                    active_effects,
                    turn,
                    log + "Player is out of Mana. Boss is victorious.",
                    "over",
                )
            ]
    else:
        p = (
            player[0] - max(boss[1] - player[3], 1),
            player[1],
            player[2],
            player[3],
        )
        b = (boss[0], boss[1], boss[2])
        ae = (active_effects[0], active_effects[1], active_effects[2])
        l = (
            log
            + f"Boss ({b[0]}) attacks Player for {max(boss[1] - player[3], 1)} damage, reducing them to {p[0]} hit points.\n"
        )
        if p[0] <= 0:
            l += "Boss is victorious."
            s = "over"
        else:
            s = status
        possibilities = [(p, b, ae, turn, l, s)]
    return possibilities


current_situations = [
    (
        (50, 500, 0, 0),
        (data["Hit Points"], data["Damage"], 0),
        (None, None, None),
        0,
        "",
        "ongoing",
    )
]
finished_situations = []
while True:
    new_situations = []
    for situation in current_situations:
        if situation[5] == "over":
            new_situations.append([situation])
        else:
            new_situations.append(fight(*situation))
    current_situations = []
    for set in new_situations:
        for situation in set:
            current_situations.append(situation)
    wins = [
        situation
        for situation in current_situations
        if situation[5] == "over" and situation[1][0] <= 0
    ]
    best = min(wins, key=lambda x: x[0][2]) if wins else None
    current_situations = [
        situation
        for situation in current_situations
        if not best or situation[0][2] <= best[0][2]
    ]
    if (
        len([situation for situation in current_situations if situation[5] != "over"])
        == 0
    ):
        break

print(
    f"The least amount of mana the player has to spend to win the fight is {best[0][2]}."
)

# Part 2
print("------- Part 2 -------")

current_situations = [
    (
        (50, 500, 0, 0),
        (data["Hit Points"], data["Damage"], 0),
        (None, None, None),
        0,
        "",
        "ongoing",
    )
]
finished_situations = []
while True:
    new_situations = []
    for situation in current_situations:
        if situation[5] == "over":
            new_situations.append([situation])
        else:
            new_situations.append(fight(*situation, hard_difficulty=True))
    current_situations = []
    for set in new_situations:
        for situation in set:
            current_situations.append(situation)
    wins = [
        situation
        for situation in current_situations
        if situation[5] == "over" and situation[1][0] <= 0
    ]
    best = min(wins, key=lambda x: x[0][2]) if wins else None
    current_situations = [
        situation
        for situation in current_situations
        if not best or situation[0][2] <= best[0][2]
    ]
    if (
        len([situation for situation in current_situations if situation[5] != "over"])
        == 0
    ):
        break

print(
    f"The least amount of mana the player has to spend to win the fight on hard difficulty is {best[0][2]}."
)
