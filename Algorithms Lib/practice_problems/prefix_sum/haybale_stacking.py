# Source: https://usaco.guide/general/io

n, k = map(int, input().split())
diffArr = [0] + [0] * n
print(diffArr)

def psa_init(arr): # Only has to loop once for the initialization, then each query is O(1)
    psa = [0] * len(arr)
    psa[0] = arr[0]
    for i in range(1, len(arr)):
        psa[i] = arr[i] + psa[i-1]
    return psa

def update(l, r, amt):
    diffArr[l] += amt
    if r+1 < len(diffArr):
        diffArr[r+1] -= amt

for i in range(k):
    l, r = map(int, input().split())
    update(l, r, 1)

result = psa_init(diffArr)
result.pop(0)
result = sorted(result)
print(result[(n-1)/2])
