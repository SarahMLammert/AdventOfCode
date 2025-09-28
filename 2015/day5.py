nicestrings = 0
vowels = "aeiou"

try:
	file = open('day5.txt')
	for line in file:
		l = line.strip()
		numvowels = 0
		double = False
		killswitch = False
		if l[-1] in vowels:
			numvowels += 1
		for i in range(len(l)-1):
			if l[i] in vowels:
				numvowels += 1
			if l[i] == l[i+1]:
				double = True
			if (l[i] == "a" and l[i+1] == "b" or l[i] == "c" and l[i+1] == "d" 
			  or l[i] == "p" and l[i+1] == "q" 
			  or l[i] == "x" and l[i+1] == "y"):
			  killswitch = True
		if not killswitch and numvowels >= 3 and double:
			nicestrings += 1
except FileNotFoundError:
	print('This file does not exist')

print(nicestrings)