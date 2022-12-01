from math import prod

# Part 1
print("------- Part 1 -------")

data = ""
with open('data.txt') as file:
    for line in file:
        data = line.strip()


result = ""
i = 0
while i < len(data):
    char = data[i]
    marker = []
    if char == "(":
        end = data.find(")",i)
        marker = data[i+1:end].split("x")
        result += int(marker[1]) * data[end+1:end+1+int(marker[0])]
        i = end+int(marker[0])
    else:
        result += char
    i += 1


print(f"The decompressed length of the file is {len(result)}.")


# Part 2
print("------- Part 2 -------")


# result = data
# start = result.find("(")
# while start >= 0:
#     end = result.find(")", start)
#     marker = result[start+1:end].split("x")
#     result = result[:start] + int(marker[1]) * result[end+1:end+1+int(marker[0])] + result[end+1+int(marker[0]):]
#     start = result.find("(")
#     print(f"{result.count('(')} marker sections remaining, the first one is at position {result.find('(')}.")

result = 0
inmarker = False
markers = []
newmarker = []
for i, char in enumerate(data):
    markers = [x for x in markers if x[0] > 0]
    for marker in markers:
        marker[0] -= 1
    if inmarker:
        if char == "x":
            newmarker.append("")
        elif char == ")":
            inmarker = False
            markers.append([int(x) for x in newmarker])
        else:
            newmarker[-1] += str(char)
    elif char == "(":
        newmarker = [""]
        inmarker = True
    else:
        multiplier = prod([x[1] for x in markers])
        result += multiplier    


print(f"The length of the fully decompressed file is {result}.")