inputFile = open("input.txt").readlines()
l = len(inputFile[0].strip("\n"))

grid = [[]*l for _ in range(l)]
visible = [[False]*l for _ in range(l)]
for i in range(len(inputFile)):
	line = inputFile[i]
	k = line.strip("\n")
	for char in k:
		grid[i].append(int(char))
#print(grid)

def checkHor(i, list, p):
	highest = -1
	global visible
	for k in range(len(list)):
		if list[k] > highest:
			highest = list[k]
			visible[i][k] = True


for i in range(len(grid)):
	hor = grid[i]
	checkHor(i, hor, 0)
	hor.reverse()
	visible[i].reverse()
	checkHor(i, hor, l)
	hor.reverse()
	visible[i].reverse()

verList = []
for i in range (len(grid)):
	thisList = []
	for k in range(len(grid)):
		thisList.append(grid[k][i])
	verList.append(thisList)
#print(verList)

verVis = []
for i in range (len(grid)):
	thisList = []
	for k in range(len(grid)):
		thisList.append(visible[k][i])
	verVis.append(thisList)


def checkVer(i, list):
	highest = -1
	global visible
	for k in range(len(list)):
		if list[k] > highest:
			highest = list[k]
			verVis[i][k] = True

for i in range(l):
	ver = verList[i]
	checkVer(i, ver)
	ver.reverse()
	verVis[i].reverse()
	checkVer(i,ver)
	ver.reverse()
	verVis[i].reverse()
#print(visible)
c = 0
for i in range(l):
	for k in range(l):
		if verVis[i][k]:
			c += 1
print(c)