t = int(input())
for i in range(t):
    n = int(input())
    s = input()
    if s.count("0") == 1:
        print("BOB")
    elif s.count("0") % 2 == 0:
        print("BOB")
    else:
        print("ALICE")
