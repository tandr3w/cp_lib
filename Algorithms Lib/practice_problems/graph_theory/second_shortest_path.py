V, M = map(int, input().split())

graph = [[] for i in range(V+1)]
graph2 = [[] for i in range(V+1)]
edges = []

def addConnection(x, y, w):
    graph[x].append((w, y)) # Connection represented by (node, weight) in adjacency list
    graph2[y].append((w, x)) # Connection represented by (node, weight) in adjacency list
    edges.append([w, x, y])

for i in range(M):
    asjds, jdsklfd, jkldsf = map(int, input().split())
    addConnection(asjds, jdsklfd, jkldsf)

from math import inf
dist = [0 for i in range(V+1)]
dist2 = [0 for i in range(V+1)]
vis = [0 for i in range(V+1)]
pq = []

import heapq
for i in range(V+1):
    dist[i] = inf
    dist2[i] = inf

dist[1] = 0
dist2[V] = 0

heapq.heappush(pq, (0, 1))
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

vis = [0 for i in range(V+1)]
pq = []

heapq.heappush(pq, (0, V))
while len(pq):
    d, n = heapq.heappop(pq)
    if vis[n]:
        continue
    else:
        vis[n] = 1
    for edge in graph[n]:
        w, v = edge
        if d+w < dist2[v]:
            dist2[v] = d+w
            heapq.heappush(pq, (dist2[v], v))

final = inf
for edge in edges:
    res = dist[edge[1]] + dist2[edge[2]] + edge[0]
    if res > dist[V]:
        final = min(res, final)

print(final)