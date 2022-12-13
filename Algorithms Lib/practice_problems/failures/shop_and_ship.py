# TLEs bcuz constant factor

from math import inf
from sys import stdin
input = stdin.readline

V = int(input())
T = int(input())

graph = [[] for i in range(V+1)]
costs = [None for i in range(V+1)]

for i in range(T):
    x, y, z = map(int, input().split())
    graph[x].append((z, y))
    graph[y].append((z, x))

if T > 500000:
    print("EE")

K = int(input())
for i in range(K):
    z, Pz = map(int, input().split())
    costs[z]=Pz

s = int(input())

dist = [0 for i in range(V+1)]
vis = [0 for i in range(V+1)]
pq = []

from heapq import heappop, heappush
for i in range(V+1):
    dist[i] = inf
dist[s] = 0

heappush(pq, (0, s))

# dijkstra
while len(pq):
    d, n = heappop(pq)
    if vis[n]:
        continue
    else:
        vis[n] = 1
    for edge in graph[n]:
        w, v = edge
        if d+w < dist[v]:
            dist[v] = d+w
            heappush(pq, (dist[v], v))

best = inf
for i in range(V+1):
    if costs[i] == None:
        continue
    else:
        res = costs[i] + dist[i]
        best = min(res, best)
print(best)