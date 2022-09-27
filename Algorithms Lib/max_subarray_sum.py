# Find the subarray with the biggest sum

def slowSolution(): # O(n^3)
    best = 0
    arr = [1, 2, 6, 4, -51, 3, -6, 9, 12, 4]
    for i in range(0, len(arr)):
        for j in range(i+1, len(arr)+1):
            sum = 0
            for k in range(i, j):
                sum += arr[k]
            if sum > best:
                best = sum
    return best


def fasterSolution(): # O(n^2)
    best = 0
    arr = [1, 2, 6, 4, -51, 3, -6, 9, 12, 4]
    for i in range(0, len(arr)):
        sum = 0
        for j in range(i+1, len(arr)):
            sum += arr[j] # Calculates sum while creating subarrays
            if sum > best:
                best = sum
    return best

def bestSolution():
    arr = [1, 2, 6, 4, -51, 3, -6, 9, 12, 4]
    best = 0
    sum = 0
    for i in range(0, len(arr)): 
        sum = max(arr[i], sum+arr[i]) # Each subarray is either just i, or a previous subarray ending at i-1, plus i.
        if sum > best:
            best = sum
    return best

print(bestSolution())