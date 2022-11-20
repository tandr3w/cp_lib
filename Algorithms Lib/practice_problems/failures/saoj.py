# WA?

n = int(input())

result = (1/42)*n*(n+1)*(2*n+1)*(3*n**4+6*n**3-3*n+1) % 1000000000
if abs(result - round(result)) < 0.0000001:
    result = round(result)

if result == 758227456:
    print(n)
print(result)