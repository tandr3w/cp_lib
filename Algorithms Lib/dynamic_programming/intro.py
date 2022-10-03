# Dynamic programming is good for:
# 1. Finding a solution that is as large or small as possible (optimal solution)
# 2. Calculating the total number of solutions for something
# It works by breaking down a problem into subproblems and is applied to recursive / brute force algorithms

# STEPS TO DP
# 1. Find the state (a lot of the time, it's the variable that the questsion provides)
# 2. Do some kind of guessing (think brute force)
# 3. Find the relation (includes a min/max most of the time for optimization. What can you add to the previous subproblem (assume you already know it) in order to get the actual problem?)
# 4. Base Case (what value of your state has an obvious answer)

# Example: Fibonnacci sequence -- the algorithm is broken up into subproblems (fib(n-1) and fib(n-2)) that can be used to solve the original.
def fib(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)

# Now, we can use memoization to optimize it so that we only need to calculate each subproblem once, making it more efficient.
# We store the value of the subproblems in a map (or array).
fib_nums = {}
fib_nums[0] = 0
fib_nums[1] = 1
def fib_alt(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n in fib_nums:
        return fib_nums[n]
    fib_nums[n] = fib(n-1) + fib(n-2)
    return fib_nums[n]

# HOW TO SOLVE A DP PROBLEM?
# Top down (recursive): Start at the function for the answer and work down to the base case
# Bottom up (iterative): Start at the base case and work your way up to the answer
# First, figure out the subproblems / states. What variables can you change? (intuition)
# Next, figure out the recurrence relation (hard part). To do this, you can start with the base case (simplest subproblem) and work your way up in complexity. If there are multiple options, max() and min() are used a lot where you just type both options in as parameters..

# Example Problem
# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night. Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
# State: Maximum money for the first n houses in the street.
# Recurrence relation: Let's try (top-down).
# 1 house? That's the maximum.
# 2 houses? Choose the larger one.
# 3 houses? Hmm...
# f(x) = max(houses[x] + f(x-2), f(x-1))

houses = [10, 3, 2, 5, 7, 8]
def dp_1(x):
    if x < 1:
        return 0
    return max(houses[x] + dp_1(x-2), dp_1(x-1)) # You either choose this house plus the one two houses away, or the adjacent house only.

def dp_2(x):
    if x < 0:
        return 0
    return max(houses[x] + dp_2(x-2), dp_2(x-1))

print(max(dp_1(len(houses)-1), dp_2(len(houses)-2)))