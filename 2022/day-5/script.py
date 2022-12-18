inputFile = open("input.txt").readlines()
def doSomething():
	return 0

chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
values = [[]]*26


c = 0
d = 0

for line in inputFile:
	c += 1
	if "move" in line:
		doSomething()
	elif not line == "\n" and not " 1   2   3" in line:
		d += 1
		for i in range(len(line)):
			k = line[i]
			if (i - 1) % 3 == 0 and k in chars:
				values[i].append(k)
print(values)
print(c)
print(d)