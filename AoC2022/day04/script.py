# Part 1
print("------- Part 1 -------")

data = []
with open('data.txt') as file:
    for line in file:
        line = line.strip()
        data.append(line.split(","))


def get_section(idrange):
    idrange = idrange.split("-")
    section = list()
    for i in range(int(idrange[0]), int(idrange[1]) + 1):
        section.append(i)
    return set(section)


def get_sections(line):
    sec1 = get_section(line[0])
    sec2 = get_section(line[1])
    return sec1, sec2


def check_full_inclusion(line):
    sec1, sec2 = get_sections(line)
    sec1diff = sec1.difference(sec2)
    sec2diff = sec2.difference(sec1)
    return sec1diff, sec2diff


def count_full_inclusions(data):
    counter = [set() in check_full_inclusion(line) for line in data]
    return sum(counter)


print(f"In {count_full_inclusions(data)} assignment pairs, one range fully contains the other.")

# Part 2
print("------- Part 2 -------")


def check_overlap(line):
    sec1, sec2 = get_sections(line)
    return sec1.difference(sec2) != sec1


def count_overlaps(data):
    counter = [check_overlap(line) for line in data]
    return sum(counter)


print(f"In {count_overlaps(data)} assignment pairs, the ranges overlap.")