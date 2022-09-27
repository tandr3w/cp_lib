# Essentially, big-o notation is how the algorithm correlates with the size of the data, and only the order of magnitude.
l = ['a', 'b', 'c'] # Data size (n) = 3
for i in l:
    print("This has a big-o notation of O(n), since it's linear to the data")

for i in l:
    print("If I repeat it, it still has a big-o notation of O(n)")

for i in l:
    for j in l:
        print("This has a big-o notation of O(n^2) since it's exponential to the size of the data")

# Since this calls itself n times and the time complexity of each call is O(1) (no input), it has a time complexity of O(n)
def f(n):
    if n == 1:
        return
    f(n-1)

# General required time complexity vs input size
# n ≤ 10 -- O(n!)
# n ≤ 20 -- O(2^n)
# n ≤ 500 -- O(n^3)
# n ≤ 5000 -- O(n^2)
# n ≤ 10^6 -- O(nlogn) or O(n)
# n is large -- O(1) or O(logn)

# Most common places you find each time complexity
# O(1) -- constant time
# O(log n) -- halves input of each step
# O(sqrt n)
# O(n) -- goes through input a constant number of times
# O(n log n) -- sorts input or uses a data structure where each op takes O(log n)
# O(n^2) -- nested loop
# O(n^3) -- two nested loops
# O(2^n) -- goes through every subset of input
# O(n!) -- goes through every permutation