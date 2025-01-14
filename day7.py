'''
from itertools import product
operators = ['*', '+']
expressions = []
with open('day7.txt') as file:
	for line in file:
		newline = line.rstrip().split(': ')
		expressions.append([newline[0], newline[1].split()])

c = []
for e in expressions:
	ops = list(product(operators, repeat=len(e[1])-1))
	for os in ops:
		sum = int(e[1][0])
		nums = e[1][1:]
		for o in os:
			if o == '*':
				sum *= int(nums[0])
			elif o == '+':
				sum += int(nums[0])
			nums = nums[1:]
		if sum == int(e[0]) and sum not in c:
			c.append(sum)

sum = 0
for x in c:
	sum += x
print(sum)
'''


from itertools import product
from functools import reduce
import operator
operators = ['*', '+', '||']
expressions = []
with open('day7.txt') as file:
	for line in file:
		newline = line.rstrip().split(': ')
		expressions.append([newline[0], newline[1].split()])

newexpression = []
for e in expressions:
	ops = list(product(operators, repeat=len(e[1])-1))
	for os in ops:
		newlist = list(reduce(operator.add, zip(e[1], os)))
		if len(e[1]) > len(os):
			newlist.append(e[1][-1])
		newexpression.append(newlist)

for e in newexpression:
	print(e)
	






