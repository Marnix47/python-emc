inputFile = open("input.txt")
firstLine = inputFile.readlines()[0]
lines = firstLine
print(str(0))

i = 0
h = 0
while h < 81:
	i = 0
	while i < len(lines):
		print(str(i) +  " is i")
		print(lines[i])
		if int(lines[i]) == 0:
			lines += ",8"
			lines[i ] = 6
		else:
			print(lines[i])
			print(str(int(lines[i]) - 1))

			lines = lines.replace(lines[i], int(lines[i]) - 1, 1)
		i += 2
	h += 1