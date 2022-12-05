inputFile = open("input.txt").readlines()
iF = inputFile
inputs = []

if 0 % 3 == 0:
	print("hoi")

for i in range(len(iF)):
	k = iF[i].replace("\n", "")
	l = int(len(k) /2)
	t = [k[:l], k[l:]]
	inputs.append(t)
	
commons = []
for i in range(len(inputs)):
	k = inputs[i]
	common = ""
	for h in range(len(k[0])):
		p = k[0][h]
		if k[0][h] in k[1]:
			common = k[0][h]
	commons.append(common)
#print(commons)

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