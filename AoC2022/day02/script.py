# Part 1
print("------- Part 1 -------")

data = []
with open('data.txt') as file:
    for line in file:
        data.append(line[0] + line[2])


def evaluate_strategy(data):
    total = 0
    for x in data:
        total += get_game(x)
    return total

def get_win_points(A, B):
    game = {
        "RR": 3,
        "RP": 0,
        "RS": 6,
        "PR": 6,
        "PP": 3,
        "PS": 0,
        "SR": 0,
        "SP": 6,
        "SS": 3
    }
    return game[A + B]


def get_choice_points(A):
    choice = {
        "R": 1,
        "P": 2,
        "S": 3
        }
    return choice[A]


def get_points(A, B):
    return get_choice_points(A) + get_win_points(A, B)


def get_game(game):
    A = ""
    B = ""
    if game[0] == "A":
        B = "R"
    elif game[0] == "B":
        B = "P"
    else:
        B = "S"
    if game[1] == "X":
        A = "R"
    elif game[1] == "Y":
        A = "P"
    else:
        A = "S"
    return get_points(A, B)

total = 0
for x in data:
    total += get_game(x)

print(f"My total score according to the strategy guide would be {total}.")

# Part 2
print("------- Part 2 -------")


def get_game(game):
    A = ""
    B = ""
    if game[0] == "A":
        B = "R"
    elif game[0] == "B":
        B = "P"
    else:
        B = "S"
    scenarios = {
        get_win_points("R", B): "R",
        get_win_points("P", B): "P",
        get_win_points("S", B): "S"
    }
    if game[1] == "X":
        A = scenarios[0]
    elif game[1] == "Y":
        A = scenarios[3]
    else:
        A = scenarios[6]
    return get_points(A, B)


total = evaluate_strategy(data)

print(f"My total score according to the new interpretation of the strategy guide would be {total}.")
