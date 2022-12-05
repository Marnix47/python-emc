inputFile = open("input.txt")
lines = inputFile.readlines()

gerold = lines[0]
currentLine = 2
i = 0
huidigeBingoKaart = 2

for bingoKaart in lines[huidigeBingoKaart]:
	while currentLine < 6:
		currentLine += 1
		newVar = lines[currentLine]
	huidigeBingoKaart += 6