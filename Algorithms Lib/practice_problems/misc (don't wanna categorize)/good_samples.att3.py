n, m, k = map(int, input().split())
origk = k

filled = 0

result = []

for i in range(n):
    num_to_add=min(k-(n-i-1),m)
    ans = 0
    if num_to_add <= 0:
        break
    if num_to_add > i:
        num_to_add = min(m, i+1)
        ans = num_to_add
    else:
        ans = result[i-num_to_add]
    result.append(ans)
    k -= num_to_add

if k != 0 or n > origk:
    print(-1)
else:
    result = list(map(str, result))
    print(" ".join(result))