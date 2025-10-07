'''Day 5'''

try:

    with open('day5.txt', encoding='utf-8') as file:
        filetext = file.readlines()
    
    seat_ids = []
    seats = []
    all_seats = [(row, col) for row in range(128) for col in range(8)]
    for line in filetext:
        rows = [0, 127, 64]
        line = line.strip()
        for letter in line[:6]:
            if letter == 'F':
                rows[1] -= rows[2]
            else:
                rows[0] += rows[2]
            rows[2] //= 2
        row = rows[0] if line[6] == 'F' else rows[1]

        columns = [0, 7, 4]
        for letter in line[7:9]:
            if letter == 'L':
                columns[1] -= columns[2]
            else:
                columns[0] += columns[2]
            columns[2] //= 2
        col = columns[0] if line[9] == 'L' else columns[1]

        seat_ids += [row * 8 + col]
    solution_one = max(seat_ids)
    print(solution_one)
    solution_two = list(set(range(96, 912)) - set(seat_ids))[0]
    print(solution_two)
except FileNotFoundError:
    print('This file does not exist')
