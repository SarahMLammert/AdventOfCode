# Open file and place the two columns into two lists
floor = 0
position = 0
try:
	file = open('day1.txt')
	filetext = file.read()
	for c in filetext:
		position += 1
		if c == "(":
			floor += 1
		elif c == ")":
			floor -= 1
		if floor == -1:
			print(position)

except FileNotFoundError:
	print('This file does not exist')

print(floor)