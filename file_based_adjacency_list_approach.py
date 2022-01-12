#python program for above approach
def addEdge(adj,u,v):
    adj[u].append(v)

def adjancencylist(adj,V):
    for i in range(0,V):
        #print(i,"-->",end="")
        print(adj[i])
        for x in adj[i]:
            print(x," ",end="")

def initGraph(V,edges,noOfEdges):

    adj=[0]*3
    for i in range(0,len(adj)):
        adj[i]=[]
        #print(adj[i])

    for i in range(0,noOfEdges):
        addEdge(adj,edges[i][0],edges[i][1])

    adjancencylist(adj,V)


V=3
edges=[[0,1],[1,2],[2,0]]
noOfEdges=3
initGraph(V,edges,noOfEdges)