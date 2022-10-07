inputFile = open("input.txt", "r")
lines = inputFile.readlines()

totalAppearances = 0

for line in lines:
    i = 0
    for i in line:
        newLine = int(line[i])
        print(newLine)
        if newLine == 0:
            totalApperances = totalAppearances + 10 ** i
            i = i + 1

print(totalAppearances)
        
