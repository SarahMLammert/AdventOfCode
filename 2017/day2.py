'''Day 2'''

from itertools import combinations

try:
    solution_one = 0
    solution_two = 0

    with open('day2.txt', encoding='utf-8') as file:
        lines = [line.split() for line in file.readlines()]

    for l in lines:
        int_list = list(map(int, l))
        solution_one += max(int_list) - min(int_list)
        for a, b in combinations(int_list, 2):
            if a % b == 0:
                solution_two += int(a / b)
            if b % a == 0:
                solution_two += int(b / a)

    print(solution_one)
    print(solution_two)

except FileNotFoundError:
    print('This file does not exist')
