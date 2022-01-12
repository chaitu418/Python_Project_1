class power:
    def calculate(self,x,n):
        val=1
        if(n>1):
            while(n>=1):
                print(n)
                val=val*x
                n-=1
        print(val)

a=power()
a.calculate(2,5)
#both should be positive
#if  negative do accrodingly
