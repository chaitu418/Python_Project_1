def BinarySearch(numbers,low,high,x):
    if(high>=low):
        mid=low+(high-low)//2
        if(numbers[mid]==x):
            print(mid)
            return mid
        elif(numbers[mid]>x):
            return BinarySearch(numbers,low,mid+1,x)
        else:
            return BinarySearch(numbers,mid+1,high,x)
    else:
        return -1

numbers=[1,2,3,4,5,6]
x=3
result=BinarySearch(numbers,0,len(numbers)-1,x)

if(result!=-1):
    print("search succesful and elemnt found at pos",result)
else:
    print("The given eleemnt is not present in array")