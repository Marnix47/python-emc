l = int(input("Until:"))
opt = int(input("0 => row, 1 => num: "))
opt2 = 0
if opt == 0:
	opt2 = int(input("From (empty => 0): "))
list = [1,1]
for i in range(2,l):
	list.append(list[i - 2] + list[i - 1])
if opt == 0:
	print(str(list[opt2:l-1]).strip("[]"))
else:
	print(list[l - 1])