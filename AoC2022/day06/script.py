# Part 1
print("------- Part 1 -------")

data = ""
with open('data.txt') as file:
    for line in file:
        data = line
    
def find_end_of_marker(data):
    origlen = len(data)
    curr = data[:4]
    data = data[4:]
    while len(set(curr)) < 4:
        curr = curr[1:] + data[:1]
        data = data[1:]
    return origlen - len(data)

print(f"{find_end_of_marker(data)} characters need to be processed before the first start-of-packet marker is detected.")

# Part 2
print("------- Part 2 -------")


def find_start_of_message(data):
    origlen = len(data)
    curr = data[:14]
    data = data[14:]
    while len(set(curr)) < 14:
        curr = curr[1:] + data[:1]
        data = data[1:]
    return origlen - len(data)

print(f"{find_start_of_message(data)} characters need to be processed before the first start-of-message marker is detected.")