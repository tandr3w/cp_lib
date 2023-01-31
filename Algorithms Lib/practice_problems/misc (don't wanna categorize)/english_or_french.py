n = int(input())
string = ""
for i in range(n):
    string += input()
if string.count("t") + string.count("T") > string.count("s") + string.count("S"):
    print("English")
else:
    print("French")