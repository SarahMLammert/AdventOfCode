'''Day 2'''

try:
    solution_one = ""
    solution_two = 0
    coord = [1, 1] # x y
    pad = [['1','2','3'],['4','5','6'],['7','8','9']]
    with open('day2.txt', encoding='utf-8') as file:
        lines = file.readlines()

    for l in lines:
        for c in l:
            if c == 'U' and coord[1] >= 1:
                coord[1] -= 1
            elif c =='D' and coord[1] < 2:
                coord[1] += 1
            elif c == 'L' and coord[0] >= 1:
                coord[0] -= 1
            elif c == 'R' and coord[0] < 2:
                coord[0] += 1
        solution_one += pad[coord[1]][coord[0]]

    print(solution_one)
    print(solution_two)

except FileNotFoundError:
    print('This file does not exist')
