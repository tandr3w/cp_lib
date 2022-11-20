# omg i have no idea why this TLEs

from sys import setrecursionlimit
setrecursionlimit(10000000)

n = int(input())
voters = []
points = []

for i in range(n):
    v, p = map(int, input().split())
    voters.append(v)
    points.append(p)

required_points = sum(points)//2 + 1
memo = [[None] * (required_points+1) for i in range(n+1)]

from math import inf

def dp(idx, required_points): # state: min cost to get required_points pts with the first idx provinces
    if required_points <= 0:
        return 0
    elif idx >= n: # already went through all states but not all points were filled
        return inf
    if memo[idx][required_points] != None:
        return memo[idx][required_points]
    memo[idx][required_points] = min(
        dp(idx+1, required_points), # Ignore province
        dp(idx+1, required_points - points[idx]) + voters[idx]//2 + 1 # Win province
        )
    return memo[idx][required_points]