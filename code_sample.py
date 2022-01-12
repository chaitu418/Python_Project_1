class ParentClass:
    def par_func(self):
        print("I am paresnt class dincruon")
class ChildClass(ParentClass):
    def child_func(self):
        print("I am child finctions")

#Driver code

obj1=ChildClass()
obj1.par_func()
obj1.child_func()
