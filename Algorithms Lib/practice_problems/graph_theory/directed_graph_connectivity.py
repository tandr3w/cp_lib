# https://dmoj.ca/problem/nccc5j5s3

n, m = map(int, input().split())

graph = [[] for i in range(n+1)]
def createEdge(x, y): # Edge from node x to node y (directed)
    graph[x].append(y)

def removeEdge(x, y):
    graph[x].remove(y)

edges = []

for i in range(m):
    s, t = map(int, input().split())
    edges.append((s, t))
    createEdge(s, t)

visited = [] * (n+100)
def dfs(n, graph):
    visited[n] = 1 # Mark node as visited
    for node in graph[n]: 
        if(visited[node] == 0): # Check next unvisited node
            dfs(node,graph)

for i in range(m):
    visited = [0] * (n+1)
    removeEdge(edges[i][0], edges[i][1])
    dfs(1, graph)
    if visited[n] == 1:
        print("YES")
    else:
        print("NO")
    createEdge(edges[i][0], edges[i][1])



