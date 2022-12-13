from sys import setrecursionlimit
setrecursionlimit(100000000)

n, m = map(int, input().split())
phoList = list(map(int, input().split()))
isPho = set(phoList)

# Step 1: Prune tree using DFS starting at a pho resturaunt

# Use DP, keep track if there's a pho resturaunt in the subtree of each node
# If there are none, you can remove the subtree (and the node)

graph = [[] for i in range(n)]
# print(graph)

def edge(x, y): # Edge from node x to node y (undirected)
    graph[x].append(y)
    graph[y].append(x)

for i in range(n-1):
    x, y = map(int, input().split())
    edge(x, y)

visited = [0] * n
valid = [0] * n

def dfs(n):
    visited[n] = 1 # Mark node as visited
    if n in isPho:
        valid[n] = 1
    for node in graph[n]: 
        if(visited[node] == 0): # Check next unvisited node
            if dfs(node) == 1:
                valid[n] = 1
    return valid[n]

dfs(phoList[0]) # get a list of all invalid nodes to ignore

distance = [0] * n

# If we made Jo return back to the starting node, she would visit every edge exactly twice. But since she doesn't have to, there will be a path where each edge is visited only once (the path that she originally would have to go on to get back to the starting node). We can maximize that path by finding the diameter of the tree, then add on 2 edges for every node not included in that path.

def dfs_finddiam(n):
    visited[n] = 1 # Mark node as visited
    for node in graph[n]: 
        if(visited[node] == 0 and valid[node] == 1): # Check next unvisited valid node
            distance[node] = distance[n] + 1
            dfs_finddiam(node)

visited = [0] * n
dfs_finddiam(phoList[0])
# print(distance)
farthest = distance.index(max(distance))
distance = [0] * n
visited = [0] * n
dfs_finddiam(farthest)
# print(distance)
diameter = max(distance)

num_nodes = valid.count(1)
# print(num_nodes)
# print(diameter)

if diameter+1 == num_nodes:
    print(num_nodes-1)
else:
    print(diameter + (num_nodes - (diameter+1))*2)