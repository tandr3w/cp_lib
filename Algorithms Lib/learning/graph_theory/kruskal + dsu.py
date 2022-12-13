v = 8
edges = []

def addConnection(x, y, w):
    edges.append((w, x, y)) # Connection represented by (node, weight) in adjacency list
addConnection(1, 4, 8)
addConnection(1, 2, 10)
addConnection(1, 3, 1)
addConnection(2, 5, 2)
addConnection(3, 2, 4)
addConnection(3, 5, 1)
addConnection(4, 2, 1)
addConnection(5, 4, 2)


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

mst = set()
edges.sort()
for edge in edges:
    a = edge[1]
    b = edge[2]
    if not same(a, b):
        unite(a, b)
        mst.add(edge)

total_weight = 0
for i in mst:
    total_weight += i[0]
print(total_weight)