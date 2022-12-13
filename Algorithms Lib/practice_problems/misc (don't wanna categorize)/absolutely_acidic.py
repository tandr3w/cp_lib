n = int(input())
readings = [0] * 1001
for i in range(n):
    x = int(input())
    readings[x] += 1

# Cases:
# One of each: Just return the abs between them
# Multi of second but one first: Either the largest or smallest second
# One of second but multi first: Either the largest or smallest first
# Multi of both: L-S, S-L, S-S, L-L

best = max(readings)
second = -1

bests = []
seconds = []

for i in range(1001):
    if readings[i] < best:
        second = max(readings[i], second)
for i in range(1001):
    if readings[i] == best:
        bests.append(i)
    if readings[i] == second:
        seconds.append(i)

if len(bests) > 1:
    print(max(bests) - min(bests))
if len(bests) == 1 and len(seconds) == 1:
    print(abs(bests[0] - seconds[0]))
if len(bests) == 1 and len(seconds) > 1:
    print(max(abs(bests[0] - min(seconds)), abs(bests[0]-max(seconds))))
