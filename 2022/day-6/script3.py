input = open("input.txt").readlines()[0]
le = 4
stop = False

def create(i, l):
	string = ""
	for k in range(i, l + i):
		string += input[k]
	return string

def process(string):
	list = [""]*len(string)
	k = 0
	for i in range(len(string)):
		for g in range(len(string)):
			if not k == g:
				list[i] += string[g]
		k += 1
	return list

for i in range(len(input) - le):
	if stop == False:
		a = create(i,le)
		b = process(a)
		c = 0
		for k in range(len(b)):
			p = b[k]
			for g in range(i, i + le):
				if not input[g] in p:
					c += 1
		if c == le:
			print("hoi")
			print(i + le)
			stop = True