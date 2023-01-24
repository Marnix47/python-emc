import math

inputFile = open("input.txt").readlines()
for i in range(len(inputFile)):
	inputFile[i] = inputFile[i].strip() 

commands = []

for com in inputFile:
	if com == "noop":
		commands.append(0)
	else:
		com = int(com.replace("addx ", ""))
		commands.append(0)
		commands.append(com)

tC = 1
answerCount = 0

l = int(len(commands) / 40)
rows = ["" for _ in range(l)]
print(rows)
#sprite = [0,1,2]
for i in range(len(commands)):
	k = math.floor(i / 40)
	print(k)
	alt_i = i - k * 40
	if tC <= alt_i + 1 and tC >= alt_i - 1:
		rows[k] += "#"
	else:
		rows[k] += "."
	tC += commands[i]
for i in range(6):
	print(rows[i])
	