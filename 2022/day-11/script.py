import math

inputFile = open("input.txt").readlines()
for i in range(len(inputFile)):
	inputFile[i] = inputFile[i].strip()

queue = []
monkeys = []
for i in range(len(inputFile)):
	if inputFile[i] == "":
		monkeys.append(queue)
		queue = []
	elif not "Monkey" in inputFile[i]:
		queue.append(inputFile[i])
monkeys.append(queue)
for i in range(len(monkeys)):
	monkey = monkeys[i]
	startItems = monkey[0].replace("Starting items: ", "").split(", ")
	operation = monkey[1].replace("Operation: ", "")
	test = int(monkey[2].replace("Test: divisible by ", ""))
	ifTrue = int(monkey[3].replace("If true: throw to monkey ", ""))
	ifFalse = int(monkey[4].replace("If false: throw to monkey ", ""))
	monkeys[i] = [startItems, operation, test, ifTrue, ifFalse]
#print(monkeys)

inspectCount = [0 for _ in range(len(monkeys))]
for i in range(20):
	#toMonkeys = [[] for _ in range(len(monkeys))]
	for i in range(len(monkeys)):
		monkey = monkeys[i]
		for k in range(len(monkey[0])):
			inspectCount[i] += 1
			item = monkey[0][0]
			#print(item)
			old = int(item)
			new = 0
			exec(monkey[1])
			new = math.floor(new / 3)
			test = new % monkey[2] == 0
			#print(new)
			if test:
				#print(str(monkey[3]) + ":  " + str(new))
				monkeys[monkey[3]][0].append(new)
			else:
				#print(str(monkey[4]) + ":  " + str(new))
				monkeys[monkey[4]][0].append(new)
			monkeys[i][0].pop(0)
	#print("******************")
#print(monkeys)
#inspectCount = inspectCount.sort()
results = sorted(inspectCount, reverse=True)
print(results)
ans = results[0] * results[1]
print(ans)
