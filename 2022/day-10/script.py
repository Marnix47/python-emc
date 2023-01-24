inputFile = open("input.txt").readlines()
for i in range(len(inputFile)):
	inputFile[i] = inputFile[i].strip() 
"""
noop: 1 cycle, 0 erbij
addx 3: 2 cycles, 3 erbij
addx -5: 2 cycles, 5 eraf
Dus:
[0,0,3,0,-5]
Instructies omzetten in List?
"""
commands = []

for com in inputFile:
	if com == "noop":
		commands.append(0)
	else:
		com = int(com.replace("addx ", ""))
		commands.append(0)
		commands.append(com)

totalCount = 1
answerCount = 0
for i in range(len(commands)):
	if (i + 21) % 40 == 0:
		answerCount += (i + 1) * totalCount
	totalCount += commands[i]
print(answerCount)
