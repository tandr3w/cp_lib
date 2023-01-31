n = int(input())
garden = list(map(int, input().split()))

def calc_twos(x):
    count = 0
    while x % 2 == 0:
        x //= 2
        count += 1
    return count

for i in range(n):
    garden[i] = calc_twos(garden[i])

precalc = [1, 2]
for i in range(2, 63):
    precalc.append((precalc[i-1] * precalc[i-1] + 1 ) % 1000000007)

sum = precalc[garden[0]]
for i in range(1, n):
    sum *= precalc[garden[i]]
    sum = sum % 1000000007
print(sum)