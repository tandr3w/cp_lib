# Query minimum without searching through the entire array

# Precalculate all values of min() for all ranges (a, b) where the length of the range is a power of two (1, 2, 4, 8, 16, etc.)
# Then, you can represent any length range by combining two intervals that are a power of two long (for the same reason that you can represent any number with only powers of two).
# e.g. min(2, 14) = min(min(2, 9), min(10, 13), min(14, 14)) -- precomputes in O(n log n), queries in O(1)
# Way better than precomputing everything which is O(n^2)

# https://www.youtube.com/watch?v=0jWeUdxrGm4&list=PLl0KD3g-oDOEbtmoKT5UWZ-0_JbyLnHPZ&index=17


arr = [1, 3, 4, 8, 6, 1, 4, 2]
n = len(arr)

from math import log2, ceil
k = ceil(log2(n))+1
table = []
for m in range(n):
    table.append([None]*(k))

for p in range(len(table)):
    table[p][0] = arr[p]

# For each power of two length, for each starting index, store the minimum sum.
for j in range(1, k):
    i = 0
    while ((i + 2**j) - 1) < n:
        table[i][j] = min(table[i][j-1], table[i + (2**(j-1))][j-1])
        i += 1

def query(l, r):
    length = r - l + 1
    k = 0
    while 2 ** (k+1) <= length: # Find the maximum power of 2 that fits
        k += 1
    return min(table[l][k], table[r-(2**k)+1][k]) 
    # Break it down into two ranges: One that starts at the start of the range and one that ends at the end of the range, both with length 2^k. The result is the minimum of the range (overlap doesn't matter). Remember that table stores minimums of ranges table[i][k] where i is the starting point and k is the power of two that's the length.

print(query(1, 3)) # Should return 3


