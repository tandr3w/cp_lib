# https://dmoj.ca/problem/ccc18j5

n = int(input())
graph = [[] for i in range(n+1)]
for i in range(n):
    for option in list(map(int, input().split()))[1:]:
        graph[i].append(option-1)

# print(graph)
paths = []
s = 0 # Start with first node
q=[] # queue 
vis=[0 for i in range(n+1)] # visited array
dist=[0 for i in range(n+1)] # distance from root node to node[i]
q.append(s) # starting node
vis[s] = 1 # mark starting node as visited
while(len(q)): # while we still have nodes to process
    topNode = q.pop(0) # remove top node 
    if len(graph[topNode]) == 0:
        paths.append(dist[topNode])
    for node in graph[topNode]: # process adjacent nodes 
        if not vis[node]: # if not visited yet 
            vis[node] = 1 # visit it
            dist[node] = dist[topNode] + 1 # update distance 
            q.append(node) # insert into queue

if 0 in vis[:n]:
    print("N")
else:
    print("Y")
print(min(paths)+1)