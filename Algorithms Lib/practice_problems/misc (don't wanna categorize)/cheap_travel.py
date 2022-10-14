n, m, a, b = map(int, input().split())
# n = number of rides
# m = rides from m ride ticket
# a = price for one ride
# b = price for m ride

from math import ceil, floor
total = 0
if m * a < b:
    print(n*a)
else:
    print(min(ceil(n / m)*b, floor(n/m)*b+(n%m)*a)) # Sometimes it's better to buy more rides than needed
