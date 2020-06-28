from random import randint

SIZE = 5
BOARD = []

counter = range(SIZE)

def for_each_set(nested_list, func):
    new_list = nested_list
    for x, row in enumerate(nested_list):
        for y, num in enumerate(row):
            new_list[x][y] = func(num)

    return new_list


for i in counter:
    row = []
    for j in counter:
        row.append(' ')

    BOARD.append(row)

def set_random_num(num):
    return str(randint(0, 1))

for_each_set(BOARD, set_random_num)

for row in BOARD:
    print(' '.join(row))
