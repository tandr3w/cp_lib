n, m = map(int, input().split())
restrictions = []
resolutions = [i for i in range(1, n+1)]

for i in range(m):
    restrictions.append(tuple(map(int, input().split())))

from itertools import chain, combinations
subsets = list(chain.from_iterable(combinations(resolutions, r) for r in range(len(resolutions)+1)))[1:]


# print(restrictions)
# print(subsets)

for subset in reversed(subsets):
    done = True
    for restriction in restrictions:
        if restriction[0] in subset and restriction[1] in subset:
            done = False
            break
    if done:
        print(len(subset))
        break
