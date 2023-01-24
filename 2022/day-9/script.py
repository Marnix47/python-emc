inputFile = open("input.txt").readlines()
l = len(inputFile)
for i in range(l):
	inputFile[i] = inputFile[i].strip()

positions = {"0.00.0"}
commands = []

head = [0,0]
tail = [0,0]

dirs = {
	"R": [1,0],
	"L": [-1,0],
	"U": [0,1],
	"D": [0,-1]
}

for i in range(l):
	k = inputFile[i].split(" ")
	commands.append([k[0], int(k[1])])

def touching():
	global head, tail
	return abs(head[0] - tail[0]) <= 1 and abs(head[1] - tail[1]) <= 1

def move(delta):
	global head
	global tail
	head[0] += delta[0]
	head[1] += delta[1]
	if not touching():
		sign_x = 0 if head[0] == tail[0] else (head[0] - tail[0]) / abs(head[0] - tail[0])
		sign_y = 0 if head[1] == tail[1] else (head[1] - tail[1]) / abs(head[1] - tail[1])

		tail[0] += sign_x
		tail[1] += sign_y
for com in commands:
	for _ in range(com[1]):
		move(dirs[com[0]])
		positions.add(str(float(tail[0])) + str(float(tail[1])))

print(len(positions))