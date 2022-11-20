# State: Max points on a day (index) that ends with activity a/b/c
from sys import stdin, setrecursionlimit
input = stdin.readline
setrecursionlimit(1000000)

def dp_recur():

    n = int(input())

    activities = []
    memo = [[None, None, None] for i in range(n)]
    for i in range(n+1):
        activities.append(list(map(int, input().split())))

    def dp(index, end):
        if memo[index][end] != None:
            return memo[index][end]
        if index == 0:
            memo[index][end] = activities[index][end]
            return memo[index][end]
        if end == 0:
            memo[index][end] = max([dp(index-1, choice) for choice in [1, 2]]) + activities[index][end]
        if end == 1:
            memo[index][end] = max([dp(index-1, choice) for choice in [0, 2]]) + activities[index][end]
        if end == 2:
            memo[index][end] = max([dp(index-1, choice) for choice in [0, 1]]) + activities[index][end]
        
        return memo[index][end]

def dp_iter():
    days = int(input())
    h = [[0, 0, 0]]
    for i in range(days):
        h.append([int(x) for x in input().split(" ")])

    dp = [[0, 0, 0] for i in range(days+1)]
    for i in range(3):
        dp[1][i] = h[1][i]

    for i in range(2,days+1):
        dp[i][0] = h[i][0] + max(dp[i-1][1], dp[i-1][2])
        dp[i][1] = h[i][1] + max(dp[i-1][0], dp[i-1][2])
        dp[i][2] = h[i][2] + max(dp[i-1][0], dp[i-1][1])

    print(max(dp[days][0],dp[days][1],dp[days][2]))

dp_iter()
# print(max(dp(n-1, 0), dp(n-1, 1), dp(n-1, 2)))
