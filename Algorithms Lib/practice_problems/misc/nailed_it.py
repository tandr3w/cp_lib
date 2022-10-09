n = int(input())
wood = list(map(int, input().split()))
pairs_dict = {}

for i in range(len(wood)-1):
    for j in range(i+1, len(wood)):
        if wood[i] + wood[j] not in pairs_dict:
            pairs_dict[wood[i] + wood[j]] = 1 
        else:
            pairs_dict[wood[i] + wood[j]] += 1

total_count = 0
best = 0

values = list(pairs_dict.values())
max = max(values)

print(max, end=" ")
print(values.count(max),)