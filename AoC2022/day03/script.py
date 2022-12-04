# Part 1
print("------- Part 1 -------")

data = []
with open('data.txt') as file:
    for line in file:
        line = line.strip()
        size = int(len(line) / 2)
        data.append((line[:size], line[size:]))


def get_shared_item(pack1, pack2):
    pack1 = set(pack1)
    pack2 = set(pack2)
    item = pack1.intersection(pack2)
    item = list(item)[0]
    return item


def get_shared_items(data):
    items = list()
    for backpack in data:
        items.append(get_shared_item(backpack[0], backpack[1]))
    return items


def get_priority(item):
    items = "0abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    priority = items.index(item)
    return priority


def get_priority_sum(items):
    priority = 0
    for item in items:
        priority += get_priority(item)
    return priority


items = get_shared_items(data)
priority = get_priority_sum(items)

print(f"The sum of priorities of duplicate items is {priority}.")


# Part 2
print("------- Part 2 -------")

data = [[]]
with open('data.txt') as file:
    for line in file:
        line = line.strip()
        if len(data[-1]) == 3:
            data.append([line])
        else:
            data[-1].append(line)


def get_shared_item(pack1, pack2, pack3):
    pack1 = set(pack1)
    pack2 = set(pack2)
    pack3 = set(pack3)
    item = pack1.intersection(pack2)
    item = item.intersection(pack3)
    item = list(item)[0]
    return item


def get_shared_items(data):
    items = list()
    for backpack in data:
        items.append(get_shared_item(backpack[0], backpack[1], backpack[2]))
    return items


items = get_shared_items(data)
priority = get_priority_sum(items)

print(f"The sum of priorities of badge items is {priority}.")