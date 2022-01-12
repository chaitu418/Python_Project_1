class Graph:
    def __init__(self,num_nodes,edges):
        self.num_nodes=num_nodes
        self.data=[[] for _ in range(num_nodes)]
        for n1,n2 in edges:
            self.data[n1].append(n2)
            self.data[n2].append(n1)
    def __repr__(self):
        return "\n".join(["{}:{}".format(n,neighbours) for n,neighbours in enumerate(self.edges)]

edges = [[0,1],[0,2],[0,3],[1,2],[2,0],[0,3],[0,4],[1,3],[2,4],[3,4],[4,5]]
num_nodes=5
graph1=Graph(num_nodes,edges)

