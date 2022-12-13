# lessons:
# - sometimes you can brute force only one part of the problem to make it way easier and it will still pass
# - build up the solution, starting with a slow one that can be improved (the simulation) then improving it (the psa)

# count num of As, Bs, and Cs
# brute force every possible boundary: the index that the A index starts, then whether the next section is a B or C section.
# For each possibility, for everything in the A section that's not an A, swap that with an A in the correct section, or if there are none, just swap it with any A in the wrong section (you don't need to define this since the solution is math).
# then, the A section should be complete. Then, just count the number of Cs in the B section.

# however, the simulation part is too slow. is there a way to make it more efficient?
# yes. Count the number of incorrect characters in the A section, and also how many B (or C but only one) characters are in the A section. For each of those, you can save a swap. Then, you just need to count the number of incorrect characters in the B section.

# the ans is the num of incorrect characters in the A section, plus the num of incorrect characters in the next (B/C) section, then you subtract the amount of characters you can save (the num of B/C characters in the A section).

c = input()
a_size = c.count("A")
b_size = c.count("B")
c_size = c.count("C")

# Create a PSA that counts the amount of a characters in a range, then a PSA that counts the number of b characters in a range, and the same for c. Then, these are all the PSAs you need.
a_psa = [0]
for char in c:
    if char == "A":
        a_psa.append(a_psa[-1] + 1)
    else:
        a_psa.append(a_psa[-1])
a_psa = a_psa[1:]
b_psa = [0]
for char in c:
    if char == "B":
        b_psa.append(b_psa[-1] + 1)
    else:
        b_psa.append(b_psa[-1])
b_psa = b_psa[1:]
c_psa = [0]
for char in c:
    if char == "C":
        c_psa.append(c_psa[-1] + 1)
    else:
        c_psa.append(c_psa[-1])
c_psa = c_psa[1:]

def calc(l, r, li):
    if r >= len(c):
        r = r % len(c)
        if l < len(c):
            return calc(l, -1, li) + li[r]
    if l >= len(c):
        l = l % len(c)
    if l == 0:
        return li[r]
    else:
        return li[r] - li[l-1]

# print(a_psa)
# print(b_psa)
# print(c_psa)

import math
best = math.inf
for i in range(0, len(c)): # each value of i
    incorrect_a = calc(i, i+a_size-1, b_psa) + calc(i, i+a_size-1, c_psa)
    incorrect_b = calc(i+a_size, i+a_size+b_size-1, a_psa) + calc(i+a_size, i+a_size+b_size-1, c_psa)
    incorrect_c = calc(i+a_size, i+a_size+c_size-1, a_psa) + calc(i+a_size, i+a_size+c_size-1, b_psa)
    
    as_in_b = calc(i+a_size, i+a_size+b_size-1, a_psa)
    bs_in_a = calc(i, i+a_size-1, b_psa)
    as_in_c = calc(i+a_size, i+a_size+c_size-1, a_psa)
    cs_in_a = calc(i, i+a_size-1, c_psa)
    ans = min(
        incorrect_a + incorrect_b - min(as_in_b, bs_in_a),
        incorrect_a + incorrect_c - min(as_in_c, cs_in_a)
    )
    best = min(best, ans)
print(best)
