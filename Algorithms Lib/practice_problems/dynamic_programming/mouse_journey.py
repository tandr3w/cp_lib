# Given an n*n grid where each square has a value, calculate the optimal path from the top-left to bottom-right corner where you can only move down or right that has the largest sum of values.

r, c = map(int, input().split())
grid = [[0 for i in range(c)] for j in range(r)]

dp_list = [[None] * c for i in range(r)]
k = int(input())
for i in range(k):
    x, y = map(int, input().split())
    grid[x-1][y-1] = "c"

# recursive (TLEs)
def sum(x, y): # state: num of ways to get to a square from the top left corner
    # Possible paths are (x-1, y) and (x, y-1)
    if x == 0 and y == 0:
        return 1
    if dp_list[x][y] != None:
        return dp_list[x][y]
    ans = 0
    if x > 0 and grid[x-1][y] != "c":
        ans += sum(x-1, y)
    if y > 0 and grid[x][y-1] != "c":
        ans += sum(x, y-1)
    return ans

# iterative
dp_list[0][0] = 1
for i in range(r):
    for j in range(c):
        if dp_list[i][j] == None:
            dp_list[i][j] = 0
        if i > 0 and grid[i-1][j] != "c":
            dp_list[i][j] += dp_list[i-1][j]
        if j > 0 and grid[i][j-1] != "c":
            dp_list[i][j] += dp_list[i][j-1]
print(dp_list[r-1][c-1])