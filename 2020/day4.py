'''Day 4'''

import re

try:
    solution_one = 0
    solution_two = 0
    passports = []
    current_passort = []
    reqs = {'byr': "(19(?:2[0-9]|[3-9][0-9])|200[0-2])",
            'iyr': "(2010|201[1-9]|2020)",
            'eyr': "(2020|202[1-9]|2030)",
            'hgt': "((?:1(?:5[0-9]|[6-8][0-9])|19[0-3])cm|(?:59|6[0-9]|7[0-6])in)",
            'hcl': "#[0-9a-f]{6}",
            'ecl': "(amb|blu|brn|gry|grn|hzl|oth)",
            'pid': r"\d{9}",
            'cid': ".*"}

    with open('day4.txt', encoding='utf-8') as file:
        filetext = file.readlines()

    for line in filetext:
        strip = line.strip()
        if strip != "":
            current_passort.append(strip)
        else:
            passports += [' '.join(current_passort)]
            current_passort = []
    
    for p in passports:
        ls = p.split(' ')
        ls = {i[0:3]:i[4:] for i in ls}
        if len(set(ls) & set(reqs)) == 8 or (len(set(ls) & set(reqs)) == 7 and not 'cid' in set(ls)):
            solution_one += 1
            match = True
            for k, v in ls.items():
                if not bool(re.fullmatch(reqs[k], v)):
                    match = False
            if match:
                solution_two += 1

    print(solution_one)
    print(solution_two)

except FileNotFoundError:
    print('This file does not exist')
