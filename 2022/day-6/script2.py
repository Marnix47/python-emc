#dit werkt niet, de goede staat in script3.py

input = open("inputTest.txt").readlines()[0]
le = 14
stop = False

def create(i, l):
	string = ""
	for k in range(i, l + i):
		string += input[k]
	#print(string)
		
	return string

def process(string):
	list = [""]*len(string)
	#print(len(string))
	#print(list)
	k = 0
	for i in range(len(string)):
		u = string[i]
		#print(u)
		for g in range(len(string)):
			#print(list[i])
			if not k == g:
				list[i] += string[g]
		k += 1
	#print(list)
	return list

for i in range(len(input) - le):
	if stop == False:
		
		p = create(i, le)
		q = process(p)
		string = input[i:i + le]
		#print(string)
		for k in range(len(q)):
			c = 0
			g = q[k]
			#print(g)
			for y in range(len(string)):
				if string[y] in g:
					c += 1
			#print(c)
			#print(le)
			print(c)
			if c < le:
				print(i + le)
				stop = True
#laatste stuk werkt totaal niet