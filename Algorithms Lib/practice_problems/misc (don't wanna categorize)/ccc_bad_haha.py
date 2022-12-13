t = int(input())
for i in range(t):
    n = input()
    digits = list(map(int, list(n)))
    k = int(input())
    idx = 0
    to_remove = []
    while len(digits) and idx < len(digits) and k > 0:
        if idx < 0:
            idx = 0
        if idx == len(digits)-1 or digits[idx] > digits[idx+1]:
            to_remove.append(digits[idx])
            digits.pop(idx)
            idx -= 2
            k -= 1
        idx += 1
    to_remove.sort()
    for j in to_remove:
        digits.append(j)
    digits = list(map(str, digits))
    print("".join(digits))
