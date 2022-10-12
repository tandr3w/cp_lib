# Giving up on this for now

from sys import stdin, stdout
input = stdin.readline
# print = stdout.write

t = int(input())

for i in range(t):
    n, k = map(int, input().split())
    psa = list(map(int, input().split()))
    print(str(psa))

    if k == 1: # PSA with 1 element is the same as the original array, which satisfies the conditoins
        print("YES")
        continue

    arr = [0] * (n+1)
    for i in range(n-k+2, n):
        arr[i] = psa[i] - psa[i-1]
    print(str(arr))
    
    if arr != sorted(arr): # Already Failed
        print("NO")
        continue
    
    if psa[n-k+1] > (n-k+1) * arr[n-k+2]:
        print(str(psa[n-k+1]))
        print(str((n-k+1) * arr[n-k+2]))
        print("NO")
        continue
    
    print("YES")
