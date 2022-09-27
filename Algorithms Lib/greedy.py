# A greedy algorithm is an algorithm that chooses the best short-term option and ignores all the previous choices in the decision. e.g. always choose the biggest number. They're usually very efficient, but it's hard to argue if they work as the locally optimal choices need to be globally optimal as well.

# Example problem: Find the minimum coins needed (out of 1c, 5c, 10c, 20c, 50c, 100c, 200c) needed to form a sum of money n.
# A greedy algorithm works here because 1. Coins 1c, 5c, 10c, 50c, and 100c can't appear more than once in an optimal solution, so a bigger coin will always be better in this scenario and 2. coins 2c and 20c can't appear more than once.
# However, if the coins were changed, there's no guarantee that a greedy algorithm would work.

# A lot of scheduling problems have greedy solutions.
# Example problem: Given n events with start / end times, find the schedule which fits as many events as possible (without overlap or partially attending events)
# Solution: Always choose the next possible event that ends as early as possible.

# Example problem: Given n tasks with deadlines and durations, where each task gives you deadline - duration points, find the maximum number of points you can get.
# The greedy algorithm here is to perform the tasks in order of shortest duration to longest duration

# Example problem: Given n numbers |a1 - x|^c + |a2-x|^c +...+ |an - x|^c minimize the sum.
# If c = 1, the best case is the median, if c = 2, the best case is the average.

# (Finish this later) Huffman coding is a good compressor and greedy algorithm.