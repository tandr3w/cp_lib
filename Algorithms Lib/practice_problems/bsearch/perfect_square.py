# Check if a number is a perfect square using bsearch!
def solve(n):
    bottom = 0
    top = n
    if n == 0:
        return True
    if n == 1:
        return True
    while top - bottom > 1:
        mid = (bottom+top)//2
        temp = mid ** 2
        if temp == n:
            return True
        elif temp > n:
            top = mid
        elif temp < n:
            bottom = mid
    return False

print(solve(870))
