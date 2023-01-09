import numpy
l = int(input("Until:"))
list = [1,1]
for i in range(2,l):
	list.append(list[i - 2] + list[i - 1])
print(numpy.sum(list))