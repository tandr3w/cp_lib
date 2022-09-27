from sys import stdin # Very important if there are a lot of inputs, like here where there can be millions!

n, k = stdin.readline().split()
n = int(n)
k = int(k)

# Put stones
arr = [0] * n
for i in range(k):
    arr[int(stdin.readline())] += 1

# PSA init
psa = [0] * n
psa[0] = arr[0]
for i in range(0, n):
    psa[i] = arr[i] + psa[i-1]

q = int(stdin.readline())
for i in range(q):
    a, b = stdin.readline().split()
    a = int(a)
    b = int(b)
    if a == 0:
        print(psa[b])
    else:
        print(psa[b] - psa[a-1])
