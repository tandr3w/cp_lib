# Any magnifying level can be broken down into a 5x5 grid using division.
# So squares at any magnifying level are like this:
# O O O O O
# O O O O O
# O O e O O
# O e E e O
# O E E E O
# E = the block is completely full with crystal,
# O = the block is empty
# e = the block might be full with crystal, depending on the position inside the block
# So, start at the input magnification level. Find where the input location lies if you turn that magnification level into a 5x5 grid. If it's in a spot that corresponds to an E, there's a crystal there. If it's in a spot that corresponds to an O, it's empty. 

# If it's on an e, we need to find where the input location lies inside that square. First, we can zoom out but only look at the square that we know it's in, making it the same shape as before (when represented with the 5x5 grid). Then, we can find the location inside that square using modulo, and recursively do that until the location corresponds to an E block.

# sorry if this is confusing. try to consider doing this on input 2 8 5. We know the location is in square 1, 1. But where is it in the square? 8%5, 5%5 = (3, 0). Since this is an E square, there's a crystal there.

def solve(mag, x, y):
    if mag < 0:
        return False
    squareX = x//(5**(mag-1))
    squareY = y//(5**(mag-1))
    if squareX > 0 and squareX < 4 and squareY == 0:
        return True
    if squareX == 2 and squareY == 1:
        return True
    if (squareX == 1 and squareY == 1) or (squareX == 3 and squareY == 1) or (squareX == 2 and squareY == 2):
        return solve(mag-1, x%(5**(mag-1)), y%(5**(mag-1))) # Modulo since we narrowed down the square, so all the other ones are irrelevant.
    return False

t = int(input())
for i in range(t):
    m, x, y = map(int, input().split())
    if solve(m,x,y):
        print("crystal")
    else:
        print("empty")