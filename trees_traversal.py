class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data

    def printInorder(root):

        if root:
            printInorder(root.left)
            print(root.data)
            printInorder(root.right)

    def printPostorder(root):
        if root:
            printPostorder(root.left)
            printPostorder(root.right)
            print(root.data)
    