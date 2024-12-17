import re

sum = 0

def multiply(s):
	s = s[4:-1]
	s = s.split(',')
	s = [int(i) for i in s]
	return s[0] * s[1]
try:
	file = open('day3.txt')
	s = ''
	for line in file:
		s += line
	s = re.findall("mul\\([0-9]{0,3},[0-9]{0,3}\\)", s)
	for line in s:
		sum += multiply(line)
except FileNotFoundError:
	print('This file does not exist')

print(sum)


sumS = 0

def multiply(s):
	s = s[4:-1]
	s = s.split(',')
	s = [int(i) for i in s]
	return s[0] * s[1]
try:
	mult = True
	file = open('day3.txt')
	s = ''
	for line in file:
		s += line
	s = re.findall("mul\\([0-9]{0,3},[0-9]{0,3}\\)|do\\(\\)|don\'t\\(\\)", s)
	for line in s:
		if line == "do()":
			mult = True
		elif line == "don't()":
			mult = False
		elif mult:
			sumS += multiply(line)
except FileNotFoundError:
	print('This file does not exist')

print(sumS)