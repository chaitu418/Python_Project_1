def func(*args,**kwargs):
    print("ARGS")
    for item in args:
        print(item,type(item))
    print("KWARGS")
    for key,value in kwargs.items():
        print("key ==>",key)
        print("Value ==>",value)
func(10,20,30,40,50)
func(10,20,name="dakash",type="abc")  
func(*[10,20,30],**{"1":10,"2":20})