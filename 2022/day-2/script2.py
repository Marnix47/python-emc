#rsp, ACBXZY
results1 = []

inputFile = open("input.txt").readlines()
inputC = []
for line in inputFile:
	t = line.split(" ")
	t[1] = t[1].replace("\n", "")
	inputC.append(t)

def getDefs(m,n):
	indexes = "ACBXZY"
	opp = indexes.index(m) + 2
	return opp

def getMatch(m,n):
	indexes = "CBACBAC"
	result = 0
	choice = 0
	if n == "X":
		choice = indexes[m + 1]
		result = 0
	if n == "Y":
		choice = indexes[m]
		result = 3
	if n == "Z":
		choice = indexes[m - 1]
		result = 6
	return [choice, result]

def getPoints(n, result):
	points = result
	indexes = "*ABC"
	points += indexes.index(n)
	return points

def getIndex(u):
	indexes = "*ABC"
	return indexes[u]

for i in range(len(inputC)):
	t = inputC[i]
	opp = getDefs(t[0], t[1])
	c = getMatch(opp, t[1])
	#print(c[0])
	h = getPoints(c[0], c[1])
	#k = getPoints(getMatch(getDefs(inputC[i][0], inputC[i][1]), inputC[i][1])[0], getMatch(getDefs(inputC[i][0], inputC[i][1]), inputC[i][1])[1])
	#print(str(h) + "\n")
	results1.append(c[0])


results2 = []
for i in range(len(results1)):
	results2.append([inputC[i][0], results1[i]])

print(results2)




def getWinnert(n,m):
	win = "none"
	#candidates = [m,n]
	if m == n:
		win = "none"
	if m == 1:
		if n == 2:
			win = "opp"
		elif n == 3:
			win = "you"
	if m == 2:
		if n == 1:
			win = "you"
		elif n == 3:
			win = "opp"
	if m == 3:
		if n == 1:
			win = "opp"
		elif n == 2:
			win = "you"
	return win

def getPointst(n,m):
	defs = getDefst(n,m)
	win = getWinnert(defs[0], defs[1])
	points = 0
	if win == "you":
		points += 6
	elif win == "none":
		points += 3
	points += defs[1]
	return points

def getDefst(m,n):
	indexes = "*ABCXYZ"
	you = indexes.index(m)
	opp = indexes.index(n)
	return [you, opp]

inputC = results2

points = 0
for i in range(len(inputC)):
	t = getPointst(inputC[i][0], inputC[i][1])
	points += t
print(points)