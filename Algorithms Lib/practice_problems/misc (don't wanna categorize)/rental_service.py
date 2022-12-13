# USACO problem
# http://www.usaco.org/index.php?page=viewproblem2&cpid=787

# We always want to use all the cows, rent the worst cows, and milk the best cows
# Example testcase:
# Cows: 6 2 4 7 1 --> 1 2 4 6 7
# Shops: (10 25), (2 10), (15 15)
# Rents: 250 100 80 40 (sorted)

# We basically want to start renting starting from the worst cow (to the highest price), then find the point where we want to start selling. We can brute force these but with PSA
# Let rent_psa[i] = the max money we can get from renting the first i cows. We can just precalculate this directly
# Let milk_psa[j] = the max money we can get from milking the last j cows. We can also just precalculate this directly
# Then, we just try all values of i with j equaling n-i, and get the max

import sys
sys.stdin = open("rental.in", "r")
sys.stdout = open("rental.out", "w")

n, m, r = map(int, input().split())
cows = []
shops = []
rents = []
rents_psa = []
shops_psa = []

for i in range(n):
    cows.append(int(input()))
for i in range(m):
    x, y = map(int, input().split())
    shops.append([y, x])
for i in range(r):
    rents.append(int(input()))

cows.sort()
rents.sort(reverse=True)
shops.sort()

rents_psa.append(rents[0])
for i in range(1, n):
    if i >= r:
        rents_psa.append(rents_psa[i-1])
    else:
        rents_psa.append(rents[i] + rents_psa[i-1])

# print(rents_psa)

for i in range(0, n):
    if len(shops) == 0:
        if i == 0:
            shops_psa.append(0)
        else:
            shops_psa.append(shops_psa[i-1])
    else:
        gains = 0
        gallons_left = cows[n-i-1]
        while gallons_left:
            if gallons_left >= shops[-1][1]:
                gains += shops[-1][0] * shops[-1][1]
                gallons_left -= shops[-1][1]
                shops.pop()
                if len(shops) == 0:
                    break
            else:
                shops[-1][1] -= gallons_left
                gains += gallons_left * shops[-1][0]
                gallons_left = 0
        if i == 0:
            shops_psa.append(gains)
        else:
            shops_psa.append(shops_psa[i-1] + gains)
# print(shops_psa)

best = 0
for i in range(0, n-1):
    best = max(best, rents_psa[i] + shops_psa[n-i-2])
    # print(rents_psa[i], end=" ")
    # print(shops_psa[n-i-2])

best = max(best, rents_psa[-1])
best = max(best, shops_psa[-1])

print(best)