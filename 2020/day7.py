'''Day 7'''

try:
    solution_one = 0
    solution_two = 0
    d = {}

    with open('day7.txt', encoding='utf-8') as file:
        filetext = file.readlines()

    for line in filetext:
        strip = line.strip().strip('.').split(' contain ')
        fits = []
        for bags in strip[1:]:
            bags = bags.split(', ')
            for b in bags:
                b = b.split(' ')
                if b[0] == 'no':
                    fits += [(0, b[0] + ' ' + b[1])]
                else:
                    fits += [(int(b[0]), b[1] + ' ' + b[2])]
        d[strip[0][:-5]] = fits
    for key, value in d.items():
        print(key, value)
    print(solution_one)
    print(solution_two)

except FileNotFoundError:
    print('This file does not exist')
