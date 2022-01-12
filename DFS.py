import Flask

graph={
    'A':['B','C'],
    'B':['D','E'],
    'C':['F'],
    'D':[],
    'E':['F'],
    'F':[]
}

"""
Uses stack
take a stack and qdd all elelemtns to it
"""

def DFS(visited,graph,node):
    if node not in visited:
        print(node)
        visited.append(node)
        for neighbour in graph[node]:
            DFS(visited, graph, neighbour)




visited=[]
DFS(visited,graph,'A')