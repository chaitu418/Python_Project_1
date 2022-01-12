# Python program to print left view of Binary Tree

# A binary tree node
class Node:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Recursive function print left view of a binary tree
def leftViewUtil(root, level, max_level):

    if root is None:
        return

    if(max_level[0] < level):
        print(root.data)
        max_level [0] =level

    leftViewUtil(root.left,level+1,max_level)
    leftViewUtil(root.right,level+1,max_level)


# A wrapper over leftViewUtil()
def leftView(root):

    max_level = [0]
    #print(max_level,type(max_level))
    leftViewUtil(root, 1, max_level)


# Driver program to test above function
root = Node(12)
root.left = Node(10)
root.right = Node(20)
root.right.left = Node(25)
root.right.right = Node(40)
root.right.right.left = Node(50)
root.right.left.left = Node(60)

leftView(root)

