# Given an n*n grid where each square has a value, calculate the optimal path from the top-left to bottom-right corner where you can only move down or right that has the largest sum of values.

grid = [[3, 7, 9, 2, 7], 
        [9, 8, 3, 5, 5], 
        [1, 7, 9, 8, 5],
        [3, 8, 6, 4, 10],
        [6, 3, 9, 7, 8]]

dp_list = [[None] * len(grid) for i in range(len(grid))]
print(dp_list)

def sum(x, y):
    # Possible paths are (x-1, y) and (x, y-1)
    if x == 0 and y == 0:
        return grid[0][0]
    if dp_list[x][y] != None:
        return dp_list[x][y]
    best_x, best_y = 0, 0
    if x > 0:
        best_x = sum(x-1, y) + grid[x][y]
    if y > 0:
        best_y = sum(x, y-1) + grid[x][y]
    dp_list[x][y] = max(best_x, best_y)
    return dp_list[x][y]

print(sum(len(grid[0])-1, len(grid)-1))
print(dp_list)