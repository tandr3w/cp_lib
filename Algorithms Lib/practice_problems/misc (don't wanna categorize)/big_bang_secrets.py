k = int(input())
word = input()
decoded = ""

for i in range(len(word)):
    shift_value = 3*(i+1) + k
    char = ord(word[i])
    char -= shift_value
    while char < 65:
        diff = 64-char
        char = 90-diff
    decoded += chr(char)

print(decoded)
