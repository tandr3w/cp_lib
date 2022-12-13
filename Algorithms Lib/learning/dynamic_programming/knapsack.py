# https://www.youtube.com/watch?v=ocZMDMZwhCY

# Subproblem: Suffix of values/weights, remaining weights.

values = [1, 5, 3]
weights = [1, 2, 3]
max_weight = 5

n = len(values)
memo = [[[None] * (max_weight+1)].copy()[0] for i in range(n)]
print(memo)

def dp(idx, remaining_weight):
    if remaining_weight <= 0 or idx >= n:
        return 0
    if memo[idx][remaining_weight] != None:
        return memo[idx][remaining_weight]
    if remaining_weight - weights[idx] >= 0:
        memo[idx][remaining_weight] = max(
            dp(idx+1, remaining_weight), # Don't include the weight
            dp(idx+1, remaining_weight-weights[idx]) + values[idx] # Include the weight
        ) 
    else:
        memo[idx][remaining_weight] = dp(idx+1, remaining_weight)
    return memo[idx][remaining_weight]

print(dp(0, max_weight))


# Bottom up solution
dp = [[0 for x in range(max_weight+1)] for y in range(n+1)]
for i in range(n+1): 
    for j in range(max_weight+1): 
        if i == 0 or j == 0: 
            dp[i][j] = 0
        elif weights[i-1] <= j: 
            dp[i][j] = max(dp[i-1][j-weights[i-1]] + values[i-1], dp[i-1][j]) 
        else: 
            dp[i][j] = dp[i-1][j] 
print(dp[n][max_weight]) 