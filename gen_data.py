import random

rand = [i for i in range(1, 10**2)]
print(rand[:5])

random.shuffle(rand)
print(rand[:5])

with open('rand_test_100_mn.csv', 'w') as out_file:
    for line in rand:
        out_file.write(str(line) + '\n')
