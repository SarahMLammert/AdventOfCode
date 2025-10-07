'''Day 6'''

try:
    solution_one = 0
    solution_two = 0
    groups = []
    current_group = []
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    with open('day6.txt', encoding='utf-8') as file:
        filetext = file.readlines()

    items = 0
    for line in filetext:
        strip = line.strip()
        if strip != "":
            current_group.append(strip)
            items += 1
        else:
            groups += [[''.join(current_group), items]]
            current_group = []
            items = 0
    if current_group:
        groups += [[''.join(current_group), items]]
    for g in groups:
        solution_one += len(set(g[0]))
        for letter in alphabet:
            if g[0].count(letter) == g[1]:
                solution_two += 1
    print(solution_one)
    print(solution_two)

except FileNotFoundError:
    print('This file does not exist')
