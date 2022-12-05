input = open("input2.txt").readlines()[0].split(" ")



inp = [[]]*len(input)

for i in range (0, len(input)):
	inp[i] = input[i].split("x")

tot = 0

for i in range (len(input)):
	a = int(inp[i][0])
	b = int(inp[i][1])
	c = int(inp[i][2])

	ac = a * c
	ab = a * b
	bc = b * c

	things = [ab, ac, bc]

	tot += ab * 2 + ac * 2 + bc * 2

	smallest = things[0]
	for k in range (0, 3):
		if smallest > things[k]:
			smallest = things[k]
	tot += smallest
	#1598415
		
print(str(tot))

total = 0

for i in range (len(input)):
	a = int(inp[i][0])
	b = int(inp[i][1])
	c = int(inp[i][2])
	d = 0

	thingssep = [a,b,c]
	
	highest = thingssep[0]
	for k in range (0,3):
		if highest < thingssep[k]:
			highest = thingssep[k]
	if highest == a:
		d = 2 * b  + 2 * c
	elif highest == b:
		d = 2 * a + 2 * c
	elif highest == c:
		d = 2 * a + 2 * b
	total += d
	total += a * b * c
print(str(total))
#3812909