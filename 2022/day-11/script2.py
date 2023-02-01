import time
now = time.time()

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
commonR = 1
for i in range(len(monkeys)):
	monkey = monkeys[i]
	startItems = monkey[0].replace("Starting items: ", "").split(", ")
	operation = monkey[1].replace("Operation: ", "")
	test = int(monkey[2].replace("Test: divisible by ", ""))
	commonR *= test
	ifTrue = int(monkey[3].replace("If true: throw to monkey ", ""))
	ifFalse = int(monkey[4].replace("If false: throw to monkey ", ""))
	monkeys[i] = [startItems, operation, test, ifTrue, ifFalse]

inspectCount = [0 for _ in range(len(monkeys))]
for y in range(10000):
	for i in range(len(monkeys)):
		monkey = monkeys[i]
		for k in range(len(monkey[0])):
			inspectCount[i] += 1
			old = int(monkey[0][0])
			new = 0
			exec(monkey[1])
			new %= commonR
			
			if new % monkey[2] == 0:
				monkeys[monkey[3]][0].append(new)
			else:
				monkeys[monkey[4]][0].append(new)
			monkeys[i][0].pop(0)
print(time.time() - now)
results = sorted(inspectCount, reverse=True)
print(results)
ans = results[0] * results[1]
print(ans)