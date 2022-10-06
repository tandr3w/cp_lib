n = int(input())
queue = list(input())
result = []
result.append(queue.pop(0))

while len(queue) > 0:
    if ord(queue[0]) > ord(result[0]):
        result.append(queue.pop(0))
    else:
        result.insert(0, queue.pop(0))

print(str(result))