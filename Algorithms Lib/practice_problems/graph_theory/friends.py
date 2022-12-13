# Store all friendship pairing in a graph
# Then, just BFS.

import sys
n = int(input())

graph = [None for i in range(10000)]

for i in range(n):
    x, y = map(int, input().split())
    graph[x] = y

from math import inf
def search(node, target):
    visited[node] = 1
    if node == target:
        return 0
    elif graph[node] == None or visited[graph[node]] == 1:
        return -inf
    else:
        return search(graph[node], target) + 1

while True:
    x, y = map(int, input().split())
    visited = [0 for i in range(10000)]
    if x == 0 and y == 0:
        break
    else:
        result = search(x, y)
        if result < 0:
            print("No")
        else:
            print("Yes " + str(result-1))
