n = int(input()) # pieces
k = int(input()) # people

memo = [[[False]*n for j in range(k)] for l in range(n)]

def dp(pieces_remaining, people_remaining, minimum):
    if not memo[pieces_remaining-1][people_remaining-1][minimum-1] == False:
        return memo[pieces_remaining-1][people_remaining-1][minimum-1]
    if people_remaining == 0:
        if pieces_remaining == 0:
            return 1
        else:
            return 0
    upper_bound = (pieces_remaining // people_remaining) # max pieces per person

    if upper_bound < minimum or pieces_remaining < 0:
        return 0

    count = 0
    for i in range(minimum, upper_bound+1):
        count += dp(pieces_remaining-i, people_remaining-1, i)
    memo[pieces_remaining-1][people_remaining-1][minimum-1] = count
    return count

print(dp(n, k, 1))
