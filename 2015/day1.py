'''Day 1
Help Santa Follow Instructions to Deliver Presents

Santa moves up and down floors based on instructions
( means up
) means down

Part 1: Find the floor that the instructions send Santa to

Part 2: Find the position of the character that causes Santa to enter the basement
'''

try:
    # Variables to keep track of
    floor = 0 # pylint: disable=C0103
    char_position = 0 # pylint: disable=C0103

    # Open and read the file
    with open('day1.txt', encoding='utf-8') as file:
        filetext = file.read()

    # Follow the instructions
    for c in filetext:
        char_position += 1
        if c == "(":
            floor += 1
        elif c == ")":
            floor -= 1
        if floor == -1:
            print(char_position)
    print(floor)

except FileNotFoundError:
    print('This file does not exist')
