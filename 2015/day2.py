wpaper = 0
ribbon = 0
try:
	file = open('day2.txt')
	for line in file:
		l = line.strip()
		l = l.split("x")
		l = list(map(int, l))
		wpaper += 2*((l[0]*l[1]) + (l[1]*l[2]) + (l[0]*l[2])) + (l[0]*l[1]*l[2]/max(l))
		ribbon += (l[0]*l[1]*l[2]) + 2*(l[0]+l[1]+l[2]-max(l))

except FileNotFoundError:
	print('This file does not exist')
print(int(wpaper))
print(int(ribbon))