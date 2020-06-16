import time


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
            return 1 + max(self.left.get_height(), self.right.get_height())
        
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


rand = []
with open('rand_test_100_mn.csv', 'r') as f:
    print('Loading file...')
    for row in f:
        rand.append(int(row.rstrip()))
    print('File loaded.\n')


for j in range(8, 9):

    t = BST()
    a = time.time()
    for i in rand[:10**j]:
        t.insert(i)
    b = time.time()
    c = b - a
    print(f'For 10 power {j}')
    print('Time: ', c*(10**6))
    print('Height: ', t.get_height(), '\n')
