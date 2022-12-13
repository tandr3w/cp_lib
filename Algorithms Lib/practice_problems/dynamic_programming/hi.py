n = int(input())
voters = []
points = []

for i in range(n):
    v, p = map(int, input().split())
    voters.append(v)
    points.append(p)

required_points = sum(points)//2 + 1

dp = [[0 for x in range(required_points+1)] for y in range(n+1)]
for i in range(n+1): 
    for j in range(required_points+1): 
        if i == 0 or j == 0: 
            dp[i][j] = 0
        elif points[i-1] <= j: 
            dp[i][j] = min(dp[i-1][j-points[i-1]] + voters[i-1]//2+1, dp[i-1][j]) 
        else: 
            dp[i][j] = dp[i-1][j] 
        print(dp)
print(dp[n][required_points])