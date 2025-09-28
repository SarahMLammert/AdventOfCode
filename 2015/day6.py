'''Day 5
Help Santa Determine Naughty or Nice

Part 1: Find how many strings are nice under the old rules

Part 2: Find how many strings are nice under the new rules
'''

try:
    lone = [[0 for i in range(1000)] for j in range(1000)]
    ltwo = [[0 for i in range(1000)] for j in range(1000)]
    with open('day6.txt', encoding='utf-8') as file:
        for s in file:
            if s.startswith('turn on'):
                command = 'turn on'
                s = s[len('turn on'):]
            elif s.startswith('turn off'):
                command = 'turn off'
                s = s[len('turn off'):]
            else:
                command = 'toggle'
                s = s[len('toggle'):]
            first, second = s.split(" through ")
            x1, y1 = map(int, first.split(','))
            x2, y2 = map(int, second.split(','))

            for r in range(x1, x2+1):
                for c in range(y1, y2+1):
                    if command == 'turn on':
                        lone[r][c] = 1
                        ltwo[r][c] += 1
                    elif command == 'turn off':
                        lone[r][c] = 0
                        if ltwo[r][c] > 0:
                            ltwo[r][c] -= 1
                    else:
                        lone[r][c] = (lone[r][c] ^ 1)
                        ltwo[r][c] += 2
    print(sum(sum(row) for row in lone))
    print(sum(sum(row) for row in ltwo))
except FileNotFoundError:
    print('This file does not exist')

