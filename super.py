class Parent:
    def __init__(self,text):
        self.message=text
    def PrintText(self):
        print(self.message)

class Child(Parent):
    def __init__(self,text):
        super().__init__(text)
    def PrintText(self):
        print(':hshhdhf')

x=Child("Hi Hello How are you")
x.PrintText()
