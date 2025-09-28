'''Day 5
Help Santa Determine Naughty or Nice

Santa gives strings

Old rules
Contain 3 vowels
One letter that appears twice in a row
Does not contain 'ab', 'cd', 'pq' or 'xy'

New rules
Contains two pairs of any two letters that are not overlapping
Contains a sandwich of any letter with one letter in between


Part 1: Find how many strings are nice under the old rules

Part 2: Find how many strings are nice under the new rules
'''
import re

try:
    rexpone = re.compile(
        r'^(?=(?:.*([a-z])\1))'
        r'(?=(?:.*[aeiou]){3,})'
        r'(?!.*(?:ab|cd|pq|xy))'
    )

    rexptwo = re.compile(
        r'^(?=.*([a-z]{2}).*\1)(?=.*([a-z]).\2)[a-z]+$'
    )

    with open('day5.txt', encoding='utf-8') as file:
        s = list([l.strip() for l in file])
    print(len(list(filter(rexpone.match, s))))
    print(len(list(filter(rexptwo.match, s))))

except FileNotFoundError:
    print('This file does not exist')
