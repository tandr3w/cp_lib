# Similar to knapsack
# TLE-s, don't know why.

from sys import setrecursionlimit, stdin
setrecursionlimit(10000)
input = stdin.readline

n = int(input())
voters = []
points = []

for i in range(n):
    v, p = map(int, input().split())
    voters.append(v)
    points.append(p)

required_points = sum(points)//2 + 1
memo = [[None] * (required_points+1)] * (n+1)
memo = {}

from math import inf
def dp(idx, required_points): # State: Suffix of voters/points array, 
    # Guess: Win or don't win for this province?
    if required_points <= 0:
        return 0
    elif idx >= n:
        return inf
    if memo[idx][required_points] != None:
        return memo[idx][required_points]
    memo[idx][required_points] = min(
        dp(idx+1, required_points - points[idx]) + voters[idx]//2 + 1, # Win province
        dp(idx+1, required_points) # Ignore province
        )
    return memo[idx][required_points]

print(dp(0, required_points))