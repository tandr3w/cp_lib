# Backtracking starts with an empty solution and builds it step by step.

# Example problem: Calculate the number of ways n queens can be placed on an n*n board where none of them are attacking each other.
# Can be solved by placing one queen on each row sequentially and checking which solutions are valid, also checking if the diagonal or column already has a queen when placing.

# Backtracking can become way more effecient by "pruning the tree", i.e., making it so the algorithm recognizes when a path doesn't work as early as possible.

# Optimization example problem: Calculate the number of paths in an n x n grid from the top-left to bottom-right that visits every square exactly once.
# Optimization 1: At the first step, you can move down or to the right, and each path moving down has a symmetric variant moving right (and vice versa). Thus, we can decide to only move down and multiply the answer by 2.
# Optimization 2: A path fails if it reaches the bottom-right too early.
# Optimization 3: If a path can't move forward and can turn either left or right, it will split the grid into two parts where you can't reach both, making the path fail.

# Meet in the middle is another (situational) way to optimize backtracking, which is to divide the search space into two parts and combine the results.
# Example problem: With a given list ([2, 4, 5, 9]), if you can make the number x (15) by adding
# Using meet in the middle: divide the list into two [2, 4], [5, 9] and calculate the sums of the numbers 
# [2, 4, 6], [5, 9, 14]. Then, we only need to check each element in the first list with each element in the second list, making it faster.
