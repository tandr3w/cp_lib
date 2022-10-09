import sys
sys.setrecursionlimit(100000000)

n, k = map(int, input().split())
sashimi = list(map(int, input().split()))
fish_dict = {}
for i in sashimi:
    if i in fish_dict:
        fish_dict[i] += 1
    else:
        fish_dict[i] = 1

keys = [None] + list(fish_dict.keys())
memo = [[[None]*(k+1)][0].copy() for i in range(n+1)]

def dp(n, k): # Stores num of combinations of (k) fish for first (index) fish
    if k == 0: # Combination has been made
        return 1
    if n == 0: # Impossible to make k fish without any fish
        return 0
    if memo[n][k] != None:
        return memo[n][k]
    # Take all the ways to add the previous fish; we can make a new combination every time we add an option for the next fish.
    # Then, you can do this for each combination of k-1 fish.
    # Basically, all combinations of k-1 to 0 fish, plus all combinations of this step (k)
    memo[n][k] = dp(n-1, k) + fish_dict[keys[n]] * dp(n-1, k-1)
    return memo[n][k]

print(dp(len(keys)-1, k) % 998244353)
