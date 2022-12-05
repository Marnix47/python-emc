inputFile = open("input2.txt").readlines()

type = [""]*300
t = 0
for i in range(len(inputFile)):
	if "on" in inputFile[i]:
		#print("on")
		type[i] = "on"
	if "off" in inputFile[i]:
		type[i] = "off"
	if "toggle" in inputFile[i]:
		type[i] = "toggle"
#print(type)

values = [[[0,0],[0,0]]]*3
lit = [[]*1000]*1000

for i in range(len(inputFile)):
	t = inputFile[i].split("through")
	for k in range(len(t)):
		u = t[k]
		if type[i] == "on":
			u = u.replace("turn on","")
		if type[i] == "off":
			u = u.replace("turn off","")
		if type[i] == "toggle":
			u = u.replace("toggle","")
		u = u.replace(" ", "")
		w = u.split(",")
		values[i][k] = w
		print(values[i][k])
		print(w)
print(values)
print(values[0])
print(values[1])
print(values[2])
#print(values[3])
#print(values[4])