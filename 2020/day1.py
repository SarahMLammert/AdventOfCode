'''Day 1'''

from itertools import permutations

try:
    l = []
    solution_one = 0
    solution_two = 0

    with open('day1.txt', encoding='utf-8') as file:
        filetext = file.readlines()

    for line in filetext:
        l += [int(line.strip())]
    perm_two = permutations(l, 2)

    for p in perm_two:
        if sum(p) == 2020:
            solution_one = p[0] * p[1]
    perm_three = permutations(l, 3)

    for p in perm_three:
        if sum(p) == 2020:
            solution_two = p[0] * p[1] * p[2]

    print(solution_one)
    print(solution_two)

except FileNotFoundError:
    print('This file does not exist')
