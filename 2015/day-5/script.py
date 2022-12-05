inputFile = open("input.txt").readlines()

input = inputFile

vowels = ['a', 'e', 'i', 'o', 'u']
letters = "abcdefghijklmnopqrstuvwxyz"
forbidden = ['ab', 'cd', 'pq', 'xy']

nice = 0
same1 = 0
same = 0
same3 = 0

for i in range(len(input)):
	conditions = 0
	n = input[i]
	tot = 0
	for k in range(5):
		h = 0
		try:
		  h = n.index(vowels[k])
		except:
			tot += 0
		else:
			tot += 1
			try:
				u = n.index(vowels[k], h)
			except:
				tot += 0
			else:
				tot += 1
				try:
					z = n.index(vowels[k], u)
				except:
					tot += 0
				else:
					tot += 1
	if tot >= 3:
		conditions += 1
		same1 += 1

	
	ln = "["
	stop2 = False
	for k in range(len(n)):
		if not stop2:
			qn = n[k]
			if qn == ln:
				same += 1
				conditions += 1
				stop2 = True
			ln = n[k]

	stop3 = False
	c3 = 0
	for k in range(len(forbidden)):
		try:
			t = n.index(forbidden[k])
		except:
			c3 += 1
		else:
			stop3 = True
			
	if c3 == 4:
		conditions += 1
		same3 += 1

	if conditions == 3:
		nice += 1
	

print(nice)
print(same1)
print(same)
print(same3)