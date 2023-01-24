import numpy
l = int(input("Until:"))
if l >= 100:
	print("Error: this will probably crash your Casio")
	print(">>Number expected from over 1000 digits")
else:
	list = [1,1]
	for i in range(2,l):
		list.append(list[i - 2] + list[i - 1])
	print(numpy.prod(list))
