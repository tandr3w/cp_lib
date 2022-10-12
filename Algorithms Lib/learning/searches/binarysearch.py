# Works on sorted arrays only. Search algorithm with an O(log n) time complexity
# Cuts input in half until item is found.

sortedArr = [-7, -4, 1, 2, 5, 7, 8, 9]

def binarySearch(target, arr):
    l = 0
    r = len(sortedArr)-1

    while l <= r:
        mid = (r+l)//2
        if arr[mid] < target:
            l = mid + 1
        if arr[mid] > target:
            r = mid - 1
        if arr[mid] == target:
            print("Found!")
            return mid

    return "Not Found"

def binarySearchAlternative(target, arr):
    k = 0
    n = len(arr)-1
    while n != 1:
        n = n // 2 # Halve the jump size each time
        # If after the jump, it will be less than the element, make the jump. Basically, if the jump makes it too big, half the jump size. If it makes it too small, make the jump and repeat.
        while k + n < len(arr) and arr[k + n] <= target: # Len check has to be first to prevent overflow
            k += n
    if arr[k] == target:
        print("Found!")
        return k
    else:
        return "Not Found"

print(binarySearch(1, sortedArr))

# In python, you can use bisect_left(arr, target, min=0, max=len(arr)) to get the first index with a value at least the target
# Or bisect_right(arr, target, min=0, max=len(arr)) to get the first index with a value greater than the target.
from bisect import bisect_left
from bisect import bisect_right
print(bisect_left(sortedArr, 1))
print(bisect_right(sortedArr, 1))

# Binary search can also be used to find the first item where a function changes, if you replace the < > operators.
# For instance:

def okay(i):
    if i < 0:
        return False
    else:
        return True

def binarySearchFunc(arr):
    l = 0
    r = len(sortedArr)-1

    while l <= r:
        mid = (r+l)//2
        if not okay(arr[mid]):
            l = mid + 1
        if okay(arr[mid]):
            r = mid - 1
    
    if okay(arr[mid]):
        print("Found!")
        return mid

    return "Not Found"

print(binarySearchFunc(sortedArr))

