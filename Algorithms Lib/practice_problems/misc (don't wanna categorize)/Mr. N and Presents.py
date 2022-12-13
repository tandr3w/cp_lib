q = int(input())
dic = {}
students = []

for i in range(q):
    t, x = input().split()
    x = int(x)
    if t == "F":
        students.insert(0, [i, x])
        dic[x]=i
    if t == "E":
        students.append([i, x])
        dic[x]=i
    if t == "R":
        dic[x]=-1

for student in students:
    if student[0] == dic[student[1]]:
        print(student[1])