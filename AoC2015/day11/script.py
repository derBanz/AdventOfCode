#!/usr/local/bin/python3

# Part 1
print("------- Part 1 -------")

data = 'hepxcrrq'


def generate_password(data):
    alphabet = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
    while True:
        i = 7
        while True:
            if data[i] == 'z':
                data = data[:i] + 'a' + data[i + 1:]
                i -= 1
            else:
                data = data[:i] + alphabet[alphabet.index(data[i]) + 1] + data[i + 1:]
                break
        test = True
        for i in range(24):
            if alphabet[i:i + 3] in data:
                break
        else:
            test = False
        for i in ['i', 'o', 'l']:
            if i in data:
                test = False
                break
        count = 0
        i = 0
        while i <= 6:
            if data[i] == data[i + 1]:
                count += 1
                i += 1
            i += 1
        if count < 2:
            test = False
        if test:
            break
    return data


pw = generate_password(data)
print(f'Santa\'s new password should be: {pw}')

# Part 2
print("------- Part 2 -------")

pw = generate_password(pw)
print(f'Santa\'s new password should be: {pw}')
