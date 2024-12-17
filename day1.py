# Store both lists to compare
list1 = []
list2 = []

# Open file and place the two columns into two lists
try:
	file = open('day1.txt')
	for l in file:
		line = l.split()
		list1.append(int(line[0]))
		list2.append(int(line[1]))
except FileNotFoundError:
	print('This file does not exist')

# Sort the lists for comparison
list1.sort()
list2.sort()

# Sum up the differences
sum = 0
for i in range(len(list1)):
	sum += abs(list1[i] - list2[i])
print(sum)

# Count all instances of items in the second list
d = {}
for i in list2:
	if i in d:
		d[i] += 1
	else:
		d[i] = 1

# Sum up similarities
similarity = 0
for i in range(len(list1)):
	if list1[i] in d:
		similarity += d[list1[i]] * list1[i]
print(similarity)

