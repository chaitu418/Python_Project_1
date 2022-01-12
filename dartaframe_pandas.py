"""


pandas in  python
"""
import numpy as np
import pandas as pd
#dataframe=pd.DataFrame(data,index,columns,dtype)
"""
data:represent various forms like series,map,ndarray,list,dict
index:optional argument that represent amn incex to row labels
columns:optional argumetns for column lables
DStype:the data type of each column again optional


Creating a series from a dictioanry object in pandas

"""
# import pandas as pd
# dict_info={'key1':2.0,'key_2':3.1,'key3':2.2}
# series_obj=pd.Series(dict_info)
# print(series_obj)
#
# df2=pd.Series([2,4,6,8,10])
# df3=pd.Series([8,12,14,16,18])
# print(df2,df3)
# p_union=pd.Series(np.union1d(df2,df3))
# p_intersect=pd.Series(np.interse)


"""
Decorators in python
"""

def smartdiv(div):
    def wrapper(a,b):
        if(b!=0):
            return div(a,b)
        else:
            print("Its zero")
    return wrapper


@smartdiv
def div(a,b):
    return a/b

a=div(2,0)
print(a)
