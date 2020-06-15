import random
from numpy import savetxt

size = 10**2
rand = random.sample(range(1,size), size - 1)
print('done')

savetxt("rand_test_10_pow_3.csv", rand, delimiter=",", fmt='%s')

