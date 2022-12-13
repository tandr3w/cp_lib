# this is just coin problem lol

dist = int(input())
clubs = []
for i in range(int(input())):
    clubs.append(int(input()))

values = {}
# first = {}
values[0] = 0
import math
def solve_dp(x):
    if x == 0:
        return 0
    if x < 0:
        return math.inf
    if x in values:
        return values[x]
    best = math.inf
    for club in clubs:
        res = solve_dp(x-club)+1
        if res < best:
            # first[x] = club
            best = res
    values[x] = best
    return best

ans = solve_dp(dist)
if ans == math.inf:
    print("Roberta acknowledges defeat.")
else:
    print("Roberta wins in " + str(ans) + " strokes.")
# x = dist
# while x > 0:
#     print(first[x], end=", ")
#     x -= first[x]