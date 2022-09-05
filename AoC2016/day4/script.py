# Part 1
print("------- Part 1 -------")

data = list()
with open('data.txt') as file:
    for line in file:
        data.append(line.strip())


RELEVANTCHARACTERS = "abcdefghijklmnopqrstuvwxyz"


def getmostcommonchars(room):
    counts = [(x, room.count(x)) for x in RELEVANTCHARACTERS]
    counts.sort(key=lambda x: x[1], reverse=True)
    chars = ""
    for char in counts[:5]:
        chars += char[0]
    return chars


def checkroom(room):
    counts = getmostcommonchars(room[:-10])
    return room[-6:-1] == counts


def getrealrooms(data):
    rooms = []
    for room in data:
        if checkroom(room):
            rooms.append((room[:-10],int(room[-10:-7])))
    return rooms


def addsectorids(data):
    ids = 0
    for room in data:
        ids += room[1]
    return ids


realrooms = getrealrooms(data)
idsum = addsectorids(realrooms)
print(f"The valid rooms' sector ids add up to {idsum}.")


# Part 2
print("------- Part 2 -------")


def decrypt(room):
    name = ""
    sectorid = room[1]
    for char in room[0]:
        if char == "-":
            char = " "
        else:
            for i in range(sectorid):
                try:
                    char = RELEVANTCHARACTERS[RELEVANTCHARACTERS.index(char) + 1]
                except IndexError:
                    char = RELEVANTCHARACTERS[0]
        name += char
    return (name,sectorid)


def decryptallrooms(realrooms):
    realroomsdecrypted = []
    for room in realrooms:
        realroomsdecrypted.append(decrypt(room))
    return realroomsdecrypted


realroomsdecrypted = decryptallrooms(realrooms)
room = [x for x in realroomsdecrypted if "north" in x[0]]

print(f"The sector id of the room storing north pole objects is {room[0][1]}.")