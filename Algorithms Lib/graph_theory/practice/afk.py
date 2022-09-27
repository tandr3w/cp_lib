# https://dmoj.ca/problem/dmopc13c1p4

t = int(input())

for i in range(t):
    l, w = input().split()
    l = int(l)
    w = int(w)
    map = []
    graph = [[] for k in range(l*w)]

    for j in range(w):
        map.append(list(input()))

    washroom = None
    computer = None

    def enum_spot(m, n):
        return m*l+n

    for m in range(len(map)):
        for n in range(len(map[m])):
            if map[m][n] == "X":
                continue
            if map[m][n] == "W":
                washroom = enum_spot(m, n)
            if map[m][n] == "C":
                computer = enum_spot(m, n)
            if m != 0: # Check top
                if map[m-1][n] != "X":
                    graph[m*l+n].append(enum_spot(m-1, n))
            if m < w-1:
                if map[m+1][n] != "X":
                    graph[m*l+n].append(enum_spot(m+1, n))
            if n != 0:
                if map[m][n-1] != "X":
                    graph[m*l+n].append(enum_spot(m, n-1))
            if n < l-1:
                if map[m][n+1] != "X":
                    graph[m*l+n].append(enum_spot(m, n+1))

    q=[] # queue 
    vis=[0 for i in range(l*w)] # visited array
    dist=[0 for i in range(l*w)] # distance from root node to node[i]
    q.append(computer) # starting node
    vis[computer] = 1 # mark starting node as visited
    while(len(q)): # while we still have nodes to process
        topNode = q.pop(0) # remove top node 
        for node in graph[topNode]: # process adjacent nodes 
            if not vis[node]: # if not visited yet 
                vis[node] = 1 # visit it
                dist[node] = dist[topNode] + 1 # update distance 
                q.append(node) # insert into queue
    if vis[washroom] == 1:
        if dist[washroom] < 60:
            print(dist[washroom])
        else:
            print("#notworth")
    else:
        print("#notworth")

