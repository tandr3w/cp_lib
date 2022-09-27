k = int(input())
unlucky = list(map(int, input().split()))
n = int(input())

arr = [0] * 1000001
for i in unlucky:
    arr[i] = 1

def psa_init(arr): # Only has to loop once for the initialization, then each query is O(1)
    psa = [0] * len(arr)
    psa[0] = arr[0]
    for i in range(1, len(arr)):
        psa[i] = arr[i] + psa[i-1]
    return psa

psa = psa_init(arr)
for i in range(n):
    j = int(input())
    print(j - psa[j])