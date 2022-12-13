# TLEs... and MLEs... I think the Time Complexity is correct though

import sys
input = sys.stdin.readline
print = sys.stdout.write
sys.setrecursionlimit(10000)

n = int(input())
graph = [[] for i in range(n+1)]
children = [[] for i in range(n+1)]
parents = [[] for i in range(n+1)]
visited = [0 for i in range(n+1)]
memo = [[None,None,None] for i in range(n+1)]
bestused = [0 for i in range(n+1)]

for i in range(n-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(n):
    visited[n] = 1 # Mark node as visited
    for node in graph[n]: 
        if(visited[node] == 0): # Check next unvisited node
            children[n].append(node)
            parents[node].append(n)
            dfs(node)
dfs(1)

def downdp(k):
    best = 0
    secondbest = 0
    if memo[k][0] != None and memo[k][2] != None:
        return [memo[k][0], memo[k][2]]

    for node in children[k]:
        ans = downdp(node)[0]+1
        if ans > best:
            if best > secondbest:
                secondbest = best
            best = ans
            bestused[k] = node
        else:
            if ans > secondbest:
                secondbest = ans
    memo[k][0] = best
    memo[k][2] = secondbest
    return [best, secondbest]

def updp(k):
    up = 0
    if memo[k][1] != None:
        return memo[k][1]
    for parent in parents[k]:
        if bestused[parent] == k:
            up = downdp(parent)[1] + 1
        else:
            up = downdp(parent)[0] + 1
        up = max(up, 1 + updp(parent))
    memo[k][1] = up
    return up

for i in range(1, n+1):
    print(str(max(downdp(i)[0], updp(i))+1))
    print("\n")