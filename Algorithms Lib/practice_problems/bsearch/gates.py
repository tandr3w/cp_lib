# finally learned how to use bisect!

from bisect import bisect_left
g = int(input())
p = int(input())
available = [0] + [i+1 for i in range(g)]
mySet = set(available)

for i in range(p):
    plane = int(input())
    successful = False
    if plane in mySet:
        mySet.remove(plane)
        available.remove(plane)
        successful = True
    else:
        next_available = bisect_left(available, plane)-1
        if next_available > 0:
            mySet.remove(available[next_available])
            available.pop(next_available) # this is the problem, too slow
            successful = True
        else:
            print(g - len(available) + 1)
            break

if successful:
    print(p)
