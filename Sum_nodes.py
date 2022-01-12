"""
To get sum of all nodes in a tree

tree = None

"""

class Tree:
    def __init__(self,data=None):
        self.data=data
        self.left=None
        self.right=None
        self.children=[]

    def add(self,value):
        self.value=value
        if((self.value is not None)):

            if (self.data > self.value):
                v=add(self.right.data)
            else:
                v2=add(self.left.data)
        else:
            return 0

    def display(self):
        if(self.data):
            print(self.data)
        else:
            return 0
        display(self.left.data)
        display(self.right.data)


tree = Tree(2)

list1=[5,6,26,21,6,23,7,252,7,27]
for i in list1:
    tree.add(i)
print(tree.display)
