#T0 parse in a dictionary in python


import os
d={
    "record1":
        {"Name":"Chay",
    "age":"26",
    "company":"Qualcomm",
    "assocoates":["ravi","radha"]
        },
    "record2":
        {
    "Name":"hay",
    "age":"6",
    "company":"Caedence",
    "assocoates":["r1","radha"]
        }
    }

d2={}
#print(d)
for record in d:
    print(d[record])
    for elements in d[record].items():
        if('assocoates' in elements):
            print(d[record]['assocoates'])
            if("radha" in d[record]['assocoates']):
                print(record,"-->",d[record]['assocoates'])
                d2[record]=d[record]['assocoates']

print("So finally the leents are")
print(d2)
