paths = {}
global currentPath
currentPath = []
nums = "0123456789"

def addDir():
	global currentPath
	k = ""
	for step in currentPath:
		k += step + "/"
	if not k in paths:
		paths[k] = 0

def removePath():
	global currentPath
	currentPath.pop()
	#print(currentPath)

def getNumber(line):
	k = line.index(" ")
	return int(line[:k])

def assignValue(num):
	global currentPath
	k = ""
	for step in currentPath:
		k+= step + "/"
	paths[k] += num


inputFile = open("input.txt").readlines()
input = []
for g in inputFile:
	input.append(g.replace("\n", ""))



for line in input:
	
	if line[0] == "$":
		if line[2:4] == "cd":
			if line[5:7] == "..":
				removePath()
			else:
				currentPath.append(line[5:])
				addDir()
	if line[0] in nums:
		num = getNumber(line)
		assignValue(num)

		
for x in paths:
	for y in paths:
		if y in x and not y == x:
			paths[y] += paths[x]

lowValues = []
emptyValue = 30_000_000 - (70_000_000 - paths["//"])


for x in paths:
	if paths[x] > emptyValue:
		lowValues.append(paths[x])


lowest = lowValues[0]
for v in lowValues:
	if v < lowest:
		lowest = v

print(lowest)