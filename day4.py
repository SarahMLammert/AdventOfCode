wordsearch = []
with open('day4.txt') as file:
	for line in file:
		wordsearch.append(line.rstrip())

rows = len(wordsearch)
columns = len(wordsearch[0])
sum = 0
for r in range(rows):
	for c in range(columns):
		#NW
		if(r - 3 >= 0 and c - 3 >= 0):
			if(wordsearch[r][c] == "X" and 
			   wordsearch[r-1][c-1] == "M" and 
			   wordsearch[r-2][c-2] == "A" and 
			   wordsearch[r-3][c-3] == "S"):
				sum +=1
		#N
		if(r - 3 >= 0):
			if(wordsearch[r][c] == "X" and 
			   wordsearch[r-1][c] == "M" and 
			   wordsearch[r-2][c] == "A" and 
			   wordsearch[r-3][c] == "S"):
				sum +=1
		#NE
		if(r - 3 >= 0 and c + 3 < columns):
			if(wordsearch[r][c] == "X" and 
			   wordsearch[r-1][c+1] == "M" and 
			   wordsearch[r-2][c+2] == "A" and 
			   wordsearch[r-3][c+3] == "S"):
				sum +=1
		#E
		if(c + 3 < columns):
			if(wordsearch[r][c] == "X" and 
			   wordsearch[r][c+1] == "M" and 
			   wordsearch[r][c+2] == "A" and 
			   wordsearch[r][c+3] == "S"):
				sum +=1

		#SE
		if(r + 3 < rows and c + 3 < columns):
			if(wordsearch[r][c] == "X" and 
			   wordsearch[r+1][c+1] == "M" and 
			   wordsearch[r+2][c+2] == "A" and 
			   wordsearch[r+3][c+3] == "S"):
				sum +=1

		#S
		if(r + 3 < rows):
			if(wordsearch[r][c] == "X" and 
			   wordsearch[r+1][c] == "M" and 
			   wordsearch[r+2][c] == "A" and 
			   wordsearch[r+3][c] == "S"):
				sum += 1

		#SW
		if(r + 3 < rows and c - 3 >= 0):
			if(wordsearch[r][c] == "X" and 
			   wordsearch[r+1][c-1] == "M" and 
			   wordsearch[r+2][c-2] == "A" and 
			   wordsearch[r+3][c-3] == "S"):
				sum +=1

		#W
		if(c - 3 >= 0):
			if(wordsearch[r][c] == "X" and 
			   wordsearch[r][c-1] == "M" and 
			   wordsearch[r][c-2] == "A" and 
			   wordsearch[r][c-3] == "S"):
				sum +=1
#print(sum)


wordsearch = []
with open('day4.txt') as file:
	for line in file:
		wordsearch.append(line.rstrip())

rows = len(wordsearch)
columns = len(wordsearch[0])
sum = 0
for r in range(rows-2):
	for c in range(columns-2):
		if(wordsearch[r][c] == "M" and 
		   wordsearch[r+1][c+1] == "A" and 
		   wordsearch[r+2][c+2] == "S" and
		   wordsearch[r+2][c] == "M" and
		   wordsearch[r][c+2] == "S"):
			sum += 1
		if(wordsearch[r][c] == "M" and 
		   wordsearch[r+1][c+1] == "A" and 
		   wordsearch[r+2][c+2] == "S" and
		   wordsearch[r+2][c] == "S" and
		   wordsearch[r][c+2] == "M"):
			sum += 1
		if(wordsearch[r][c] == "S" and 
		   wordsearch[r+1][c+1] == "A" and 
		   wordsearch[r+2][c+2] == "M" and
		   wordsearch[r+2][c] == "M" and
		   wordsearch[r][c+2] == "S"):
			sum += 1
		if(wordsearch[r][c] == "S" and 
		   wordsearch[r+1][c+1] == "A" and 
		   wordsearch[r+2][c+2] == "M" and 
		   wordsearch[r+2][c] == "S" and
		   wordsearch[r][c+2] == "M"):
			sum += 1
print(sum)

