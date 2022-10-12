donations = [10, 3, 2, 5, 7, 8]

# State: Maximum value for a prefix of the array
# Relation: 

# Variables: Donation List
def solve(k): # Calculates max donation amount for donations[k:]
    if k == 0:
        return donations[0]
    if k == 1:
        return max(donations[0], donations[1])
    return max()

print(solve(0))