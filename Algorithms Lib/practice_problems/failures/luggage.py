# TLEs for some reason
# Time complexity should be n log n
# i should've just used bisect smh

n, k = map(int, input().split())
items = list(map(int, input().split()))
if len(items) == 2: # Idk why but this edge case fails
    if items[-1] - items[0] <= k:
        print(2)
    else:
        print(1)
else:
    items = sorted(items)
    best = 1
    for j in range(n-1): # Try each starting index
        if n-j < best:
            break
        x = 0
        m = n-j-1
        while m != 1: # Bsearch to find the optimal subarray for starting index
            m = m // 2
            while x + m < n-j and items[x+m] - items[0] <= k:
                x += m
        best = max(best, x+1) # Store best
        items.pop(0)
    print(best)