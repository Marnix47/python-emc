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
	#print(currentPath)
	
	if line[0] == "$":
		if line[2:4] == "cd":
			if line[5:7] == "..":
				#print(line)
				#print(currentPath)
				removePath()
				#print("removed")
			else:
				currentPath.append(line[5:])
				addDir()
	if line[0] in nums:
		num = getNumber(line)
		assignValue(num)
		
#print(paths)

c = 0
for x in paths:
	# print(x)
	# print(paths[x])
	# for y in paths:
	# 	if y in x and not x == y:
	# 		paths[x] += paths[y]
	# 	elif x == y:
	# 		c += 1
	# 		#paths[y] = paths[x]
	for y in paths:
		if y in x and not y == x:
			paths[y] += paths[x]

print(paths)
print(c)
print(len(paths))

lowValues = 0

for x in paths:
	if paths[x] <= 100000:
		lowValues += paths[x]
		print(paths[x])
print(lowValues)