n = int(input())
people = sorted(list(map(int, input().split())))
from math import inf

best = inf
for i in range(len(people)-1): # Remove last element
    for j in range(i+1, len(people)):
        k = 0
        total = 0
        temp = people[:i] + people[i+1:j] + people[j+1:] 
        for k in range(0, len(temp), 2):
            total += temp[k+1] - temp[k]
            k += 2
        best = min(best, total)

print(best)

# 2 5 8 3 9 5 3 2