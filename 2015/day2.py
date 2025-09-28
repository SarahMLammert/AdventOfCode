'''Day 2
Help the Elves with Ordering the Right Amount of Wrapping Paper

Elves give gift sizes
length x width x height

Part 1: Find the total square feet of wrapping paper to order for the gifts

Part 2: Find the total feet of ribbon
'''

try:
    # Variables to keep track of
    wrapping_paper = 0 # pylint: disable=C0103
    ribbon = 0 # pylint: disable=C0103

    # Open and read the file
    with open('day2.txt', encoding='utf-8') as file:
        for line in file:
            l = line.strip()
            l = l.split("x") # Need to cut out the 'x'
            l = list(map(int, l))
            wrapping_paper += l[0] * l[1] * l[2] / max(l)
            wrapping_paper += 2 * ((l[0] * l[1]) + (l[1] * l[2]) + (l[0] * l[2]))
            ribbon += (l[0]*l[1]*l[2]) + 2*(l[0]+l[1]+l[2]-max(l))
    print(int(wrapping_paper))
    print(int(ribbon))

except FileNotFoundError:
    print('This file does not exist')
