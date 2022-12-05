def getWinner(n,m):
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

def getPoints(n,m):
	defs = getDefs(n,m)
	win = getWinner(defs[0], defs[1])
	points = 0
	if win == "you":
		points += 6
	elif win == "none":
		points += 3
	points += defs[1]
	return points

def getDefs(m,n):
	indexes = "*ABCXYZ"
	you = indexes.index(m)
	opp = indexes.index(n) - 3
	return [you, opp]

inputFile = open("input.txt").readlines()
inputC = []
for line in inputFile:
	t = line.split(" ")
	t[1] = t[1].replace("\n", "")
	inputC.append(t)
	#inputC.append([line.split(" ")[0], line.split(" ")[1].replace("\n", "")])


points = 0
for i in range(len(inputC)):
	t = getPoints(inputC[i][0], inputC[i][1])
	points += t
print(points)