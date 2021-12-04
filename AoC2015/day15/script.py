#!/usr/local/bin/python3
import os

# Part 1
print("------- Part 1 -------")

data = []
script_dir = os.path.dirname(__file__)
with open(os.path.join(script_dir, 'data.txt')) as file:
    for line in file:
        line = line.split()
        data.append([line[0][:-1], int(line[2][:-1]), int(line[4][:-1]), int(line[6][:-1]), int(line[8][:-1]), int(line[10])])

variations = (
    (
        [sprinkles, butterscotch, chocolate, 100 - sprinkles - butterscotch - chocolate],
        (
            data[0][1] * sprinkles + data[1][1] * butterscotch + data[2][1] * chocolate + data[3][1] * (100 - sprinkles - butterscotch - chocolate)
        ) * 
        (
            data[0][2] * sprinkles + data[1][2] * butterscotch + data[2][2] * chocolate + data[3][2] * (100 - sprinkles - butterscotch - chocolate)
        ) * 
        (
            data[0][3] * sprinkles + data[1][3] * butterscotch + data[2][3] * chocolate + data[3][3] * (100 - sprinkles - butterscotch - chocolate)
        ) * 
        (
            data[0][4] * sprinkles + data[1][4] * butterscotch + data[2][4] * chocolate + data[3][4] * (100 - sprinkles - butterscotch - chocolate)
        )
    ) if all((data[0][i] * sprinkles + data[1][i] * butterscotch + data[2][i] * chocolate + data[3][i] * (100 - sprinkles - butterscotch - chocolate)) > 0 for i in range(1, 5)) else (
        [sprinkles, butterscotch, chocolate, 100 - sprinkles - butterscotch - chocolate],
        0
    ) for sprinkles in range(1, 98) for butterscotch in range(1, 99 - sprinkles) for chocolate in range(1, 100 - sprinkles - butterscotch)
)

best = max(variations, key=lambda x: x[1])
print(f'The best combination has a score of {best[1]} and is set up as follows:\n{best[0][0]}tsps of Sprinkles\n{best[0][1]}tsps of Butterscotch\n{best[0][2]}tsps of Chocolate\n{best[0][3]}tsp of Candy\n')

# Part 2
print("------- Part 2 -------")

variations = (
    (
        [sprinkles, butterscotch, chocolate, 100 - sprinkles - butterscotch - chocolate],
        (
            data[0][1] * sprinkles + data[1][1] * butterscotch + data[2][1] * chocolate + data[3][1] * (100 - sprinkles - butterscotch - chocolate)
        ) * 
        (
            data[0][2] * sprinkles + data[1][2] * butterscotch + data[2][2] * chocolate + data[3][2] * (100 - sprinkles - butterscotch - chocolate)
        ) * 
        (
            data[0][3] * sprinkles + data[1][3] * butterscotch + data[2][3] * chocolate + data[3][3] * (100 - sprinkles - butterscotch - chocolate)
        ) * 
        (
            data[0][4] * sprinkles + data[1][4] * butterscotch + data[2][4] * chocolate + data[3][4] * (100 - sprinkles - butterscotch - chocolate)
        ),
        data[0][5] * sprinkles + data[1][5] * butterscotch + data[2][5] * chocolate + data[3][5] * (100 - sprinkles - butterscotch - chocolate)
    ) if all(
        (data[0][i] * sprinkles + data[1][i] * butterscotch + data[2][i] * chocolate + data[3][i] * (100 - sprinkles - butterscotch - chocolate)
    ) > 0 for i in range(1, 5)) and (
        data[0][5] * sprinkles + data[1][5] * butterscotch + data[2][5] * chocolate + data[3][5] * (100 - sprinkles - butterscotch - chocolate) <= 500
    ) else (
        [sprinkles, butterscotch, chocolate, 100 - sprinkles - butterscotch - chocolate],
        0
    ) for sprinkles in range(1, 98) for butterscotch in range(1, 99 - sprinkles) for chocolate in range(1, 100 - sprinkles - butterscotch)
)

best = max(variations, key=lambda x: x[1])
print(f'The best combination has a score of {best[1]} and {best[2]} calories. The set-up is as follows:\n{best[0][0]}tsps of Sprinkles\n{best[0][1]}tsps of Butterscotch\n{best[0][2]}tsps of Chocolate\n{best[0][3]}tsp of Candy\n')
