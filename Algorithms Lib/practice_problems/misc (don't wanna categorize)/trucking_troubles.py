# Idea: bsearch the answer and check if it works.

# TLEs lol. (At this point I gave up and decided to learn MST)

import sys
input = sys.stdin.readline

c, r, d = map(int, input().split())
cities = [[] for i in range(c+1)]

for i in range(r):
    x, y, w = map(int, input().split())
    cities[x].append((y, w))
    cities[y].append((x, w))

destinations = []
for i in range(d):
    destinations.append(int(input()))

l = -1
r = 100000

visited = [0] * (c+1)


def bfs(n, w):
    s = n
    q=[]
    q.append(s)
    visited[s] = 1 
    while(len(q)):
        topNode = q.pop(0)
        for node in cities[topNode]:
            if visited[node[0]] == 0 and w<=node[1]:
                visited[node[0]] = 1
                q.append(node[0])

while l <= r:
    visited = [0] * (c+1)
    mid = (l+r)//2
    bfs(1, mid)
    is_work = True
    for i in destinations:
        if visited[i] == 0:
            is_work = False
    if is_work:
        l = mid+1
        ans = mid
    else:
        r = mid - 1
print(l)

