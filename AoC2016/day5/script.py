from hashlib import md5

# Part 1
print("------- Part 1 -------")

data = ""
with open('data.txt') as file:
    for line in file:
        data = line.strip()


def checkhash(base, integer, match, position):
    hash = md5((base + str(integer)).encode("utf-8")).hexdigest()
    if hash.find(match) == 0:
        return hash[position - 1]
    return ""


def getinput(base, match, position, repetitions):
    i = 0
    code = ""
    while len(code) < repetitions:
        check = checkhash(base, i, match, position)
        code += check
        i += 1
    return code


base = data
match = "00000"
position = 6
repetitions = 8

code = getinput(base, match, position, repetitions)
print(f"The code for the door is {code}.")


# Part 2
print("------- Part 2 -------")



def checkhash(base, integer, match, position, character):
    hash = md5((base + str(integer)).encode("utf-8")).hexdigest()
    if hash.find(match) == 0:
        return (hash[position - 1],hash[character-1])
    return None


def getinput(base, match, position, character, repetitions):
    i = 0
    code = []
    for x in range(repetitions):
        code.append("")
    while len([x for x in code if x != ""]) < repetitions:
        check = checkhash(base, i, match, position, character)
        if check:
            try:
                if code[int(check[0])] == "":
                    code[int(check[0])] = check[1]
            except:
                pass
        i += 1
    return code


base = data
match = "00000"
position = 6
character = 7
repetitions = 8

code = "".join(getinput(base, match, position, character, repetitions))
print(f"The code for the second door is {code}.")