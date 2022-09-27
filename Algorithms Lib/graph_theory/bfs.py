# Breadth first search: Searches all nodes distance 1 away, then distance 2, then distance 3... etc.

# Useful for: Find the shortest path (unweighted graphs only)

# Simulate it on paper if you're confused.

V = 10 # Number of nodes
adj_graph = [[] for i in range(V+1)]

def adj_createEdge(x, y): # Edge from node x to node y (directed)
    adj_graph[x] = y

s = 0 # Start with first node
q=[] # queue 
vis=[0 for i in range(V+1)] # visited array
dist=[0 for i in range(V+1)] # distance from root node to node[i]
q.append(adj_graph[s]) # starting node
vis[s] = 1 # mark starting node as visited
while(len(q)): # while we still have nodes to process
    topNode = q.pop(0) # remove top node 
    for node in adj_graph[topNode]: # process adjacent nodes 
        if not vis[node]: # if not visited yet 
            vis[node] = 1 # visit it
            dist[node] = dist[topNode] + 1 # update distance 
            q.append(node) # insert into queue

