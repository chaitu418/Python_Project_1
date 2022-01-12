class check:
    def __init__(self):
        self.n=[]

    def add(self,a):
        return self.n.append(a)
    def remove(self,b):
        self.n.remove(b)
    def dis(self):
        return self.n

obj=check()

choice=1
while choice!=0:
    print("0 exit")
    print("1 ADD")
    print("2 Delete")
    print("3 Display")

    choice=int(input("Enter choice"))
    if choice==1:
        n=int(input("Enter eleent toa ppend"))
        obj.add(n)
        