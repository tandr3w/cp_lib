# Two pointers (USACO PROBLEM)

# import sys
# sys.stdin = open("diamond.in", "r")
# sys.stdout = open("diamond.out", "w")

n, k = map(int, input().split())

arr = []
for i in range(n):
    arr.append(int(input()))

arr.sort()

mins_li = [0]*n # Maximum number of diamonds assuming the smallest one is i
maxs_li = [0]*n # Maximum number of diamonds assuming all of them are less than i

j = 0
for i in range(n): # precalc for mins_li w/ two pointers
    while j < n and arr[j]-arr[i] <= k:
        j += 1
    mins_li[i] = j-i

j = n-1
for i in reversed(range(n)):
    while j >= 0 and arr[i]-arr[j] <= k:
        j -= 1
    maxs_li[i] = i-j

maxsp = [0]*n
maxsp[0] = maxs_li[0]
for i in range(1, n):
    maxsp[i] = max(maxsp[i-1], maxs_li[i])

ans = 0
for i in range(n):
	ans = max(ans, mins_li[i] + maxsp[i])
if ans > n:
    ans = n
print(ans)


