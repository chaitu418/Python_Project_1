import os
a=[2,4,33,1,2,5,3,7,9,76,2]

first=0
second=0

for i in range(len(a)):
    if(a[i]>first):

        second=first
        first=a[i]


print(first,second)