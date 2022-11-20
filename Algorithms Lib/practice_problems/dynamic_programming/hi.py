n, w = map(int, input().split())
values = []
weights = []
for i in range(n):
    x, y = map(int, input().split())
    weights.append(x)
    values.append(y)
    
max_weight = w
memo = [[[None]*(max_weight+1)][0] for i in range(n)]

from math import inf
def dp(idx, remaining_weight):
    if remaining_weight < 0:
        return -inf
    if remaining_weight == 0 or idx >= n:
        return 0
    if memo[idx][remaining_weight] != None:
        return memo[idx][remaining_weight]
    memo[idx][remaining_weight] = max(
        dp(idx+1, remaining_weight), # Don't include the weight
        dp(idx+1, remaining_weight-weights[idx]) + values[idx] # Include the weight
    ) 
    return memo[idx][remaining_weight]

print(dp(0, max_weight))