#python program to above approach\

#fucntion to add edges

#Fucntion to print adajancent lsity

#Fucntion to initilaize adjaceny list


class Graph:
    """

    Hello how are ypu
    """

    def __init__(self,edges):
        d={}
        for i,j in edges:
            if(i in d.keys()):
                d[i].append(j)
            else:
                d[i]=[]
        for key ,value in d.items():
            print(key,"==>",value)
    def __repr__(self):
        print("This is dictionary")
    def print(self,strings):
        print("strings")

edges=[[0,1],[0,2],[0,3],[1,2],[2,0],[0,3],[0,4],[1,3],[2,4],[3,4],[4,5]]
graph=Graph(edges)
graph.__repr__()
graph.print("Hey you man")