str1 = "Ab3bdE"
str2 = "db3bAE"

memo = [[-1]*(len(str2)+1) for i in range(len(str1)+1)]
def dp(pos1, pos2):
    if memo[pos1][pos2] != -1:
        return memo[pos1][pos2]
    if pos1 == len(str1) or pos2 == len(str2):
        return 0
    if str1[pos1] == str2[pos2]: # If we find matching characters, add them to the subsequence
        memo[pos1][pos2] = 1 + dp(pos1+1, pos2+1)
        return memo[pos1][pos2]
    memo[pos1][pos2] = max(dp(pos1+1, pos2), dp(pos1, pos2+1))
    return memo[pos1][pos2]

def dp_iter():
    memo = [[-1]*(len(str2)+1) for i in range(len(str1)+1)]
    for i in range(len(str1)+1):
        memo[i][len(str2)] = 0
    for j in range(len(str2)+1):
        memo[len(str1)][j] = 0
    for i in reversed(range(len(str1))):
        for j in reversed(range(len(str2))):
            if str1[i] == str2[j]:
                memo[i][j] = memo[i+1][j+1] + 1
            else:
                memo[i][j] = max(memo[i+1][j], memo[i][j+1])

# print(dp(0, 0))

dp_iter()
print(memo[0][0])


