'''Day 2'''

import re
try:
    l = []
    solution_one = 0
    solution_two = 0

    with open('day2.txt', encoding='utf-8') as file:
        filetext = file.readlines()
    
    for line in filetext:
        parts = line.strip().split(' ')
        r = parts[0].split('-')
        l_bound = int(r[0])
        u_bound = int(r[1])
        letter = parts[1][0]
        val_one = parts[2][l_bound-1]
        val_two = parts[2][u_bound-1]

        if len(re.findall(letter, parts[2])) in range(l_bound, u_bound + 1):
            solution_one += 1

        if (val_one == letter or val_two == letter) and val_one != val_two:
            solution_two += 1

    print(solution_one)
    print(solution_two)

except FileNotFoundError:
    print('This file does not exist')
