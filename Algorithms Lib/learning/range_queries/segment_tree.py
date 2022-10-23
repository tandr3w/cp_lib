# The Cooler Binary Indexed Tree
# Can do more stuff but takes more memory and is harder to implement
# Uses the same principle in that you can calculate any range as the sum of O(log(n)) ranges that are powers of two in length
# The bottom row is the array
# The next row up is the sum of two numbers in the array (2^1 range)
# The next row is the sum of four numbers in the array (2^2 range)
# etc. until one node covers the entire array
# To update an element, you just have to traverse the path to the element and update each value (O(log n) elements)
# You can also use this for min queries (just replace the addition with min) so who needs sparse tables smh

# IMPORTANT INFO!! 
# The array goes top-down and left-right in storing values. This makes it so index//2 is the parent of node infex and index*2 & index*2+1 are the children.
# For some reason that I'm too lazy to find out, it works for arbitrarily sized arrays as well, not just for powers of two. You can also just pad the array with 0s (or inf if you're using it for min) just in case, but that takes more memory.

# Code plagarised from https://www.youtube.com/watch?v=Oq2E2yGadnU (amazing video btw watch it to help understanding)

arr = [1, 5, 4, 7, 4, 6, 3, 2, 2]

def tree_init(arr): # Generates segment tree for array
    n = len(arr)
    tree = ([0] * n) + arr # Create bottom row and make space for rest of nodes (there will always be 2n nodes in the tree)
    index = n-1 # Calculate for each node from n-1 to 1
    while index > 0:
        tree[index] = tree[index*2] + tree[index*2+1] # Each node is the sum of its two child nodes (you can change this to min for min queries)
        index -= 1
    return tree

def update(index, value, arr, tree):
    n = len(arr)
    index += n # Start on corresponding index in the tree for the index in the array
    tree[index] = value # Change Value

    while index > 1:
        index //= 2 # Jump to parent
        tree[index] = tree[index*2] + tree[index*2+1] # Set value again for each parent of the changed node
    return tree

def calc_range(left, right, arr, tree):
    n = len(arr)
    left += n
    right += n
    sum = 0

    while left < right:
        if left % 2 == 1: # If the index is even, that means the node is the left-child of its parents, which means we can process it one layer up (the other child is in the range as well)
            sum = sum + tree[left]
            left += 1 # node was processed so remove it from the range
        if right % 2 == 1: # same thing as left, if it's the left child then since we're subtracting 1 first, we can process it one layer up.
            right -= 1 # subtract first because right is excluded in the range
            sum = sum + tree[right]
        left //= 2 # Move one layer up
        right //= 2
    return sum

tree = tree_init(arr)
print(tree)
# tree = update(2, 14, arr, tree)
# print(tree)
print(calc_range(4, 6, arr, tree)) # left is included, right is not
print(tree)



