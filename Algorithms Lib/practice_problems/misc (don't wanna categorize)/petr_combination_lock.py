n = int(input())
def turnAngle(angle, val, counter):
    if not counter:
        angle += val
        if angle >= 360:
            angle -= 360
    else:
        angle -= val
        if angle < 0:
            angle += 360
    return angle

turns = []
for i in range(n):
    turns.append(int(input()))

def recur(index, angle):
    if index >= n:
        if angle == 0:
            return True
        else:
            return False
    return recur(index+1, turnAngle(angle, turns[index], True)) or recur(index+1, turnAngle(angle, turns[index], False))

if recur(0, 0):
    print("YES")
else:
    print("NO")