k, n = map(int, input().split())
marks = list(map(int, input().split()))
polycarps = list(map(int, input().split()))

def psa_init(arr): 
    psa = [0] * len(arr)
    psa[0] = arr[0]
    for i in range(1, len(arr)):
        psa[i] = arr[i] + psa[i-1]
    return psa

psa = psa_init(marks)

possible_starts = set()
for i in range(0, len(psa)):
    possible_starts.add(polycarps[0] - psa[i])

if len(polycarps) == 1:
    print(len(possible_starts))
else:
    total = 0
    for i in possible_starts:
        big_set = set()
        for j in psa:
            big_set.add(i + j)
        for k in polycarps[1:]:
            if k not in big_set:
                total -= 1
                break
        total += 1
    print(total)

