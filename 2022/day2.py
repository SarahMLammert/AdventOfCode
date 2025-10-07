'''Day 2'''

try:
    scores_dict = {'A':1, 'B':2, 'C':3}
    transfer = {'X':'A', 'Y':'B', 'Z':'C'}
    solution_one = 0
    solution_two = 0
    with open('day2.txt', encoding='utf-8') as file:
        filetext = file.readlines()
    for line in filetext:
        line = line.split(' ')
        line[1] = line[1][0].strip()
        line[1] = transfer[line[1]]
        solution_one += scores_dict[line[1]]
        if line[0] == line[1]:
            solution_one += 3
        elif (line[0] == 'A' and line[1] == 'B') or (line[0] == 'B' and line[1] == 'C') or (line[0] == 'C' and line[1] == 'A'):
            solution_one += 6
        else:
            solution_one += 0

        if line[1] == 'B':
            line[1] = line[0]
        elif line[1] == 'A':
            match line[0]:
                case 'A':
                    line[1] = 'C'
                case 'B':
                    line[1] = 'A'
                case 'C':
                    line[1] = 'B'
        else:
            match line[0]:
                case 'A':
                    line[1] = 'B'
                case 'B':
                    line[1] = 'C'
                case 'C':
                    line[1] = 'A'

        solution_two += scores_dict[line[1]]
        if line[0] == line[1]:
            solution_two += 3
        elif (line[0] == 'A' and line[1] == 'B') or (line[0] == 'B' and line[1] == 'C') or (line[0] == 'C' and line[1] == 'A'):
            solution_two += 6
        else:
            solution_two += 0

    print(solution_one)
    print(solution_two)
except FileNotFoundError:
    print('This file does not exist')
