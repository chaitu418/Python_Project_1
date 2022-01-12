class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
    def insert_at_beg(self,new_node):
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head=new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next
        print(end='\n')

    def insert_at_end(self,new_node):
        #loop till last
        current=self.head
        while(current.next):
            print(current.data)
            current=current.next
        current.next=new_node

    def insert_at_pos(self,newnode,afternode):

        current=self.head
        node2 = Node(afternode)
        while(current.next):

            if(current.data==afternode):

                temp=current.next
                current.next=newnode
                newnode.next=temp
            current = current.next

        while(current.next):
            print("Inside")
            print(current.data)
            current=current.next


a_llist = LinkedList()
n = int(input('How many elements would you like to add? '))
for i in range(n):
    data = int(input('Enter data item: '))
    node = Node(data)
    a_llist.insert_at_beg(node)

a_llist.display()

print('The linked list: ', end='')
a_llist.insert_at_pos("5","2")
a_llist.display()
