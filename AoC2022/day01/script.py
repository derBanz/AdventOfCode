# Part 1
print("------- Part 1 -------")

data = [[]]
with open('data.txt') as file:
    for line in file:
        if line == "\n":
            data.append([])
        else:
            data[-1].append(int(line))

maxcalories = max(data, key=lambda x: sum(x))
print(f"The elf carrying the most calories is elf number {data.index(maxcalories) + 1}, carrying a total of {sum(maxcalories)} calories.")


# Part 2
print("------- Part 2 -------")

data.sort(key=lambda x: -sum(x))
top3 = data[0:3]
top3 = [sum(x) for x in top3]
print(f"The top three elves carry a combined amount of {sum(top3)} calories.")

