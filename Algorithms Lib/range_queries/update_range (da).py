# Update the range in O(1) with multiple queries after O(n) initialization
# Difference Array is the exact opposite of prefix sum array -- the PSA of a difference array is equal to the original array.

list = [1, 4, 6, 7, 4, 7, 8, 4, 4, 4]

def naive_solution(l, r, updt_amt):
    for i in range(len(list[l:r])):
        list[i] += updt_amt

def da_init(arr):
    d_array = [0] * len(arr)
    d_array[0] = arr[0]
    for i in range(1, len(arr)):
        d_array[i] = arr[i] - arr[i-1]
    return d_array

def psa_init(arr): # Only has to loop once for the initialization, then each query is O(1)
    psa = [0] * len(arr)
    psa[0] = arr[0]
    for i in range(1, len(arr)):
        psa[i] = arr[i] + psa[i-1]
    return psa

def update(l, r, updt_amt, da):
    da[l] += updt_amt
    da[r] -= updt_amt
    return da

da = da_init(list)
print(psa_init(update(1, 4, 5, da)))


    
