# A flat runway is given in the form of a list with spikes that will kill you (need to be avoided)
# You have a starting speed (how many elements you can jump). Every time you jump, you can change your speed by 1 for the next one.

# 1. Identify a DP problem
# Can it be solved with subproblems? Yes.
# The places you can jump depend on the places you jumped previously.

# 2. Which parameters change in the subproblems?
# The Speed
# The Position

# 3. Reccurance Relation: How would you compute the main problem if you had the answer to the subproblems?
# If we know the previous speed S, the next speed is S-1, S, or S+1.
# If you know the previous position P, the next position is P+S-1, P+S, or P+S+1
# The result is a boolean, so the algorithm would be canStop(S, P) = canStop(S, P+S) or canStop(S+1, P+S+1) or canStop(S-1, P+S-1).

# 4. Base Case: Which subproblem is obvious and always the same (doesn't depend on another subproblem)?
# If P is on a spike, return False: if not runway[p]: return False.
# If P is out of bounds, return False: if p < 0 or p > len(runway), return False
# If S is 0, return True (we've stopped): if speed == 0, return True

# Let's program!
runway = [True, False, True, False]
dp_memo = {}

def addToMemo(s, p, trueOrFalse):
    dp_memo[p] = {s: trueOrFalse}

def canStop(s, p):
    if p < 0 or p >= len(runway): # Base Case
        return False
    if not runway[p]:
        return False
    if s == 0 and runway[p]:
        return True
    if p in dp_memo:
        if s in dp_memo[p]:
            return dp_memo[p][s]
    addToMemo(s, p, canStop(s, p+s) or canStop(s+1, p+s+1) or canStop(s-1, p+s-1)) # Recurrence Relation
    return dp_memo[p][s]
print(canStop(2, 0))
