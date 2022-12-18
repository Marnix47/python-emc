inputFile = open("input.txt").readlines()

def check(a,b,c,d):
	t = False
	if a <= c and b >= c:
		t = True
	elif c <= a and d >= a:
		t = True
	
	return t


lines = []
for line in inputFile:
	k = line.split(",")
	h = []
	for i in k:
		h.append(int(i.split("-")[0].replace("\n", "")))
		h.append(int(i.split("-")[1].replace("\n", "")))
	lines.append(h)
#print(lines)

count = 0
for line in lines:
	k = line
	if check(k[0], k[1], k[2], k[3]) == True:
		count += 1
print(count)