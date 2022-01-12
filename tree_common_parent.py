class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def push(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node

    def PrintList(self):
        node=self.head
        while(node):
            print(str(node.data)+"-->",end=" ")
            node=node.next
        print("NULL")

    def printMiddle(self):
        slow=self.head
        fast=self.head
        while(fast and fast.next):
            slow=slow.next
            fast=fast.next.next
        print(slow.data)

if __name__=='__main__':
    list1=LinkedList()
    for i in range(5,0,-1):
        list1.push(i)
        list1.PrintList()
        list1.printMiddle()

A = [1, 2, 3, 4, 5, 6]
start=0
end=5
while(start<end):
    A[start],A[end]=A[end],A[start]
    start+=1
    end-=1

print(A)
