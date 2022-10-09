# Depth first search: Goes deeper through a single path until the path ends, then backtracks until it has an unexplored option again.

# Useful for: Check if two nodes are connected

# Draw the recursion tree if you don't understand how these work.

V = 10 # Number of nodes
adj_graph = [[] for i in range(V+1)]

def adj_createEdge(x, y): # Edge from node x to node y (directed)
    adj_graph[x].append(y)

visited = [0] * (V+1)

def dfs(n, graph):
    visited[n] = 1 # Mark node as visited
    for node in graph[n]: 
        if(visited[node] == 0): # Check next unvisited node
            dfs(node,graph)

dfs()
