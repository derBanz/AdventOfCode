#!/usr/local/bin/python3

# Part 1
print("------- Part 1 -------")

data = '3113322113'


def look_and_say(start, iterations=1):
    current = None
    count = 0
    result = ''
    for char in start:
        if char is not current and current:
            result += str(count) + current
            current = char
            count = 1
        elif current:
            count += 1
        else:
            current = char
            count = 1
    else:
        result += str(count) + current
    if iterations == 1:
        return result
    else:
        return look_and_say(result, iterations - 1)


result = look_and_say(data, 40)
print(f'The final result using 40 iterations is {len(result)} characters long.')

# Part 2
print("------- Part 2 -------")

result = look_and_say(data, 50)
print(f'The final result using 50 iterations is {len(result)} characters long.')
