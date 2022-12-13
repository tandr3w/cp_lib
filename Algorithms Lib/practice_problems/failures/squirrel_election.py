# omg i have no idea why this TLEs. I guess top down is just slow??
# my brain is fried i dont wanna do this

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

from math import inf
dp = [[None for x in range(required_points+1)] for y in range(n+1)]
for i in range(0, n+1): 
    for j in range(0, required_points+1):
        if i == 0:
            dp[i][j] == 0
        elif j == 0:
            dp[i][j] = inf
        if points[i-1] <= j: 
            print("e")
            dp[i][j] = min(dp[i-1][j-points[i-1]] + voters[i-1]//2+1, dp[i-1][j]) 
        else: 
            dp[i][j] = dp[i-1][j] 
print(dp[n][required_points])