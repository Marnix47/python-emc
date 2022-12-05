inputFile = open("input.txt").readlines()

values = []
temp = []


for line in inputFile:
	if line == "\n":
		values.append(temp)
		temp = []
	else:
		t = int(line)
		temp.append(t)

totals = []
for list in values:
	count = 0
	for num in list:
		count += num
	totals.append(count)

highest = [0]*3
#highest = [0,0,0]

for num in totals:
	if num > highest[0]:
		highest[2] = highest[1]
		highest[1] = highest[0]
		highest[0] = num
	elif num > highest[1]:
		highest[2] = highest[1]
		highest[1] = num
	elif num > highest[2]:
		highest[2] = num
		
#werkt niet
print(highest)
print(highest[1] + highest[0] + highest[2])

