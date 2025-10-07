'''Day 3'''

import math
try:
    l = []
    solution_one = 0
    solution_two = []

    slopes = [[1, 1], [1, 3], [1, 5], [1, 7], [2, 1]]

    with open('day3.txt', encoding='utf-8') as file:
        filetext = file.readlines()

    for line in filetext:
        l += line.strip().split()

    x_max = len(l[0])
    y_max = len(l)

    for sl in slopes:
        x = 0
        y = 0
        trees = 0
        while y < y_max:
            if x >= x_max:
                x -= x_max
            if l[y][x] == '#':
                trees += 1
            x += sl[1]
            y += sl[0]
        if sl == [1, 3]:
            solution_one = trees
        solution_two += [trees]
    solution_two = math.prod(solution_two)
    print(solution_one)
    print(solution_two)

except FileNotFoundError:
    print('This file does not exist')
