# Traverse a graph using dfs

class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def addEdge(self, vertex, edge):
        self.gdict[vertex].append(edge)

    def dfs(self, vertex):
        visited = [vertex]
        stack = [vertex]
        while stack:
            popVertex = stack.pop()
            print(popVertex)
            for adjacentVertex in self.gdict[popVertex]:
                if adjacentVertex not in visited:
                    visited.append(adjacentVertex)
                    stack.append(adjacentVertex)

    # Time complexity of dfs O(V + E)
    # Space complexity of dfs O(V + E)

customDict = { "a" : ["b","c"],
               "b" : ["a","d","e"],
               "c" : ["a","e"],
               "d" : ["b","e","f"],
               "e" : ["d","f"],
               "f" : ["d","e"]
                }

graph = Graph(customDict)
graph.dfs("a")

# code worked as expected