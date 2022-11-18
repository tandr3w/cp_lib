n = int(input())

partners = {}

first = input().split()
second = input().split()
bad = 0

for i in range(n):
    if first[i] == second[i]:
        print("bad")
        bad = 1
        break
    partners[first[i]] = second[i]
    
if bad == 0:
    for i in range(n):
        if not partners[partners[first[i]]] == first[i]:
            print("bad")
            bad = 1
            break

if bad == 0:
    print("good")