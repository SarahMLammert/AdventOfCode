'''Day 1'''

try:
    fuel = []
    solution_one = 0
    solution_two = 0

    with open('day1.txt', encoding='utf-8') as file:
        filetext = file.readlines()

    for line in filetext:
        fuel += [int(line.strip()) // 3 - 2]

    solution_one = sum(fuel)

    current_fuel = fuel.copy()
    while sum(current_fuel) != 0:
        next_fuel = []
        for f in current_fuel:
            next_fuel += [f // 3 - 2] if f // 3 - 2 > 0 else [0]
        fuel += next_fuel
        current_fuel = next_fuel
    solution_two = sum(fuel)
    print(solution_one)
    print(solution_two)

except FileNotFoundError:
    print('This file does not exist')
