from math import ceil, inf
def solve(piles, k):
    def possible(r):
        hours = 0
        for i in piles:
            hours += ceil(i / r)
        if hours <= k:
            return True
        else:
            return False
    bottom = 1
    top = max(piles)
    if top == bottom:
        return top
    best = inf
    while bottom <= top:
        mid = (bottom + top) // 2
        if possible(mid):
            if mid < best:
                best = mid
            top = mid - 1
        else:
            bottom = mid + 1
    return best

print(solve([1], 1))