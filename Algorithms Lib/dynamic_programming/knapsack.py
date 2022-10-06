# https://www.youtube.com/watch?v=ocZMDMZwhCY

# Subproblem: Suffix of values/weights, remaining weights.

values = [1, 5, 3]
weights = [1, 2, 3]
max_weight = 5

n = len(values)
memo = [[[None] * (max_weight+1)].copy()[0] for i in range(n)]
print(memo)

from math import inf
def dp(idx, remaining_weight):
    if remaining_weight < 0:
        return -inf
    if remaining_weight == 0 or idx >= n:
        return 0
    print(idx, end=" ")
    print(remaining_weight)
    if memo[idx][remaining_weight] != None:
        return memo[idx][remaining_weight]
    memo[idx][remaining_weight] = max(
        dp(idx+1, remaining_weight), # Don't include the weight
        dp(idx+1, remaining_weight-weights[idx]) + values[idx] # Include the weight
    ) 
    return memo[idx][remaining_weight]

print(dp(0, max_weight))