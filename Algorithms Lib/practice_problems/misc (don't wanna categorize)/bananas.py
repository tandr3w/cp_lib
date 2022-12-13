# Basically, this approach is to simplify every monkey language word we can find to A until we can't anymore, then check if the result has been simplified to A.

# Ignoring B and S, every valid monkey language word is just alternating As and Ns. Thus, we can saftely convert all alternating ANANA patterns to A. Then, let's assume that every monkey language word without B or S is an A. 

# Then, we need to deal with B and S. The only remaining valid monkey language words will be some amount of Bs, followed by a single A, then some amount of Ss equal to the amount of Bs. Since these are valid we can also convert them to A.

# Finally, since there can be multiple monkey words in between each set, doing these steps may create new words we need to check. So, we need to repeat it until no valid monkey words are left other than "A". For example: BBANANASSNBANBASNAS --> BB[ANANA]SSNBAN[BAS]NAS --> B[BAS]SNB[ANANA]S --> [BAS]N[BAS] --> [ANA] --> A --> Yes
# ANABANANAS --> [ANA]B[ANANA]S --> A[BAS] --> AA --> Can't simplify --> No 

# If the steps stop in the middle and the result is not A, that means it's not a monkey language word.


# This is kinda a cheese approach tbh. If you want to do it recursively, here's how:
# Create a function that checks if a given word is valid. If it's surrounded by a B and S, you can safetly just delete those. Then, you separate the remainder into multiple subproblems and call them recursively.

while True:
    word = input()
    if word == "X":
        break
    else:
        while "ANA" in word or "BAS" in word:
            while "ANA" in word:
                word = word.replace("ANA", "A")
            while "BAS" in word:
                word = word.replace("BAS", "A")
        if word == "A":
            print("YES")
        else:
            print("NO")