# A graph is a mathematical data structure with "nodes" which are connected by "edges".
# Many things can be represented by graphs, such as grids (where each square is a node and adjacencies are edges), maps, roads, etc.
# Directed edges only go in one direction while undirected edges go both ways. Edges can also be weighted.
# So, how do you make a graph?

# ---

# Adjacency list: List each node, then for each node, list all nodes that are connected. 
# Memory Complexity: O(V+E) where V is the number of nodes and E is the number of edges. 

V = 10 # Number of nodes
adj_graph = [[] for i in range(V+1)]

def adj_createEdge(x, y): # Edge from node x to node y (directed)
    adj_graph[x].append(y)

def adj_createEdgeUndirected(x, y):
    adj_createEdge(x, y)
    adj_createEdge(y, x)

adj_createEdge(2, 5)
print(adj_graph)

# ---

# Adjacency matrix: 2d boolean where arr[i][j] is true if there's an edge between them.
# Memory complexity: O(V^2)

mat_graph = [[False for x in range(V+1)] for y in range(V+1)] 

def mat_createEdge(i, j):
    mat_graph[i][j] = True

mat_createEdge(2, 5)
print(mat_graph)

# ---

# Edge List: store all edges as pairs
# Memory complexity: O(E)

edge_graph = set()

def edge_createEdge(x, y):
    edge_graph.add((x, y))

edge_createEdge(2, 5)
print(edge_graph)
