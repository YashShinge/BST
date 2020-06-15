class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left:
                return self.left.insert(value)
            else:
                self.left = Node(value)
            
            
        elif value > self.value:
            if self.right:
                return self.right.insert(value)
            else:
                self.right = Node(value)
        else:
            print('Value already in BST')
            return False
    
    def print_all(self):
        if self:
            print(self.value)
            if self.left:
                self.left.print_all()
                
            if self.right:
                self.right.print_all()

                
    def print_left(self):
        if self.left:
            print(self.left.value)
            self.left.print_left()
            
        
    def print_right(self):
        if self.right:
            print(self.right.value)
            self.right.print_right()
            
    def get_height(self):
        if self.left and self.right:
            return 1  + max(self.left.get_height(), self.right.get_height())
        
        elif self.left:
            return 1 + self.left.get_height()
        
        elif self.right:
            return 1 + self.right.get_height()
        
        else:
            return 1


class BST:
    def __init__(self):
        self.root = Node(0)

    def insert(self, value):
        if self.root:
            return self.root.insert(value)
        # else:
        #     self.root = Node(value)

    def print_all(self):
        self.root.print_all()

    def print_root(self):
        print(self.root.value)

    def print_left(self):
        self.root.print_left()

    def print_right(self):
        self.root.print_right()

    def get_height(self, p=None):

        if p == 'L':
            if self.root:
                return self.root.left.get_height()
            else:
                return -1

        elif p == 'R':
            if self.root:
                return self.root.right.get_height()
            else:
                return -1

        if self.root:
            return self.root.get_height()
        else:
            return -1


import os
import csv
import datetime

path = os.getcwd()
os.chdir(path)

# filenames = [f'rand_10_power_{i}.csv' for i in range(7,8)]

# file = filenames[]

# times = []
# for i in range(len(filenames)):
with open('rand_10_power_3.csv', newline='') as f:
    reader = csv.reader(f)
    row1 = next(reader)

rand = [int(i) for i in row1]

t = BST()
a = datetime.datetime.now()
for i in rand:
    t.insert(i)
b = datetime.datetime.now() 
c = b - a

print('Time: ',c.microseconds)
print('Height: ', t.get_height())
