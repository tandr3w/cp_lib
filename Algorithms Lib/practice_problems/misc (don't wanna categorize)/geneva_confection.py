# guys be careful when you code lol, don't start implementing immediately. realize every part of the solution first

t = int(input())
for i in range(t):
    n = int(input())
    branch = []
    needed = 1
    possible = True
    li = []
    for j in range(1, n+1):
        li.append(int(input()))
    for j in range(n):
        next = li[n-j-1]
        if next == needed:
            needed += 1
        else:
            branch.append(next)
        while branch:
            if branch[-1] == needed:
                branch.pop()
                needed += 1
                continue
            else:
                break
    while branch:
        if branch[-1] == needed:
            branch.pop()
            needed += 1
            continue
        else:
            possible = False
            break
    if possible:
        print("Y")
    else:
        print("N")
