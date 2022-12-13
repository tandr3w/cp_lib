v, m = map(int, input().split())
edges = []

for i in range(1, m+1):
    x, y = map(int, input().split())
    edges.append((i, x, y))

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

if len(mst) < v-1:
    print("Disconnected Graph")
else:
    for i in mst:
        print(i[0])