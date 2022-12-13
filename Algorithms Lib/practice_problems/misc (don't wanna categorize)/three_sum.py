# O(N^2)
# Try all possible values of the 3rd pointer

n, x = map(int, input().split())

arr = list(map(int, input().split()))
for i in range(n):
    arr[i] = (arr[i], i+1)
arr.sort()

win = False
for third in range(n):
    l = 0
    r = n-1
    while l < r and l < n:
        while l < r and arr[r][0] + arr[l][0] + arr[third][0] > x:
            r -= 1
        if l >= r:
            break
        if l != third and r != third and arr[r][0] + arr[l][0] + arr[third][0] == x:
            print(*[arr[l][1], arr[r][1], arr[third][1]])
            win = True
            break
        if arr[r][0] + arr[l][0] + arr[third][0] > x:
            r -= 1
        else:
            l += 1
    if win:
        break
if not win:
    print("IMPOSSIBLE")