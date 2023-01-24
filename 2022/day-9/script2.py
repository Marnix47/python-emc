inputFile = open("input.txt").readlines()
l = len(inputFile)
for i in range(l):
	inputFile[i] = inputFile[i].strip()

positions = {"0.00.0"}
commands = []

dirs = {
	"R": [1,0],
	"L": [-1,0],
	"U": [0,1],
	"D": [0,-1]
}

for i in range(l):
	k = inputFile[i].split(" ")
	commands.append([k[0], int(k[1])])

knots = [[0,0]for _ in range(10)]
# knots[0] is head, knots[9] is tail
def touching(knotIndex):
	global knots
	head = knots[knotIndex]
	tail = knots[knotIndex+1]
	return abs(head[0] - tail[0]) <= 1 and abs(head[1] - tail[1]) <= 1


def move(dir, knotIndex):
	global knots
	kI = knotIndex
	head = knots[kI]
	tail = knots[kI + 1]
	# hier ging het fout:
	# knots[kI][0] += dir[0]
	# knots[kI][1] += dir[1]
	if not touching(kI):
		sign_x = 0 if head[0] == tail[0] else (head[0] - tail[0]) / abs(head[0] - tail[0])
		sign_y = 0 if head[1] == tail[1] else (head[1] - tail[1]) / abs(head[1] - tail[1])
		
		knots[kI + 1][0] += sign_x
		knots[kI + 1][1] += sign_y


for com in commands:
	for i in range(com[1]):
		knots[0][0] += dirs[com[0]][0]
		knots[0][1] += dirs[com[0]][1]
		for k in range(9):
			move(dirs[com[0]], k)
			positions.add(str(float(knots[9][0])) + str(float(knots[9][1])))
print(len(positions))