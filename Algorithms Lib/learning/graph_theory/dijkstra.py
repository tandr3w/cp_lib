V = 4

graph = [[] for i in range(V+1)]
def addConnection(x, y, w):
    graph[x].append((w, y)) # Connection represented by (node, weight) in adjacency list

addConnection(0,1,3)
addConnection(0,2,1)
addConnection(1,3,0)
addConnection(2,3,4)


s = 0 # Starting node

from math import inf
dist = [0 for i in range(V+1)]
vis = [0 for i in range(V+1)]
pq = []

import heapq
for i in range(V+1):
    dist[i] = inf
dist[s] = 0

heapq.heappush(pq, (0, s))
while len(pq):
    d, n = heapq.heappop(pq)
    if vis[n]:
        continue
    else:
        vis[n] = 1
    for edge in graph[n]:
        w, v = edge
        if d+w < dist[v]:
            dist[v] = d+w
            heapq.heappush(pq, (dist[v], v))
print(dist)

