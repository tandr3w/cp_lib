# easy problem
# state is the highest sum of numbers starting at a point

triangle = []
n = int(input())
for i in range(n):
    triangle.append(list(map(int, input().split())))
memo = [[0]*n for i in range(n)]
def dp(row, index):
    if memo[row][index] != 0:
        return memo[row][index]
    if row == n-1:
        return triangle[row][index]
    memo[row][index] = triangle[row][index] + max(dp(row+1, index), dp(row+1, index+1))
    return memo[row][index]

print(dp(0, 0))