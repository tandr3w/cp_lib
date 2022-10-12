# https://dmoj.ca/problem/vmss7wc16c3p2


# Graph Initialization
n, m, a, b = map(int, input().split())
graph = [[] for i in range(n+1)]

for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [0] * (n+1)
# DFS to check connectivity
def dfs(n, graph):
    visited[n] = 1 # Mark node as visited
    for node in graph[n]: 
        if(visited[node] == 0):
            dfs(node,graph)

if a == b:
    print("GO SHAHIR!")
else:
    dfs(a, graph)
    if visited[b] == 1:
        print("GO SHAHIR!")
    else:
        print("NO SHAHIR!")
