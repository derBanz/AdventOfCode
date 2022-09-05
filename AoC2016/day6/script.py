# Part 1
print("------- Part 1 -------")

data = []
with open('data.txt') as file:
    helper = []
    for line in file:
        helper.append(line.strip())
    for x in range(max([len(x) for x in helper])):
        data.append("")
    for r, row in enumerate(helper):
        for c, column in enumerate(row):
            data[c] += column

RELEVANTCHARACTERS = "abcdefghijklmnopqrstuvwxyz"


def getmostfrequentchar(column):
    chars = [(x, column.count(x)) for x in RELEVANTCHARACTERS]
    return max(chars, key=lambda x: x[1])


def correct(data):
    message = ""
    for column in data:
        message += getmostfrequentchar(column)[0]
    return message


message = correct(data)
print(f"The error-corrected version of the message is {message}.")


# Part 2
print("------- Part 2 -------")


def getleastfrequentchar(column):
    chars = [(x, column.count(x)) for x in RELEVANTCHARACTERS if column.count(x) > 0]
    return min(chars, key=lambda x: x[1])


def correct(data):
    message = ""
    for column in data:
        message += getleastfrequentchar(column)[0]
    return message


message = correct(data)
print(f"The error-corrected version of the message is actually {message}.")