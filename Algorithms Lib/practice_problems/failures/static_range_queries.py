n, q = map(int, input().split())

# 1 7 5
# 3 10 2
# 2 5 1

# https://codeforces.com/gym/102951/problem/D


# 1 2 3  6  8 11
# 5 1 2 -1 -5 -2 (DA)

# to sort, can store as: (1, 5), (2, 1), (3, 2), (6, -1), (8, -5), (11, -2)

# then, query (2, 9), (3, 5), (3, 6), (7, 20). need to add each of them - 1 to the DA
# so: (1, 5), (2, 1), (3, 2), (4, 0), (5, -1), (6, 0), (8, -5), (11, -2), (19, 0)
# then, PSA twice

# then, correspond all the spots using a dict
# 1:0, 2:1, 3:2, 4:3, 5:4, 6:5, 8:6, 11:7, 19:8
# then, for each of the queries
# (2, 9) = psa(6) - psa(0) = psa(compressed[8]) - psa(compressed[1])
# (3, 5) = psa(3) - psa(1) = psa(compressed[4]) - psa(compressed[2])
# (3, 6) = psa(4) - psa(1)
# (7, 20) = psa(8) - psa(5)

vals = []
queries = []
compressed = {}
compressedinit = {}
used = set()

count = -1
for i in range(n):
    l, r, v = map(int, input().split())
    if l in used:
        vals[compressedinit[l]][1] += v
    else:
        count += 1
        vals.append([l, v])
        used.add(l)
        compressedinit[l] = count
    if r in used:
        vals[compressedinit[r]][1] -= v
    else:
        count += 1
        vals.append([r, 0-v])
        compressedinit[r] = count
        used.add(r)
    
print(vals)
print(compressedinit)
vals.sort()
print(vals)

for i in range(1, len(vals)):
    vals[i][1] = vals[i][1] + vals[i-1][1]

for i in range(q):
    l, r = map(int, input().split())
    queries.append([l, r])
    if l-1 not in used:
        vals.append([l-1, 0])
    if r-1 not in used:
        vals.append([r-1, 0])

vals.sort()
print(vals)
for i in range(len(vals)):
    compressed[vals[i][0]] = i
print(compressed)

for i in range(1, len(vals)):
    vals[i][1] = vals[i][1] + vals[i-1][1]

for query in queries:
    if query[1] == 0:
        print(vals[compressed[query[1]-1]])
    else:
        print(vals[compressed[query[1]-1]][1] - vals[compressed[query[0]-1]][1])