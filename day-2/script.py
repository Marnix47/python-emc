inputFile = open('input.txt', 'r')
lines = inputFile.readlines()

xPositie = 0
huidigeXPositie = 0
huidigeDiepte = 0
diepte = 0
aim = 0

for line in lines:
    if "up" in line:
        huidigeDiepte = int(line[3])
        diepte = diepte - huidigeDiepte
        aim = aim - huidigeDiepte
    if "down" in line:
        huidigeDiepte = int(line[5])
        diepte = diepte + huidigeDiepte
        aim = aim + huidigeDiepte
    if "forward" in line:
        huidigeXPositie = int(line[8])
        xPositie = xPositie + huidigeXPositie
        diepte = diepte + aim * huidigeXPositie
        
        

print("diepte is " + str(diepte))
print("xPositie is " + str(xPositie))
print("antwoord is " + str(diepte * xPositie))