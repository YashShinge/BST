import random
import csv

size = 10**8
rand = random.sample(range(1,size), size - 1)
print('done')


# for i in range(8, 10):
# 	size = 10**i
# 	rand = random.sample(range(1,size), size - 1)
# 	print('done')
# 	with open(f'rand_10_power_{i}.csv', 'w') as myfile:
# 	    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
# 	    wr.writerow(rand)
# 	print(f'Done {i}')
