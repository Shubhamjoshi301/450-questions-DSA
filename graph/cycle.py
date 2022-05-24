# A class to represent a graph object
class Graph:
    # Constructor
    def __init__(self, edges, n):
        # A list of lists to represent an adjacency list
        self.adjList = [[] for _ in range(n)]
 
        # add edges to the undirected graph
        for (src, dest) in edges:
            self.adjList[src].append(dest)
            self.adjList[dest].append(src)
 
 
# Function to perform DFS traversal on the graph on a graph
ansStack = []
def DFS(graph, v, discovered):
 
    discovered[v] = True            # mark the current node as discovered
    ansStack.append(v)               # print the current node
 
    # do for every edge (v, u)
    for u in graph.adjList[v]:
        if discovered[u]:
            print(True)
            return
        if not discovered[u]:       # if `u` is not yet discovered
            DFS(graph, u, discovered)
 
 
if __name__ == '__main__':
 
    # List of graph edges as per the above diagram
    edges = [
        # Notice that node 0 is unconnected
        (1, 2), (1, 7), (1, 8), (2, 3), (2, 6), (3, 4),
        (3, 5), (8, 9), (8, 12), (9, 10), (9, 11)
    ]
 
    # total number of nodes in the graph (labelled from 0 to 12)
    n = 13
 
    # build a graph from the given edges
    graph = Graph(edges, n)
 
    # to keep track of whether a vertex is discovered or not
    discovered = [False] * n
 
    # Perform DFS traversal from all undiscovered nodes to
    # cover all connected components of a graph
    for i in range(n):
        if not discovered[i]:
            DFS(graph, i, discovered)
    # print(ansStack)