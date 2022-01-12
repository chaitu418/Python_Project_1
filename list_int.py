def summer(step, track, lst):
    if track<10:
        lst.append(1)
        summer(step,track+step,lst)

    return lst

a=summer(1,1,[])
print(a)