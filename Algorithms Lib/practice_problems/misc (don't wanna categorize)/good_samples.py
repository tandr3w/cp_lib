# Need n-k samples

# Count up from 1, 2, 3... m, then repeat, adding n-1 good samples each time (or append the number n units away) until the required good samples is less than m-1, then shorten the jump back to fit the remainder. Then, repeat that same note to make sure no good samples are added.

# First, check if it's possible (k has to be less than somewhere around nm? and greater than n)) 

n, m, k = map(int, input().split())
filled = 0

result = []
reqk = k-n
next_note = "1"

while filled < n:
    # Need a check if it's the first sequence added of 123456...m since it will have more good samples (if len of result < m)
    if reqk <= 0: # Finished, fill rest
        temp = result[-1]
        for i in range(n-filled):
            result.append(temp)
        filled = n

    elif filled < m and (m/2) * (1 + m) > reqk:
        pass

    elif m*(m-1) > reqk:
        for i in range(m*(m-1)-reqk, m+1):
            result.append(str(i))
            if filled >= m: 
                reqk -= m-1
            else:
                reqk -= i-1
            filled += 1
            if filled == n or reqk == 0:
                break
    else: 
        for i in range(1, m+1):
            result += str(i)
            if filled >= m: 
                reqk -= m-1
            else:
                reqk -= i-1
            filled += 1
            if filled == n or reqk == 0:
                break

if filled == n and reqk > 0:
    print(-1)
else:
    print(" ".join(result))