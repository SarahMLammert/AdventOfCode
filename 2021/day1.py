'''Day 7'''

try:
    solution_one = 0
    solution_two = 0

    with open('day1.txt', encoding='utf-8') as file:
        filetext = file.readlines()
    previous_num = int(filetext[0])
    for line in filetext[1:]:
        current_num = int(line.strip())
        if current_num > previous_num:
            solution_one += 1
        previous_num = current_num

    print(solution_one)
    print(solution_two)

except FileNotFoundError:
    print('This file does not exist')
