# Part 1
print("------- Part 1 -------")

data = list()
with open('data.txt') as file:
    for line in file:
        data.append(line.split())



def checktriangle(specs):
    specs = [int(x) for x in specs]
    x = specs[0]
    y = specs[1]
    z = specs[2]
    return x + y > z and x + z > y and y + z > x


def checkalltriangles(data):
    count = 0
    for triangle in data:
        count += checktriangle(triangle)
    return count


count = checkalltriangles(data)
print(f"{count} of the {len(data)} listed triangles are possible.")

# Part 2
print("------- Part 2 -------")


triangledata = []
for r, row in enumerate(data):
    if r%3 == 0:
        triangledata.append([])
        triangledata.append([])
        triangledata.append([])
    for c, column in enumerate(row):
        triangledata[-3+c%3].append(column)


count = checkalltriangles(triangledata)
print(f"{count} of the {len(triangledata)} listed triangles are possible.")