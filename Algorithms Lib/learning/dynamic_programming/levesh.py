str_x = "movie"
str_y = "loveszz"

def cost(a, b):
    if str_x[a] == str_y[b]:
        return 0
    else:
        return 1

dp_dict = [[None] * len(str_y) for i in range(0, len(str_x))]

def distance(a, b): # a, b are the prefixes (first n characters) of strings x and y.
    if dp_dict[a][b] != None:
        return dp_dict[a][b]
    if a < 0:
        return max(0, b+1) # Base Case
    if b < 0:
        return max(0, a+1) # Base Case
    dp_dict[a][b] = min(
                distance(a, b-1) + 1, # Inserting into A
                distance(a-1, b) + 1, # Removing from A
                distance(a-1, b-1) + cost(a, b) # Modifying (or don't change)
            )
    return dp_dict[a][b]

print(distance(len(str_x)-1, len(str_y)-1))