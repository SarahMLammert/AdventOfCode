'''Day 1'''

try:
    with open('day1.txt', encoding='utf-8') as file:
        filetext = file.readlines()
    elf_calories = []
    total_calories = []
    for line in filetext:
        if line == "\n":
            total_calories += [elf_calories]
            elf_calories = []
        else:
            line = line.strip('\n')
            elf_calories += [int(line)]
    elf_order = list(map(sum, total_calories))
    elf_order.sort()
    solution_one = elf_order[-1]
    solution_two = sum(elf_order[-3:])
    print(solution_one)
    print(solution_two)
except FileNotFoundError:
    print('This file does not exist')
