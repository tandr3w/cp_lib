n, l = map(int, input().split())
lanterns = sorted(list(map(int, input().split())))

biggest = max(lanterns[0]*2, (l - lanterns[-1])*2)

for i in range(n):
    if i == 0:
        continue
    if lanterns[i] - lanterns[i-1] > biggest:
        biggest = lanterns[i] - lanterns[i-1]

print(biggest / 2)
