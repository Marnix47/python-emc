input = open("input.txt").readlines()[0]

pos = 0

for i in range (0, len(input)):
	if input[i] == "(":
		pos += 1
	if input[i] == ")":
		pos -= 1
print(str(pos))

pos = 0
i = 0

while pos > -1:
	if input[i] == "(":
		pos += 1
	if input[i] == ")":
		pos -= 1
	i += 1
print(str(i + 1))