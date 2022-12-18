#werkt niet, zie script22


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
	e = c[1] - 1
	f = c[2] - 1
	#print(d)
	g = list[e][-1 - d: -1]
	#print(list[f])
	#list[f].append(g)
	for q in g:
		list[f].append(q)
	#print(list[f])
	for t in range(d):

		list[e].pop(-1)
		print(list[e])
		
print(list)
output = ""
for i in list:
	output += i[-1]
print(output)