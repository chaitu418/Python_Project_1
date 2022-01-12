#to find lduplicate lee,nt in list

l=[1,2,34,5,6,6,7,5]
l2 = []
for i in l:
    if (i not in l2):
        l2.append(i)
    else:
        print("element repeated i", i)
