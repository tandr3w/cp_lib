# Plan: 2d PSA (treat it like a DA)
# Compress the coordinates so only the mentioned coords are tracked (since everything in between can be found with multiplication)
# Since every coordinate that's in the input will be in the DA, we don't need to track the rest. They just have to be sorted.
# Use a dict to quickly get the actual coord from the coord on the array (or vice versa)
# Then, PSA and do some multiplication to get the area

n = int(input())
t = int(input())

x_positions = []
y_positions = []
rects = []
for i in range(n):
	x1, y1, x2, y2, tint = map(int, input().split())
	rects.append([x1, y1, x2, y2, tint])
	x_positions.append(x1)
	x_positions.append(x2)
	y_positions.append(y1)
	y_positions.append(y2)

xPos = list(set(x_positions))
yPos = list(set(y_positions))
xPos.sort()
yPos.sort()

x_i = {}
for i in range(len(xPos)):
	x_i[xPos[i]] = i
y_i = {}
for i in range(len(yPos)):
	y_i[yPos[i]] = i

da = [[0]*len(xPos) for i in range(len(yPos))]

# Ok 2d PSA is frying my brain so im gonna try to split it into a bunch of 1d PSAs. Time complexity should be good enough since the input isn't too big
for i in range(n):
	for y in range(y_i[rects[i][1]], y_i[rects[i][3]]): # Update range for each row since it's easier (one row at a time)
		da[y][x_i[rects[i][0]]] += rects[i][4]
		da[y][x_i[rects[i][2]]] -= rects[i][4]

# print(da)
out = 0

for y in range(len(y_i)-1): # Iterate through every individual PSA
	for x in range(len(x_i)-1):
		da[y][x+1] = da[y][x] + da[y][x+1] # Calc into a PSA to get the actual tint values
		if da[y][x] >= t:
			out += (yPos[y+1]-yPos[y]) * (xPos[x+1]-xPos[x]) # Add the area of the rectangle from this element to the next element (since they can have a gap of more than 1)
print(out)

# 2d PSA attempt. Feel free to try it yourself lol
# for i in range(n):
# 	x1_updt = x_i[rects[i][0]]
# 	y1_updt = y_i[rects[i][1]]
# 	x2_updt = x_i[rects[i][2]]
# 	y2_updt = y_i[rects[i][3]]
# 	tint_fac = rects[i][4]
# 	da[y1_updt][x1_updt] += tint_fac
# 	if x2_updt+1 < len(xPos):
# 		da[y1_updt][x2_updt+1] -= tint_fac
# 	if y2_updt+1 < len(yPos):
# 		da[y2_updt+1][x1_updt] -= tint_fac
# 	if x2_updt+1 < len(xPos) and y2_updt+1 < len(yPos):
# 		da[y2_updt+1][x2_updt+1] += tint_fac

# out = 0
# for x in range(1, len(xPos)):
# 	for y in range(1, len(yPos)):
# 		if x > 0:
# 			da[y][x] += da[y][x-1]
# 		if y > 0:
# 			da[y][x] += da[y-1][x]
# 		if x > 0 and y > 0:
# 			da[y][x] -= da[y - 1][x - 1]
# 		if da[y][x] >= t:
# 			out += (xPos[x]-xPos[x-1])*(yPos[y]-yPos[y-1])

# print(out)
