input = open("inputTest.txt").readlines()[0]
stop = False


	
for i in range(len(input) - 4):
	a = input[i + 0]
	b = input[i + 1]
	c = input[i + 2]
	d = input[i + 3]
	k = a + b + c + d
	
	if (not a == b) and (not a == c) and (not a == d) and (not b == c) and (not b == d) and (not c == d):
		if(stop == False):
			print(a + b + c + d)
			print(i + 4)
			stop = True

