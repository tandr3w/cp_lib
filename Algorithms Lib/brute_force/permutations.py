# Recursive solution:
# Basically, start with one letter [a], then add letters one at a time, generating a permutation for every possible position you can insert it in.
# Example: 'abc'
# Step 1: [a]
# Step 2: ab, ba
# Step 3: abc, acb, cab, bac, bca, cba

# However, the code works backwards
# Starting with [a, b, c], it splits it into the front and back
# [a, b], c
# Then, it inserts the back into every possible position for every permutation of the front, so we need to calculate every permutation of the front first.
# Split into front and back: [a], b
# Since the length of the list [a] is one, we already have every possible permutation so we've reached the base case. Then, we can find every possible position we can insert b; [a, b], [b, a]
# Then, going back up, we insert c in every possible position in both of these:
# In list [a, b]: [a, b, c], [a, c, b], [c, a, b]
# In list [b, a]: [b, a, c], [b, c, a], [c, b, a]
# And all of these permutations are appended into the returned list

def permutations(lis):
    if len(lis) == 1: # Base Case
        return [lis]

    output = []

    front = lis[:-1]
    last = lis[-1]
    
    # Working backwards
    for perm in permutations(front): # For each of the permutations in the previous step
        for i in range(len(perm) + 1): # Loop through all possible positions and create new permutation after inserting.
            new = perm[:i] + [last] + perm[i:]
            output.append(new)

    return output # In reverse order

print(permutations(['a', 'b', 'c']))


# Library solution:
import itertools
print(list(itertools.permutations([1, 2, 3])))