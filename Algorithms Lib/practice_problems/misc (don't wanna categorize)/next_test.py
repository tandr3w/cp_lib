# No idea why this is rated 1200, it's ridiculously easy

n = int(input())
arr = list(map(int, input().split()))
arr = sorted(arr)
count = 1
while True:
    if count not in arr:
        print(count)
        break
    count += 1
