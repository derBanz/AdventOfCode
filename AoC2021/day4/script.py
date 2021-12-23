#!/usr/local/bin/python3
import os

# Part 1
print("------- Part 1 -------")

data = {
    'draw': [],
    'boards': [],
}
script_dir = os.path.dirname(__file__)
with open(os.path.join(script_dir, 'data.txt')) as file:
    for i, line in enumerate(file):
        if i == 0:
            line = line.split(',')
            data['draw'] = [int(x) for x in line]
            continue
        if line == '\n':
            data['boards'].append([])
            continue
        line = line.split()
        data['boards'][-1].append([int(x) for x in line])


def check_win_condition(board):
    for i in range(len(board)):
        if all((x == 'x' for x in board[i])) or all((x[i] == 'x' for x in board)):
            return True
    return False


solved = None
for draw in data['draw']:
    for board in data['boards']:
        for i, row in enumerate(board):
            board[i] = ['x' if x == draw else x for x in row]
        if check_win_condition(board):
            solved = (board, draw)
    if solved:
        break
score = 0
for row in solved[0]:
    for column in row:
        if column != 'x':
            score += column
else:
    score *= solved[1]

print(f'The final score of the winning board is {score}.')

# Part 2
print("------- Part 2 -------")

data = {
    'draw': [],
    'boards': [],
}
script_dir = os.path.dirname(__file__)
with open(os.path.join(script_dir, 'data.txt')) as file:
    for i, line in enumerate(file):
        if i == 0:
            line = line.split(',')
            data['draw'] = [int(x) for x in line]
            continue
        if line == '\n':
            data['boards'].append([])
            continue
        line = line.split()
        data['boards'][-1].append([int(x) for x in line])

solved = []
for draw in data['draw']:
    for board in data['boards']:
        for i, row in enumerate(board):
            board[i] = ['x' if x == draw else x for x in row]
        if check_win_condition(board):
            if len(data['boards']) == 1:
                solved = (data['boards'].pop(), draw)
            else:
                solved.append(board)
    if type(solved) == tuple:
        break
    for board in solved:
        data['boards'].remove(board)
    solved = []
score = 0
for row in solved[0]:
    for column in row:
        if column != 'x':
            score += column
else:
    score *= solved[1]

print(f'The final score of the losing board is {score}.')
