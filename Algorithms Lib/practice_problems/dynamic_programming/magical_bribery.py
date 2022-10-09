from sys import setrecursionlimit
setrecursionlimit(10000000)

n = int(input())
values = [None] * (n+1)

for i in range(1, n+1):
    values[i] = int(input())

memo = {}

def dp(x): # Max value for x cards
    if x == 0:
        return 0
    best = 0
    if x in memo:
        return memo[x]
    for i in range(1, x+1):
        temp = dp(x-i) + values[i]
        if temp > best:
            best = temp
    memo[x] = best
    return best

print(dp(n))