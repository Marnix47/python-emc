
def calc(n):
	returnValue = 0
	for i in range(n):
		returnValue += i
	print(returnValue)
	return returnValue

inputFile = open("input.txt")
line = inputFile.readlines()[0]
numbers = line.split(',')

for k in range(1000):
	numbers[k] = int(numbers[k])
#print(numbers)

	
fuels = [0]*2000
	

for number in numbers:
	n = int(number)
	for i in range(500,1500):
		#if fuels[i] != "":
			#fuels[i] = abs(i - n)
		#else:
		#t = calc(n)
		
		t = abs(i - n)
		#print(t)
		r = 0
		for i in range(0, t):
			r += i
		fuels[i] += t
#print(fuels)


lowestFuel = fuels[0]
lowestFuelIndex = 0
for h in range(999):
	f = fuels[h]
	if lowestFuel > f:
		lowestFuel = f
		lowestFuelIndex = h

print(lowestFuel)
print(lowestFuelIndex)

