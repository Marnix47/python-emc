inputFile = open("input.txt").readlines()
chars = "ABCDEFGHIJKLMNOPQRESTUVWXYZ"

cont = inputFile[0:8]
#print(cont)
input = inputFile[10:]

list = []
for i in range(9):
	list.append([])
#print(list)

for line in cont:
	#print(line)
	for i in range(len(line)):
		k = line[i]
		if k in chars:
			list[int((i - 1) / 4)].append(k)
#print(list)

for i in range(len(list)):
	list[i].reverse()
print(list)
commands = []

for c in input:
	k = c.split(" ")
	k.remove("move")
	k.remove("from")
	k.remove("to")
	k[2] = k[2].replace("\n", "")
	g = []
	for r in k:
		g.append(int(r))
	commands.append(g)
#print(commands)

for c in commands:
	#print(c)
	d = c[0]
	e = c[1]
	f = c[2]
	#print(d)

	for i in range(d):
		#print(i)
		list[f - 1].append(list[e - 1][-1])
		#print(e)
		#print(list[e - 1])
		list[e - 1].pop(-1)
print(list)
output = ""
for i in list:
	output += i[-1]
print(output)