# Problem: Given a set of coins, print the minimum number of coins needed to form the sum n.
# If you ever struggle with recursion, try drawing out the tree
# We can break this into subproblems; We can create three recursive branches that add a coin like this:

import math
coins = [1, 3, 4]

def solve(x):
    if x == 0:
        return 0
    if x < 0: # If a coin overflows, it will never be the minimum unless the sum is impossible
        return math.inf
    best = math.inf
    for coin in coins:
        best = min(best, solve(x-coin)+1) # Each time we add a coin, we take all the previous combinations and for each one, call the function n times, once for each coin in the list.
    return best
# --------------------
values = {}
values[0] = 0
def solve_dp(x):
    if x == 0:
        return 0
    if x < 0:
        return math.inf
    if x in values:
        return values[x]
    best = math.inf
    for coin in coins:
        best = min(best, solve_dp(x-coin)+1)
    values[x] = best
    return best

# --------------------
# Iterative approach: Calculate all values of solve() within the constraints (n)
# This approach is recommended for cp
values = {}
values[0] = 0
def solve_dp_iter(x):
    for n in range(1, x+1):
        values[n] = math.inf
        for coin in coins:
            if n-coin >= 0:
                values[n] = min(values[n], values[n-coin]+1)
    
# solve_dp_iter(2)
# print(values[2]) 
# print(solve(300)) # Way faster than without dp!!

# --------------------
# Construct an example of the solution
values = {}
first = {}
values[0] = 0
def solve_dp_iter_example(x):
    for n in range(1, x+1):
        values[n] = math.inf
        for coin in coins:
            if n-coin >= 0 and values[n-coin]+1 < values[n]:
                values[n] = values[n-coin]+1
                first[n] = coin # Store the coin added at this point to make the optimal solution

# x = 23
# solve_dp_iter_example(x)
# print(values[x])
# while x > 0:
#     print(first[x], end=", ")
#     x -= first[x]

# --------------------
# Count the number of solutions

def count_nodp_recur(x): # Basically, just add 1 to the count every time the sum reaches 0, the base case (i.e. finds a solution)
    c = 0
    if x == 0:
        return 1
    if x < 1:
        return 0
    best = math.inf
    for coin in coins:
        c += count_nodp_recur(x-coin) 
    return c

print(count_nodp_recur(5))

# --------------------

count = [1]
def solve_dp_iter_count(x): # Basically, each time the sum reaches 0 in a branch (the base case), the count goes up by 1, and the values are stored with bp.
    for n in range(x + 1):
        count.append(0)
        for coin in coins:
            if n - coin >= 0:
                count[n] += count[n-coin]

solve_dp_iter_count(5)
print(count[5])


