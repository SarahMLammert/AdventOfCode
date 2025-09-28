'''Day 3
Help Santa Keep Track of Where Gifts Have Been Given

Santa moves based on four arrows
^ up
< left
> right
v down

Part 1: Find how many houses Santa visited more than once

Part 2: Find how many houses Santa and Robot visited more than once together
'''

try:
    position = [0, 0]
    santa_pos = [0, 0]
    robot_pos = [0, 0]
    d = {tuple([0, 0]):1}
    d_santa_robot = {tuple([0, 0]):2}
    turn = santa_pos

    # Open and read the file
    with open('day3.txt', encoding='utf-8') as file:
        filetext = file.read()

    # Follow instructions
    for direction in filetext:
        if direction == "^":
            position[1] += 1
            turn[1] += 1
        elif direction == ">":
            position[0] += 1
            turn[0] += 1
        elif direction == "<":
            position[0] -= 1
            turn[0] -= 1
        else: # Down
            position[1] -= 1
            turn[1] -= 1

        if tuple(position) in d:
            d[tuple(position)] += 1
        else:
            d[tuple(position)] = 1

        if tuple(turn) in d_santa_robot:
            d_santa_robot[tuple(turn)] += 1
        else:
            d_santa_robot[tuple(turn)] = 1

        if turn == santa_pos:
            turn = robot_pos
        else:
            turn = santa_pos

    total1 = sum(1 for i in d.values() if i >= 1)
    print(total1)

    total2 = sum(1 for i in d_santa_robot.values() if i >= 1)
    print(total2)

except FileNotFoundError:
    print('This file does not exist')
