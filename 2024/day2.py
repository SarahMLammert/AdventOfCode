# Keep track of safe
safe = 0

try:
	file = open('day2.txt')
	for l in file:
		safetrack = True
		line = l.split()
		line = [int(x) for x in line]
		if line[1] > line[0]:
			for i in range(len(line)-1):
				if not (line[i] < line[i+1] < line[i] + 4):
					safetrack = False
		else:
			for i in range(len(line)-1):
				if not (line[i] - 4 < line[i+1] < line[i]):
					safetrack = False
		if safetrack:
			safe += 1
	#print(safe)

except FileNotFoundError:
	print('This file does not exist')


# Keep track of safe
safe = 0

try:
	file = open('day2.txt')
	for l in file:
		safetrack = False
		line = l.split()
		line = [int(x) for x in line]
		lines = [line[:x] + line[x+1:] for x in range(len(line))]
		lines.append(line)

		for l in lines:
			safeline = True
			if l[1] > l[0]:
				for i in range(len(l)-1):
					if not (l[i] < l[i+1] < l[i] + 4):
						safeline = False
			else:
				for i in range(len(l)-1):
					if not (l[i] - 4 < l[i+1] < l[i]):
						safeline = False
			if safeline:
				safetrack = True
				break
		if safetrack:
			safe += 1
	print(safe)

except FileNotFoundError:
	print('This file does not exist')