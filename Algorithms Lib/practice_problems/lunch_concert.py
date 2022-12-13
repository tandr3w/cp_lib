# Binary Search Solution
# Let s = sum
# Let l = the amount that leftSum changes by when walking to the left (every time you walk left, s decreases by l since you become closer)
# Let r = the amount that rightSum changes by when walking to the left (every time you walk right, s increases by r since you become farther)
# There are two ways where l and r can change. If you move into the range of a person on the left, walking left more won't shorten the time for that specific person. Thus, l -= w for that person
# If you pass the range of a person on the right, that person will have to start walking more if you keep moving to the left. Thus, r += w for that person.
# Observe that the total amount that sum increases by when walking left can ONLY increase. Thus, this is something we can binary search.
# At each step, if r - l is negative, that means we should keep moving left since it's profitable (the optimal solution is on the left).
# If r - l is positive, that means the sum will increase if we keep moving left, so the optimal solution is on the right. We just need to find the point where it switches from negative to positive (or zero) and stop there.

n = int(input())
plist = []
from math import inf
lower_bound = inf # Pos of leftmost person
higher_bound = 0 # Pos of rightmost person
# Optimal answer is always between lower_bound and higher_bound

def s(i): # The answer for a certain point
    out = 0
    for j in plist:
        temp = abs(i-j[0])-j[2] # distance they have to walk
        if temp > 0:
            out += temp*j[1]
    return out

for i in range(n):
    plist.append(list(map(int, input().split())))

    if plist[i][0] < lower_bound: # set to pos of leftmos person
        lower_bound = plist[i][0]

    if plist[i][0] > higher_bound: # set ot pos of rightmost person
        higher_bound = plist[i][0]

while lower_bound <= higher_bound:
    mid_point = (lower_bound+higher_bound)//2
    leftSum = s(mid_point-1) # check whether left is lower
    rightSum = s(mid_point+1) # check if right side is lower
    midSum = s(mid_point)
    if (midSum < leftSum and midSum < rightSum) or (midSum == leftSum or midSum == rightSum): # Optimal solution since going to the left or right are both bad
        break
    else:
        if midSum < rightSum: # optimal solution is on the left
            higher_bound = mid_point - 1
            continue
        else: # optimal solution is on the right
            lower_bound = mid_point + 1
            continue
print(midSum)