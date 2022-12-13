# First, math. Every mountain is made of 2 isosceles right triangles, and every mountain is similar. Thus, we only need to check the bases. Since the triangles are isosceles, the base is the range from (x - height) to (x + height)

# We can sort the mountain by the left pos of the base, then sort by the biggest rightpos as a tiebreaker.
# Let's break it down into two parts: Whether the leftpos is covered and whether the rightpos is covered
# Because of the sorting, no leftpos will be covered by a mountain after it, unless they have the same leftpos (which is why we need the rightpos as a tiebreaker, as the bigger rightpos will cover the smaller one)
# So, there are only two cases. Every mountain will cover the leftpos of the next mountain, or the next mountain's leftpos is past the first mountain's rightpos.
# In the second case, the rightpos must be bigger, so that mountain must be visible (there's no way for that mountain's leftpos to be covered anymore)
# In the first case, the mountain is only visible if the rightpos is bigger, since the leftpos is already covered.

# Thus, a mountain is only visible if its rightpos is bigger than the largest previous rightpos.

n = int(input())

mountains = []
for i in range(n):
    x, y = map(int, input().split())
    mountains.append((x-y, -(x+y)))

mountains.sort()
count = 0
most = 0
for mountain in mountains:
    leftPos = mountain[0]
    rightPos = 0 - mountain[1]
    if rightPos > most:
        most = rightPos
        count += 1
print(count)