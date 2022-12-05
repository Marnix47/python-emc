def main():
	i = 0;
	while i < 100000000:
		i += 1;
	print(i)

import time
start_time = time.time()
main()
print("%s seconds" % (time.time() - start_time))