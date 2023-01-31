import sys
print = sys.stdout.write

n, m = map(int, input().split())
from math import sqrt, ceil

prime_max = ceil(sqrt(m))+1
is_prime = [True for i in range(prime_max + 1)]
primes = []

for i in range(2, prime_max):
    if is_prime[i]:
        for j in range(i**2, prime_max+1, i):
            is_prime[j] = False
        primes.append(i)

prime_list = [True for i in range(m-n+1)]
for j in primes:
    start = n//j
    if start <= 1:
        start = j*2
    elif n % j != 0:
        start = (start*j)+j
    else:
        start *= j
    for k in range(start, m+1, j):
        prime_list[k-n] = False

for i in range(n, m+1):
    if prime_list[i-n]:
        print(str(i) + "\n")