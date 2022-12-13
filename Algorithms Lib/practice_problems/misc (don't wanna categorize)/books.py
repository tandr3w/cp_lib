# Basic 2 pointers
n, t = map(int, input().split())
books = list(map(int, input().split()))
secondpointer = 0
sum = 0
best = 0
for i in range(n):
    if i > 0:
        sum -= books[i-1]
    if secondpointer < len(books):
        while sum + books[secondpointer] <= t:
            sum += books[secondpointer]
            secondpointer += 1
            if secondpointer >= len(books):
                break
    best = max(best, secondpointer-i)
print(best)
    
