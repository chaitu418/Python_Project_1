"""

First write fucntion based code
then write class baesed code
Uses Queue
"""


class DFS:
    def __init__(self):
        self.visited = []  # To track all the visited nodes
        self.queue = []  # Initialize a queue

    def bfs(self, graph, node):
        self.visited.append(node)
        self.queue.append(node)
        while (self.queue):
            s = self.queue.pop(0)
            print(s)
            for neighbours in graph[s]:
                if neighbours not in self.visited:
                    self.visited.append(neighbours)
                    self.queue.append(neighbours)

if __name__=="__main__":

    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }
    a=DFS()
    a.bfs(graph,'A')