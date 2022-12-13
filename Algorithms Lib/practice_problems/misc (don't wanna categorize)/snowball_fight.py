n, t = map(int, input().split())

initials = [0] + list(map(int, input().split()))
students = [[] for i in range(n+1)]
finals = [0 for i in range(n+1)]

for i in range(1, n+1):
    students[i].append(initials[i])

toAdd = [-1 for i in range(n+1)]
for i in range(t):
    for idx in range(1, n+1):
        if len(students[idx]) > 0:
            temp = students[idx].pop(0)
            finals[idx] = temp
            toAdd[idx] = temp
    for i in range(1, n+1):
        if toAdd[i] != -1:
            students[toAdd[i]].append(i)
            toAdd[i] = -1

print(" ".join(list(map(str, finals[1:]))))

