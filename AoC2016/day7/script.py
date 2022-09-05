# Part 1
print("------- Part 1 -------")

data = []
with open('data.txt') as file:
    for line in file:
        data.append(line.strip())


def checkabba(ipt):
    value = False
    hyper = False
    for i, x in enumerate(ipt):
        hyper = True if (hyper and not x == "]") or x == "[" else False
        try:
            if x == ipt[i+3] and ipt[i+1] == ipt[i+2] and x != ipt[i+1]:
                if hyper:
                    return False
                else:
                    value = True
        except IndexError:
            return value
    return value
        

def checkips(data):
    counter = 0
    for ip in data:
        counter += checkabba(ip)
    return counter


counter = checkips(data)
print(f"There are {counter} ips that support TLS.")

# Part 2
print("------- Part 2 -------")

def checkaba(ipt):
    valuesaba = []
    valuesbab = []
    hyper = False
    for i, x in enumerate(ipt):
        hyper = True if (hyper and not x == "]") or x == "[" else False
        try:
            if x == ipt[i+2] and ipt[i+1] != x:
                var1 = x + ipt[i+1] + x
                var2 = ipt[i+1] + x + ipt[i+1]
                if (hyper and var2 in valuesaba) or (not hyper and var2 in valuesbab):
                    return True
                elif hyper and var1 not in valuesbab:
                    valuesbab.append(var1)
                elif not hyper and var1 not in valuesaba:
                    valuesaba.append(var1)
        except IndexError:
            pass
    return False


def checkips(data):
    counter = 0
    for ip in data:
        counter += checkaba(ip)
    return counter


counter = checkips(data)
print(f"There are {counter} ips that support SSL.")