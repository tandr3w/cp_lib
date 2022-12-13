# BFS can find shortest path, but only in unweighted graphs.

# Bellman-ford can find the shortest path in a weighted graph, even if it has negatives. It doesn't work on graphs with negative cycles, though.
# It works in O(VE).
# It starts by assigning a value (shortest path to that node) of 0 to the starting node and inf to the rest of the nodes. 
# It then iterates through every node, and checks all the edges that lead from it. 
# Let's say node x leads to node y. 
# If the value of node x plus the value of the edge between x and y is less than the value in node y, change node y to that value (a reduction).
# Then, iterate over every node multiple times until no more reductions can be made. It's kind of like bubble sort. At most, you'll need to do this O(V-1) times.
# https://www.youtube.com/watch?v=obWXjtg0L64

v = 6
graph = [[] for i in range(v)]
print(graph)

# Node 1, Node 2, Weight
def addConnection(x, y, w):
    graph[x].append((y, w)) # Connection represented by (node, weight) in adjacency list

addConnection(0, 1, 8)
addConnection(0, 2, 10)
addConnection(1, 3, 1)
addConnection(2, 5, 2)
addConnection(3, 2, 4)
addConnection(3, 5, 1)
addConnection(4, 2, 1)
addConnection(5, 4, 2)

from math import inf

# Initialize starting values
distance = [inf for i in range(v)]
distance[0] = 0

done = True

for j in range(v-1):
    if not done: # one iteration without changes
        break
    done = False
    for i in range(v):
        for e in graph[i]:
            if distance[e[0]] > distance[i]+e[1]:
                distance[e[0]] = distance[i]+e[1]
                done = True
print(distance)