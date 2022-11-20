# Find the longest increasing subsequence that ends at position pos
# Works by splitting it into subproblems, finding every possible place it can jump from and recursively calling the function, then returning the best result.

sequence = [6, 2, 5, 1, 7, 4, 8, 3]

# Recursive Approach
length_dp = {}
def lis(k):
    best = 1
    for i in range(0, k):
        if sequence[i] < sequence[k]:
            if i in length_dp:
                temp = length_dp[i]
            else:
                temp = lis(i)
            if temp+1 > best:
                best = temp+1
    length_dp[k] = best
    return best

print(max([lis(i) for i in range(0, len(sequence))]))

# --------

# Iterative Approach (calc all values for length and then take the best result)
length = [1] * len(sequence)
for k in range(0, len(sequence)):
    length[k] = 1
    for i in range(0, k):
        if sequence[i] < sequence[k]:
            length[k] = max([length[k], length[i]+1]) # Store Best Result

print(max(length))


# fast way! (n log n)

# https://leetcode.com/problems/longest-increasing-subsequence/solutions/1326552/optimization-from-brute-force-to-dynamic-programming-explained/
# https://usaco.guide/gold/lis?lang=py
# super helpful !!

from bisect import bisect_left

def lis_fast(arr):
    sequence = []
    for i in arr:
        if len(sequence) == 0 or i > sequence[-1]:
            sequence.append(i)
        else:
            smallest = bisect_left(sequence, i)
            sequence[smallest] = i
    return len(sequence)
print(lis_fast(sequence))