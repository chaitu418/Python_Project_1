class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

#Add new element at the end of the list

#class linkedlist
class LinkedList:
    def __init__(self):
        self.head=None

    def push_back(self, newElement):
        newNode = Node(newElement)
        if (self.head == None):
            self.head = newNode
            return
        else:
            temp = self.head
            while (temp.next != None):
                temp = temp.next
            temp.next = newNode

    #insert New element at given position
    def insert_at_pos(self,newElement,position):
        newnode=Node(newElement)
        if(position<1):
            print("Invalid posiiton")
        elif(position==1):
            headNode=self.head
            newnode.next=headNode
            self.head=newnode
        else:
            print("here")
            temp=self.head
            for i in range(1,(position-1)):
                print(i)
                if(temp!=None):
                    temp=temp.next

                if(temp!=None):
                    newnode.next=temp.next
                    temp.next=newnode
                else:
                    print("The previosi node is Null")
    def PrintList(self):
        temp=self.head
        if(temp!=None):
            while(temp!=None):
                print(temp.data,end=" ")
                temp=temp.next
            print()
        else:
            print("the list is empty")

#test the code
MyList=LinkedList()

#add three elements at the end of the list
MyList.push_back(10)
MyList.push_back(20)
MyList.push_back(30)
MyList.PrintList()

#insert an elent at position 2
MyList.insert_at_pos(100,2)
MyList.PrintList()
