from sys import stdin
input = stdin.readline

n = int(input())
# queue = input()
queue = "a"*100000
result = ""
result += queue[0]
queue = queue[1:]

while len(queue) > 0:
    if ord(queue[0]) > ord(result[0]):
        result += queue[0]
        queue = queue[1:]
    else:
        result = queue[0] + result
        queue = queue[1:]

print(result)