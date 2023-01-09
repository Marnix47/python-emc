inputFile = open("input2.txt").readlines()
l = len(inputFile)
positions = set(([0,0]))
commands = []
print(l)

for i in range(l):
	k = inputFile[i].split(" ")
	commands.append([k[0], int(k[1])])

head = [0,0]
tail = [0,0]
dirs = {
	"R": (1,0),
	"L": (-1,0),
	"U": (0,1),
	"D": (0,-1)
}

def getDelta(type):
	global head, tail
	return [abs(head[0] - tail[0]), abs(head[1] - tail[1])] if type == "p" else [head[0] - tail[0], head[1] - tail[1]]

def checkIfHasToMove():
	global head, tail
	positiveDelta = getDelta("p")
	if head == tail:
		return False
	elif 2 in positiveDelta:
		return True
	elif 1 in positiveDelta:
		return False
	else:
		return True

def checkIfDiagonal():
	return 2 in getDelta("p") and 1 in getDelta("p")

def checkIf1():
	if 1 in getDelta("p"):
		return False
	else:
		return True


def moveHead(direction):
	head[0] += dirs[direction][0]
	head[1] += dirs[direction][1]

def moveDiagonal():
	global head, tail
	d = getDelta("n")
	if d[0] < 0:
		tail[0] -= 1
	else:
		tail[0] += 1
	if d[1] < 0:
		tail[1] -= 1
	else:
		tail[1] += 1

def follow(direction):
	tail[0] += dirs[direction][0]
	tail[1] += dirs[direction][1]


for i in range(l):
	c = commands[i]
	for k in range(c[1]):
		moveHead(c[0])
		print(tail)
		print("nd")
		if not head == tail:
			if checkIfDiagonal():
				print("diagonal")
				moveDiagonal() 
			elif checkIf1():
				follow(c[0])
				print("follow")
	positions.add(tail)
print(tail)
print(len(positions))
			
			
	