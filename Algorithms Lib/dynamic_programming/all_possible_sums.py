# A knapsack problem is you're given a set and you have to find subsets with certain properties.
# Given a list of numbers, list all possible sums.

weights = [1, 3, 3, 5]
max_possible = sum(weights)
dp_list = dp_list = [[None] * (len(weights)) for i in range(max_possible+1)]
print(dp_list)

def possible(x, k): # Can you construct sum x with index k?
    if x == 0:
        return True
    if k == 0:
        if x == weights[k]:
            return True
        else:
            return False
    if dp_list[x][k] == None:
        dp_list[x][k] = possible(x, k-1) or possible(x-weights[k], k-1)
    return dp_list[x][k]
    
for i in range(0, max_possible+1):
    print(i, end="")
    print(": ", end="")
    print(possible(i, len(weights)-1))