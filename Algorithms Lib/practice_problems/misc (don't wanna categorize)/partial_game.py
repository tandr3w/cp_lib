n = int(input())
stones = [0] * n
duke_moves = 0
alice_moves = 0
a = list(map(int, input().split()))
for i in range(len(a)):
    if int(a[i]) % 2 == 0:
        duke_moves += int(a[i]) / 2
    else:
        alice_moves += int(a[i]+1) / 2
if duke_moves > alice_moves:
    print("Duke")
else:
    print("Alice")

