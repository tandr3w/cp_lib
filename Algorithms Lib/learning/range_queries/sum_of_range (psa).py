# Calculate the sum within a range (with multiple queries). This includes the sum up to a point. Look for if there are a lot of queries.
list = [1, 4, 6, 7, 4, 7, 8, 4, 4, 4]

def naive_solution(l, r): # Has to loop through everything every time you call it!
    sum = 0
    for i in list[l:r]:
        sum += i
    return sum

def psa_init(arr): # Only has to loop once for the initialization, then each query is O(1)
    # You can also do this in a one-liner without declaring new variables in case of MLE (check volcano)
    psa = [0] * len(arr)
    psa[0] = arr[0]
    for i in range(1, len(arr)):
        psa[i] = arr[i] + psa[i-1]
    return psa

def calc(l, r, li): # With a PSA, we can now calculate the sum of a range [l:r] (inclusive) in O(1) by subtracting r - l. 
    if l == 0:
        return li[r]
    else:
        return li[r] - li[l-1]

psa = psa_init(list)
print(list)
print(psa)
print(calc(2, 6, psa))
