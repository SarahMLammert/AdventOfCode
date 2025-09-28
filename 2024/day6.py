grid = []
start = [0,0]
onmap = True
directions = ['<', '>', '^', 'v']
with open('day6.txt') as file:
	for line in file:
		grid.append(list(line.rstrip()))

start = [0, 0]
rows = len(grid)
columns = len(grid[0])
for r in range(rows):
	for c in range(columns):
		if grid[r][c] in directions:
			start = [r, c] # index

direction = grid[start[0]][start[1]]

while onmap:

	grid[start[0]][start[1]] = 'X'

	if direction == '<':
		start = [start[0], start[1]-1]
		if (start[0] < 0 or
		start[0] >= rows or
		start[1] < 0 or
		start[1] >= columns):
			onmap = False
		elif grid[start[0]][start[1]] == '#':
			start = [start[0], start[1]+1]
			direction = '^'

	elif direction == '^':
		start = [start[0]-1, start[1]]
		if (start[0] < 0 or
		start[0] >= rows or
		start[1] < 0 or
		start[1] >= columns):
			onmap = False
		elif grid[start[0]][start[1]] == '#':
			start = [start[0]+1, start[1]]
			direction = '>'

	elif direction == '>':
		start = [start[0], start[1]+1]
		if (start[0] < 0 or
		start[0] >= rows or
		start[1] < 0 or
		start[1] >= columns):
			onmap = False
		elif grid[start[0]][start[1]] == '#':
			direction = 'v'
			start = [start[0], start[1]-1]

	else:
		start = [start[0]+1, start[1]]
		if (start[0] < 0 or
		start[0] >= rows or
		start[1] < 0 or
		start[1] >= columns):
			onmap = False
		elif grid[start[0]][start[1]] == '#':
			direction = '<'
			start = [start[0]-1, start[1]]

sum = 0
for r in range(rows):
	for c in range(columns):
		if grid[r][c] == 'X':
			sum += 1
#print(sum)


grid = []
start = [0,0]
onmap = True
directions = ['<', '>', '^', 'v']
with open('day6.txt') as file:
	for line in file:
		grid.append(list(line.rstrip()))

start = [0, 0]
rows = len(grid)
columns = len(grid[0])


for r in range(rows):
	for c in range(columns):
		if grid[r][c] in directions:
			start = [r, c] # index
direction = grid[start[0]][start[1]]
answer = []

for r in range(rows):
	for c in range(columns):
		positions = {}
		if r != start[0] or c != start[1] and grid[r][c] != '#':
			temp = grid[r][c]
			grid[r][c] = '#'
			onmap = True
			for i in grid:
				print(i)
			print()
			while onmap:
				if (start[0],start[1],direction) in positions:
					answer.append([r,c])
					onmap = False
				else:
					positions[(start[0],start[1],direction)] = True
					if direction == '<':
						start = [start[0], start[1]-1]
						if (start[0] < 0 or
						start[0] >= rows or
						start[1] < 0 or
						start[1] >= columns):
							onmap = False
						elif grid[start[0]][start[1]] == '#':
							start = [start[0], start[1]+1]
							direction = '^'

					elif direction == '^':
						start = [start[0]-1, start[1]]
						if (start[0] < 0 or
						start[0] >= rows or
						start[1] < 0 or
						start[1] >= columns):
							onmap = False
						elif grid[start[0]][start[1]] == '#':
							start = [start[0]+1, start[1]]
							direction = '>'

					elif direction == '>':
						start = [start[0], start[1]+1]
						if (start[0] < 0 or
						start[0] >= rows or
						start[1] < 0 or
						start[1] >= columns):
							onmap = False
						elif grid[start[0]][start[1]] == '#':
							direction = 'v'
							start = [start[0], start[1]-1]

					else:
						start = [start[0]+1, start[1]]
						if (start[0] < 0 or
						start[0] >= rows or
						start[1] < 0 or
						start[1] >= columns):
							onmap = False
						elif grid[start[0]][start[1]] == '#':
							direction = '<'
							start = [start[0]-1, start[1]]
			grid[r][c] = temp
print(answer)