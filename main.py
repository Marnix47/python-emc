go = True
inputs = []
while(go):
	print("Naam: ")
	name = input().lower()[::-1]
	if name != "":
		inputs.append(name)
	else:
		go = False
inputs.sort()
ret = []
for el in inputs:
	ret.append(el[::-1].capitalize())
print(ret)