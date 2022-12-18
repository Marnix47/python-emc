inputFile = open("input.txt").readlines()
l = len(inputFile[0].strip("\n"))

grid = [[]*l for _ in range(l)]
visible = [[False]*l for _ in range(l)]
for i in range(len(inputFile)):
	line = inputFile[i]
	k = line.strip("\n")
	for char in k:
		grid[i].append(int(char))
# print(grid)

def checkLeft(i,k):
	global grid
	tree = grid[i][k]
	count = 1
	for a in range(1, k + 1):
		if k - a <= 0:
			break
		elif grid[i][k - a] >= tree:
			break
		else:
			count +=1
	if k == 0:
		count = 0
	return count

def checkRight(i,k):
	global grid
	tree = grid[i][k]
	count = 1
	for a in range(1, l - k):
		if k + a >= l - 1:
			break
		elif grid[i][k + a] >= tree:
			break
		else:
			count +=1
	if k == l - 1:
		count = 0
	return count

def checkTop(i,k):
	global grid
	tree = grid[i][k]
	count = 1
	for a in range(1, i + 1):
		if i - a <= 0:
			break
		elif grid[i - a][k] >= tree:
			break
		else:
			count += 1
	if i == 0:
		count = 0
	return count

def checkBottom(i,k):
	global grid
	tree = grid[i][k]
	count = 1
	for a in range(1, l - i):
		if i + a >= l - 1:
			break
		elif grid[i + a][k] >= tree:
			break
		else:
			count += 1
	if i == l - 1:
		count = 0
	return count
		
	


def checkTree(i,k):
	nums = []
	nums.append(checkLeft(i,k))
	nums.append(checkRight(i,k))
	nums.append(checkTop(i,k))
	nums.append(checkBottom(i,k))
	#print(nums)
	return nums


scenicS = []
for i in range(l):
	for k in range(l):
		scores = checkTree(i,k)
		c = 1
		for num in scores:
			c *= num
		scenicS.append(c)
#print(scenicS)
print(max(scenicS))
