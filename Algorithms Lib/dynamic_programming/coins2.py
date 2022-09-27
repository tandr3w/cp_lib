# Coins problem again but I solve it without looking at the solutions.
from math import inf
coins = [1, 4, 6, 7]

def solve(x): # print minimum number of coins needed to solve x
    best = inf
    if x == 0:
        return 0
    if x < 0:
        return inf
    for coin in coins:
        best = min(solve(x-coin)+1, best)
    return best

print(solve(8))