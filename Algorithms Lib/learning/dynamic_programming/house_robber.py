nums = [1, 2, 3, 4, 5]
memo = [-1 for i in range(len(nums))]
def dp(k):
    if k == 0:
        return nums[k]
    if k == 1:
        return max(nums[0], nums[1])
    if memo[k] == -1:
        memo[k] = max(dp(k-1), dp(k-2) + nums[k])
    return memo[k]

print(dp(len(nums)-1))

# Iterative Solution
dp = [-1 for i in range(len(nums))]
dp[0] = nums[0]
dp[1] = max(nums[0], nums[1])
for i in range(2, len(nums)):
    dp[i] = max(dp[i-1], dp[i-2]+nums[i])
