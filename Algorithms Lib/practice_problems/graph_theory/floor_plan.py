# Iterate through every empty space. If it's not visited, then BFS starting from it and append the size of the room in a list. The rest is trivial.

flooring = int(input())
r = int(input())
c = int(input())

graph = [[] for i in range(r*c)]

def xytorc(x, y):
    return x + y*c

def rctoxy(sum):
    return sum % c, sum // c

def createEdge(x, y):
    graph[x].append(y)

floorplan = []
for i in range(r):
    row = input()
    floorplan.append(row)

for i in range(r):
    for j in range(c):
        if floorplan[i][j] != "I":
            if j != 0:
                if floorplan[i][j-1] != "I":
                    graph[xytorc(j, i)].append(xytorc(j-1, i))
            if j < c-1:
                if floorplan[i][j+1] != "I":
                    graph[xytorc(j, i)].append(xytorc(j+1, i))
            if i != 0:
                if floorplan[i-1][j] != "I":
                    graph[xytorc(j, i)].append(xytorc(j, i-1))
            if i < r-1:
                if floorplan[i+1][j] != "I":
                    graph[xytorc(j, i)].append(xytorc(j, i+1))

vis=[0 for i in range(r*c+1)]
rooms = []
for i in range(r*c):
    x, y = rctoxy(i)
    if vis[i] == 0 and floorplan[y][x] != "I":
        area = 1
        queue=[]
        queue.append(i)
        vis[i] = 1
        while(len(queue)):
            topNode = queue.pop(0)
            for node in graph[topNode]:
                if not vis[node]:
                    vis[node] = 1
                    queue.append(node)
                    area += 1
        rooms.append(area)

rooms.sort()
e = reversed(rooms)

count = 0
for room in e:
    if flooring >= room:
        flooring -= room
        count += 1
    else:
        break
if count == 1:
    print("" + str(count) + " room, " + str(flooring) + " square metre(s) left over")
else:
    print("" + str(count) + " rooms, " + str(flooring) + " square metre(s) left over")
