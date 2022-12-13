# BFS

def xytoi(x, y):
    return (x) + (y-1) * 8

graph = [[] for i in range(1000)]

knightx, knighty = map(int, input().split())
targetx, targety = map(int, input().split())
knight = xytoi(knightx, knighty)
target = xytoi(targetx, targety)

vis = [0 for i in range(1000)]
def graphCreator(x, y):
    if vis[xytoi(x, y)] == 1:
        return
    vis[xytoi(x, y)] = 1
    changes = [[-2,-1],[-1,-2],[2,1],[1,2],[1,-2],[-1,2],[2,-1],[-2,1]]
    for pair in changes:
        if x + pair[0] > 0 and x + pair[0] <= 8 and y + pair[1] > 0 and y + pair[1] <= 8:
            graph[xytoi(x, y)].append(xytoi(x + pair[0], y + pair[1]))
            graphCreator(x + pair[0], y + pair[1])

graphCreator(knightx, knighty)

q=[]
visited=[0 for i in range(1000)]
dist=[0 for i in range(1000)]
q.append(knight)
vis[knight] = 1
dist[knight] = 0
while(len(q)):
    topNode = q.pop(0)
    for node in graph[topNode]:
        if not visited[node]: 
            visited[node] = 1
            dist[node] = dist[topNode] + 1
            q.append(node)

if knight == target:
    print(0)
else:  
    print(dist[target])
