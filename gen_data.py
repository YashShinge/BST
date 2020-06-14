import random
import csv
import os
path = 'C:/Users/Yash Shinge/Desktop/BST/'
os.chdir(path)

for i in range(1,9):
	size = 10**i
	rand = random.sample(range(1,size), size - 1)

	with open(f'rand{size}.csv', 'w') as myfile:
	    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
	    wr.writerow(rand)