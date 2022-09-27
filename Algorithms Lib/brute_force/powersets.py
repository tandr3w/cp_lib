# Generating all subsets of a set (powerset):
# Note that the order doesn't matter in either each element or the powerset itself, since a set is, by definition, unordered. 

# Recursive solution
# Esseentially, each time we add a letter, we take each element of the current powerset and add the letter to the end of each element, and merge that into the powerset (doubling the size)
# e.g. for set (a, b, c, d), we start with the powerset {()}
# Then we add the letter a (to the empty item), so {()} + {a} = {(), a}
# Then we add the letter b to each element, so {(), a} + {b, ab} = {(), a, b, ab}
# Then we add the letter c to each element, so {(), a, b, ab} + {c, ac, bc, abc} = {(), a, b, ab, c, ac, bc, abc}
# Then we add the letter d to each element, so {(), a, b, ab, c, ac, bc, abc} + {d, ad, bd, abd, cd, acd, bcd, abcd} = {(), a, b, ab, c, ac, bc, abc, d, ad, bd, abd, cd, acd, bcd, abcd} -- etc.

def powerSet(str):
  result = [] # Create empty list

  def constructSubSet(subSet, index):
    if index >= len(str): # When all characters are added, add the final subset to the result
      # Process each subset here.
      result.append(subSet)
      return
    # Index 0: subset: ""
    # Index 1: two functions called, with subsets "" and "a", moved on to next character
    # Index 2: four functions called, with subsets ("" and "b") and ("a" and "ab")
    # Index 3: eight functions called, with subsets ("", "b", "a", "ab") and ("c", "bc", "bac", "abc"); No new subsets are constructed, everything is returned since index is 3.
    constructSubSet(subSet, index + 1) # Create element where nothing is added this step
    constructSubSet(subSet + str[index], index + 1) # Create element where next character is added this step
  
  constructSubSet("", 0)
  return result

# print(powerSet("abc"))


# Bit representation of integers solution
# Essentially, a set of all binary numbers up to a point is basically a powerset. 
# If you generate all binary numbers up to 2^n-1, then correspond each number to a letter in the set (1 = included and 0 = not included), you get the powerset.
# For example: set {a, b, c} has a length of 3
# Every binary number from 0 to 2^n-1 (2^3-1 = 7) is 000, 001, 010, 100, 011, 110, 111
# Then, let's make the first digit = a, the second digit = b, the third digit = c, and only include the letter if its corresponding digit is a one
# So then it turns into {(), a, b, c, ab, cb, abc} which is the powerset!!

def printPowerSet(set):
    pow_set_size = int(2**len(set)); # Calculate what to generate binary numbers up to
    counter = 0
    j = 0
     
    # Run from counter 000..0 to 111..1
    for counter in range(0, pow_set_size):
        for j in range(0, len(set)):
             
            # Check if jth bit in the counter is set. If set then print jth element from set
            if((counter & (1 << j)) > 0): # & is bitwise operator and << is bitshift
                print(set[j], end = "")
        print("")
 
set = ['a', 'b', 'c']
printPowerSet(set)


# Library solution (faster)
from itertools import chain, combinations

def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

# print(list(powerset([1,2,3])))


