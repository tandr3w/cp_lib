v, q = map(int, input().split())

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

for i in range(q):
    inp = input().split()
    if inp[0] == "A":
        unite(int(inp[1]), int(inp[2]))
    elif inp[0] == "Q":
        if same(int(inp[1]), int(inp[2])):
            print("Y")
        else:
            print("N")