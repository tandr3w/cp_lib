V, M = map(int, input().split())

graph = [[] for i in range(V+1)]
def addConnection(x, y, t):
    graph[x].append((t, 1, y))
    graph[y].append((t, 1, x))

for i in range(M):
    x, y, t = map(int, input().split())
    addConnection(x, y, t)

s = 1

from math import inf
dist = [0 for i in range(V+1)]
vis = [0 for i in range(V+1)]
pq = []

import heapq
for i in range(V+1):
    dist[i] = [inf, inf]
dist[s] = [0, 0]

heapq.heappush(pq, (0, 0, s))
while len(pq):
    dang, d, n = heapq.heappop(pq)
    if vis[n]:
        continue
    else:
        vis[n] = 1
    for edge in graph[n]:
        danger, w, v = edge
        if dang + danger < dist[v][0] or (dang + danger == dist[v][0] and d+w < dist[v][1]):
            dist[v][1] = d+w
            dist[v][0] = dang+danger
            heapq.heappush(pq, (dist[v][0], dist[v][1], v))
if inf in dist[V]:
    print(-1)
else:
    print(*dist[V])

