inputFile = open("input.txt", "r")
lines = inputFile.readlines()

tA = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for line in lines:
        #print(line)
        #print("started with new line")
        i = 0
        while (i < 12):
            newLine = int(line[i])
            #print(newLine)
            if newLine == 1:
                tA[i] = tA[i] + 1
            i = i + 1
        i = 0

print(tA)

gammaRate = ""
epsilonRate = ""

t = 0

while (t < 12):
    if tA[t] > 500:
        gammaRate = gammaRate + "1"
        epsilonRate = epsilonRate + "0"
    if tA[t] < 500:
        gammaRate = gammaRate + "0"
        epsilonRate = epsilonRate + "1"
    t = t + 1

print("epsilonRate is " + epsilonRate)
print("gammaRate is " + gammaRate)

testNumber = int(epsilonRate, 2) * int(gammaRate, 2)

print(testNumber)

        
