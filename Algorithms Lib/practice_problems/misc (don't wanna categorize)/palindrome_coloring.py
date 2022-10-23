# Idea: count num of pairs, divide by num of colors, add 1 if there are enough extras (non-pairs) for each color

t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    myString = input()
    myDict = {}
    for char in myString:
        if char in myDict:
            myDict[char] += 1
        else:
            myDict[char] = 1

    pairs = 0
    bonuses = 0
    for key in myDict:
        pairs += myDict[key]//2
        bonuses += myDict[key]%2

    result = (pairs//k) * 2
    if bonuses + 2*(pairs%k) >= k:
        result += 1
    print(result)
