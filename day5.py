rules = []
updates = []
sum = 0
notPassedBlank = True
with open('day5.txt') as file:
	for line in file:
		if line == "\n":
			notPassedBlank = False
		elif notPassedBlank:
			rules.append(line.rstrip())
		else:
			updates.append(line.rstrip())
	for pages in updates:
		correct = True
		pages = pages.split(",")
		for rule in rules:
			newrule = rule.split("|")
			if(newrule[0] in pages and newrule[1] in pages):
				if(pages.index(newrule[1]) < pages.index(newrule[0])):
					correct = False
		if correct:
			sum += int(pages[len(pages)//2])
print(sum)

rules = []
updates = []
sum = 0
notPassedBlank = True
with open('day5.txt') as file:
	for line in file:
		if line == "\n":
			notPassedBlank = False
		elif notPassedBlank:
			rules.append(line.rstrip())
		else:
			updates.append(line.rstrip())
	for pages in updates:
		correct = True
		ncorrect = True
		pages = pages.split(",")
		for rule in rules:
			newrule = rule.split("|")
			if(newrule[0] in pages and newrule[1] in pages):
				if(pages.index(newrule[1]) < pages.index(newrule[0])):
					correct = False
					ncorrect = False
		newpages = pages
		while not(correct):
			correct = True
			for rule in rules:
				newrule = rule.split("|")
				if(newrule[0] in pages and
				   newrule[1] in pages and 
				   newpages.index(newrule[1]) < newpages.index(newrule[0])):
				   i1 = newpages.index(newrule[1])
				   i0 = newpages.index(newrule[0])
				   temp = newpages[i1]
				   newpages[i1] = newpages[i0]
				   newpages[i0] = temp
				   correct = False


		if not(ncorrect):
			sum += int(pages[len(pages)//2]) 
print(sum)