# psa template problem lol (also demonstrates the importance of fast inputs)

import sys
input = sys.stdin.readline
n, q = map(int, input().split())
arr = list(map(int, input().split()))
psa = [arr[0]]
for i in range(1, n):
    psa.append(psa[i-1] + arr[i])

def calc(l, r, li):
    if l == 0:
        return li[r]
    else:
        return li[r] - li[l-1]

for i in range(q):
    l, r = map(int, input().split())
    print(psa[-1] - (calc(l-1, r-1, psa)))