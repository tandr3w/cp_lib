n, m, k = map(int, input().split())
filled = 0

result = []
reqk = k-n

# Adding the number x places back adds x-1 good samples, or filled-1 if filled < m
# If it's too much, decrease x by the amount it's too much by (the overflow)

def number_back(x): # Get the number after jumping back x spots
    return result[filled-x]

while filled < n:
    if reqk <= 200:
        pass
    if filled == 0:
        result.append(1) # Always start with 1
        filled += 1

    elif reqk <= 0: # Finished, fill rest
        temp = result[-1] # Get last element and repeat forever
        for i in range(n-filled):
            result.append(temp)
        filled = n

    elif filled < m: # The first sequence of 1 2 3 4 5 ... m has not been completed yet
        add_amt = number_back(1) + 1 # Count 1 2 3 4 5 ... m 1 2 3 4 5... until that results in a jump size too big
        if add_amt - 1 > reqk: # Jump size is too big
            overflow_amt = add_amt-1-reqk # Amt of excess good samples
            result.append(result[overflow_amt-1])
            reqk = 0
        else:
            result.append(add_amt)
            reqk -= add_amt - 1 # add_amt-1 good samples added
        filled += 1
    else: # The first sequence of 1 2 3 4 5 ... m has been completed
        if m-1 > reqk: # The jump will be too big
            overflow_amt2 = m-1-reqk # Decrease jump-back size by the amount its too big by
            result.append(number_back(overflow_amt2+1)) # Jump back less (PROBLEM IS PROBABLY HERE)
            reqk = 0
        else:
            result.append(number_back(m)) # Append the note m elements back (repeat the sequence)
            reqk -= m-1
        filled += 1

if reqk > 0 or n > k:
    print(-1)
else:
    result = list(map(str, result))
    print(" ".join(result))