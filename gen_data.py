import random
from numpy import savetxt

for i in range(1,8):
	size = 10**i
	rand = random.sample(range(1,size), size - 1)

	savetxt(f"rand_test_10_pow_{i}.csv", rand, delimiter=",", fmt='%s')
