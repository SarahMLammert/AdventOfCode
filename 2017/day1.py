'''Day 1'''

try:
    with open('day1.txt', encoding='utf-8') as file:
        filetext = file.read()
    solution_one = 0
    solution_two = 0
    l = list([int(s) for s in filetext])
    step = int(len(l) / 2)
    for i, v in enumerate(l):
        if i == (len(l) - 1):
            if l[0] == v:
                solution_one += v
        else:
            if v == l[i+1]:
                solution_one += v
        if i + step >= len(l):
            if l[i + step - len(l)] == l[i]:
                solution_two += v
        else:
            if l[i + step] == l[i]:
                solution_two += v
    print(solution_one)
    print(solution_two)
except FileNotFoundError:
    print('This file does not exist')
    