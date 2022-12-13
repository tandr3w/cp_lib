v = int(input())
coords = [None for i in range(v+1)]
for i in range(1, v+1):
    coords[i] = tuple(map(int, input().split()))

existing = []
edges = []

from math import sqrt
m = int(input())
for i in range(m):
    b1, b2 = map(int, input().split())
    d = sqrt(abs(coords[b1][0] - coords[b2][0])**2 + abs(coords[b1][1]-coords[b2][1])**2)
    existing.append((d, b1, b2))

# Add all possible cable locations to edge list
for i in range(1, v+1):
    for j in range(i+1, v+1):
        if i == j:
            continue
        d = sqrt(abs(coords[i][0] - coords[j][0])**2 + abs(coords[i][1]-coords[j][1])**2)
        edges.append((d, i, j))

# ---------------
# DSU
link = [0 for i in range(v+1)]
size = [1 for i in range(v+1)]
for i in range(1, v+1):
    link[i] = i

def find(x): # find the representative of the set
    while x != link[x]:
        x = link[x]
    return x

def same(x, y): # find if two elements are in the same set
    return find(x) == find(y)

def unite(x, y): # connect two sets by connecting the representative of the smaller set to the representative of the larger set (to minimize the length of chains)
    xRep = find(x)
    yRep = find(y)
    if size[xRep] > size[yRep]:
        link[yRep] = xRep
        size[xRep] += yRep
    else:
        link[xRep] = yRep
        size[yRep] += xRep

# ---------------
# Build MST

# Make it use all existing first

mst = set()

for edge in existing:
    a = edge[1]
    b = edge[2]
    unite(a, b)
    mst.add(edge)

edges.sort()
total_weight = 0

for edge in edges:
    a = edge[1]
    b = edge[2]
    if not same(a, b):
        unite(a, b)
        mst.add(edge)
        total_weight += edge[0]

if total_weight == 0:
    print("0.00")
else:
    print(round(total_weight, 2))

for i in mst:
    if i not in existing:
        print(i[1], end=" ")
        print(i[2])