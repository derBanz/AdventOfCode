#!/usr/local/bin/python3
import os
from math import sqrt

# Part 1
print("------- Part 1 -------")

data = ["", []]
script_dir = os.path.dirname(__file__)
with open(os.path.join(script_dir, "data.txt")) as file:
    algorithm = True
    for line in file:
        if line == "\n":
            algorithm = False
        elif algorithm:
            data[0] += line.strip()
        else:
            data[1].append(line.strip())


def enhance(inpt):
    translate = {".": "0", "#": "1"}
    enhancement = (len(inpt[1]) - len(data[1])) / 2
    outside = "#" if enhancement % 2 and inpt[0][0] == "#" else "."
    inpt = [
        inpt[0],
        [outside * (2 + len(inpt[1][0]))]
        + [outside + row + outside for row in inpt[1] + [outside * len(inpt[1][0])]],
    ]
    output = [inpt[0], []]
    for i, row in enumerate(inpt[1]):
        output[1].append("")
        for j, cell in enumerate(row):
            if i == 0:
                if j == 0:
                    output[1][-1] += output[0][
                        int(
                            translate[outside]
                            + translate[outside]
                            + translate[outside]
                            + translate[outside]
                            + translate[inpt[1][i][j]]
                            + translate[inpt[1][i][j + 1]]
                            + translate[outside]
                            + translate[inpt[1][i + 1][j]]
                            + translate[inpt[1][i + 1][j + 1]],
                            2,
                        )
                    ]
                elif j == len(row) - 1:
                    output[1][-1] += output[0][
                        int(
                            translate[outside]
                            + translate[outside]
                            + translate[outside]
                            + translate[inpt[1][i][j - 1]]
                            + translate[inpt[1][i][j]]
                            + translate[outside]
                            + translate[inpt[1][i + 1][j - 1]]
                            + translate[inpt[1][i + 1][j]]
                            + translate[outside],
                            2,
                        )
                    ]
                else:
                    output[1][-1] += output[0][
                        int(
                            translate[outside]
                            + translate[outside]
                            + translate[outside]
                            + translate[inpt[1][i][j - 1]]
                            + translate[inpt[1][i][j]]
                            + translate[inpt[1][i][j + 1]]
                            + translate[inpt[1][i + 1][j - 1]]
                            + translate[inpt[1][i + 1][j]]
                            + translate[inpt[1][i + 1][j + 1]],
                            2,
                        )
                    ]
            elif i == len(inpt[1]) - 1:
                if j == 0:
                    output[1][-1] += output[0][
                        int(
                            translate[outside]
                            + translate[inpt[1][i - 1][j]]
                            + translate[inpt[1][i - 1][j + 1]]
                            + translate[outside]
                            + translate[inpt[1][i][j]]
                            + translate[inpt[1][i][j + 1]]
                            + translate[outside]
                            + translate[outside]
                            + translate[outside],
                            2,
                        )
                    ]
                elif j == len(row) - 1:
                    output[1][-1] += output[0][
                        int(
                            translate[inpt[1][i - 1][j - 1]]
                            + translate[inpt[1][i - 1][j]]
                            + translate[outside]
                            + translate[inpt[1][i][j - 1]]
                            + translate[inpt[1][i][j]]
                            + translate[outside]
                            + translate[outside]
                            + translate[outside]
                            + translate[outside],
                            2,
                        )
                    ]
                else:
                    output[1][-1] += output[0][
                        int(
                            translate[inpt[1][i - 1][j - 1]]
                            + translate[inpt[1][i - 1][j]]
                            + translate[inpt[1][i - 1][j + 1]]
                            + translate[inpt[1][i][j - 1]]
                            + translate[inpt[1][i][j]]
                            + translate[inpt[1][i][j + 1]]
                            + translate[outside]
                            + translate[outside]
                            + translate[outside],
                            2,
                        )
                    ]
            else:
                if j == 0:
                    output[1][-1] += output[0][
                        int(
                            translate[outside]
                            + translate[inpt[1][i - 1][j]]
                            + translate[inpt[1][i - 1][j + 1]]
                            + translate[outside]
                            + translate[inpt[1][i][j]]
                            + translate[inpt[1][i][j + 1]]
                            + translate[outside]
                            + translate[inpt[1][i + 1][j]]
                            + translate[inpt[1][i + 1][j + 1]],
                            2,
                        )
                    ]
                elif j == len(row) - 1:
                    output[1][-1] += output[0][
                        int(
                            translate[inpt[1][i - 1][j - 1]]
                            + translate[inpt[1][i - 1][j]]
                            + translate[outside]
                            + translate[inpt[1][i][j - 1]]
                            + translate[inpt[1][i][j]]
                            + translate[outside]
                            + translate[inpt[1][i + 1][j - 1]]
                            + translate[inpt[1][i + 1][j]]
                            + translate[outside],
                            2,
                        )
                    ]
                else:
                    output[1][-1] += output[0][
                        int(
                            translate[inpt[1][i - 1][j - 1]]
                            + translate[inpt[1][i - 1][j]]
                            + translate[inpt[1][i - 1][j + 1]]
                            + translate[inpt[1][i][j - 1]]
                            + translate[inpt[1][i][j]]
                            + translate[inpt[1][i][j + 1]]
                            + translate[inpt[1][i + 1][j - 1]]
                            + translate[inpt[1][i + 1][j]]
                            + translate[inpt[1][i + 1][j + 1]],
                            2,
                        )
                    ]
    return output


def print_scan(inpt):
    for x in inpt[1]:
        print(x)


def count_pixels(inpt):
    return sum([x.count("#") for x in inpt[1]])


new_data = data
for x in range(2):
    new_data = enhance(new_data)

print(
    f"After applying the enhancement algorithm twice, there are {count_pixels(new_data)} lit pixels."
)

# Part 2
print("------- Part 2 -------")

new_data = data
for x in range(50):
    new_data = enhance(new_data)

print(
    f"After applying the enhancement algorithm fifty times, there are {count_pixels(new_data)} lit pixels."
)
