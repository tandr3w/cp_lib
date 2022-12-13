n = int(input())
str1 = input()
str2 = str1[::-1]

memo = [[0]*(n+1) for i in range(n+1)]
for i in range(n+1):
    memo[i][len(str2)] = 0
for j in range(n+1):
    memo[len(str1)][j] = 0
for i in reversed(range(n)):
    for j in reversed(range(n)):
        if str1[i] == str2[j]:
            memo[i][j] = memo[i+1][j+1] + 1
        else:
            memo[i][j] = max(memo[i+1][j], memo[i][j+1])
print(memo)
print(n - memo[0][0])


# With Length instead of l and r. L also shifts based on the starting index. 
memo = [[0]*(5001) for i in range(5001)]
for l in range(2, n):
    for i in range(1, n-l+1):
        if str1[i] == str1[i+l-1]:
            memo[l][i] = memo[l-2][i+1]
        else:
            memo[l][i] = min(memo[l-1][i], memo[l-1][i+1]) + 1
print(memo[n][1])

