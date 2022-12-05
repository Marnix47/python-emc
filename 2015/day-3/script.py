inputFile = open("input.txt").readlines()[0]

s = []
rs = []

print((0 % 2) == 0)
#print(str(round(len(inputFile)/2)))

for n in range(len(inputFile)):
	if (n % 2) == 0:
		s.append(inputFile[n])
	else:
		rs.append(inputFile[n])
print(len(s))
print(len(rs))

pos = [[0,0]]
count = 1


x = 0
y = 0

for n in s:
	if n == '^':
		y += 1
	if n == "v":
		y -= 1
	if n == "<":
		x -= 1
	if n == ">":
		x += 1
	try:
		k = pos.index([x,y])
	except:
		count += 1
		pos.append([x,y])
	else:
		count += 0
print(count)
#2564

x = 0
y = 0

for n in rs:
	if n == "^":
		y += 1
	if n == "v":
		y -= 1
	if n == "<":
		x -= 1
	if n == ">":
		x += 1
	try:
		k = pos.index([x,y])
	except:
		count += 1
		pos.append([x,y])
	else:
		count += 0
print(count)