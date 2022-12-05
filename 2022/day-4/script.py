inputFile = open("inputText.txt").readlines()
lines = []

for line in inputFile:
	k = line.split(",")
	j = []
	for g in k:
		h = g.split("-")
		j.append([h[0],h[1].replace("\n", "")])
	lines.append(j)
#print(lines)

h = []
for line in lines:
	d = []
	p = []
	k = line
	d.append(k[0][0] >= k[1][0] and k[0][0] <= k[1][1])
	d.append(k[0][1] <= k[1][1] and k[0][1] >= k[1][0])
	if d[0] == d[1] and d[0] == True:
		p.append(True)
	else:
		p.append(False)
	d = []
	d.append(k[1][0] >= k[0][0] and k[0][1] <= k[1][0])
	d.append(k[1][1] <= k[0][1] and k[0][0] >= k[1][1])
	if d[0] == d[1] and d[0] == True:
		p.append(True)
	else:
		p.append(False)
	
	h.append(p)
print(h)

ov = 0
for g in h:
	
	if True in g:
		#print("overlap")
		ov += 1

print(ov)

#404 werkt niet
#481 ook te laag