from math import ceil, sqrt
from sys import stdin

houses = [0] * 1414215 # Upper Bound
n, q = map(int, stdin.readline().split())
for i in range(n):
    x, y = map(int, stdin.readline().split())
    distance = ceil(sqrt(x**2 + y**2))
    houses[distance] += 1

for i in range(1, 1414215): 
    houses[i] += houses[i-1]
    
for i in range(q):
    print(houses[int(stdin.readline())])
