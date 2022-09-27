n = int(input())
c = 0
for i in range(n):
    x = input().split()
    if x.count("1") >= 2:
        c += 1
print(c)