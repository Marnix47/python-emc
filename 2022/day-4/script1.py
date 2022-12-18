 inputFile = open("input.txt").readlines()
lines = []

for line in inputFile:
	k = line.split(",")
	j = []
	for g in k:
		h = g.split("-")
		j.append([int(h[0]) ,int(h[1].replace("\n", ""))])
	lines.append(j)
#print(lines)

def check(a,b,c,d):
	overlap = False
	if (b - a) > (d - c):
		if a <= c and b >= d:
			overlap = True
	elif (b - a) < (d - c):
		if a >= c and b <= d:
			overlap = True
	elif (b - a) == (d - c):
		if a == c:
			overlap = True
		else:
			overlap = False
	else:
		overlap = False
	return overlap

c = 0
for i in range(len(lines)):
	k = lines[i][0] + lines[i][1]
	if check(k[0], k[1], k[2], k[3]) == True:
		c += 1
print(c)