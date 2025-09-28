'''Day 4
Help Santa Mine AdventCoins

Santa gives an input

Part 1: Find the lowest positive number that combined with my input
produces a hash, starting with 5 zeros

Part 2: Find the lowest positive number that combined with my input
produces a hash, starting with 6 zeros
'''

from hashlib import md5

# Variables to keep track of
answer = 0 # pylint: disable=C0103
puzzle_input = 'iwrupvqb' # pylint: disable=C0103

while True:
    answer += 1
    hex_hash = md5((puzzle_input + str(answer)).encode()).hexdigest() # pylint: disable=C0103
    if hex_hash[:5] == '00000':
        print(answer)
        if hex_hash[5] == '0':
            print(answer)
            break
