m = int(input())
n = int(input())

rows = [0] * m
columns = [0] * n

k = int(input())
for i in range(k):
    paint_type, num = input().split()
    num = int(num)
    if paint_type == "R":
        rows[num-1] += 1
    if paint_type == "C":
        columns[num-1] += 1

count = 0 
for i in range(m):
    for j in range(n):
        if (rows[i] + columns[j]) % 2 == 1:
            count += 1
print(count)