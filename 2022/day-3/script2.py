inputFile = open("input.txt").readlines()
iF = inputFile
inputs = []


for i in range(len(iF)):
	k = []
	if i % 3 == 0:
		for h in range(3):
			k.append(iF[i + h].replace("\n", ""))
		inputs.append(k)
#print(inputs)
#print(len(inputs))
commons = []
for i in range(len(inputs)):
	k = inputs[i]
	common = ""
	for h in range(len(k[0])):
		if k[0][h] in k[1] and k[0][h] in k[2]:
			common = k[0][h]
	commons.append(common)
print(commons)

upC = "*ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowC = "*abcdefghijklmnopqrstuvwxyz"
total = 0
for i in range(len(commons)):
	value = 0
	c = commons[i]
	if c in upC:
		value = upC.index(c) + 26
	if c in lowC:
		value = lowC.index(c)
	total += value
print(total)