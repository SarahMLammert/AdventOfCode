position = [0, 0]
santapos = [0, 0]
robopos = [0, 0]
d = {tuple([0, 0]):1}
dsandr = {tuple([0, 0]):2}
turn = santapos
try:
	file = open('day3.txt')
	filetext = file.read()
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
		else:
			position[1] -= 1
			turn[1] -= 1

		if tuple(position) in d:
			d[tuple(position)] += 1
		else:
			d[tuple(position)] = 1

		if tuple(turn) in dsandr:
			dsandr[tuple(turn)] += 1
		else:
			dsandr[tuple(turn)] = 1

		if turn == santapos:
			turn = robopos
		else:
			turn = santapos
except FileNotFoundError:
	print('This file does not exist')

total1 = sum(1 for i in d.values() if i >= 1)
print(total1)

total2 = sum(1 for i in dsandr.values() if i >= 1)
print(total2)