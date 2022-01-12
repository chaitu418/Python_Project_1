"""


using queue finding left view
do a level order and print the left most  node

To print left view
To create a new node


"""


class newNode:

    # Construct to create a newNode
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


    def search(self,key):

        if(self.key==key):
            return self
        if(self.left is not None):
            temp=self.left.search(key)
            if temp is not None:
                return temp
            if self.right is not None:
                temp=self.right.search()


# Driver Code
if __name__ == '__main__':

    root = newNode(10)
    root.left = newNode(2)
    root.right = newNode(3)
    root.left.left = newNode(7)
    root.left.right = newNode(8)
    root.right.right = newNode(15)
    root.right.left = newNode(12)
    root.right.right.left = newNode(14)
    printLeftView(root)
    root.search(14)