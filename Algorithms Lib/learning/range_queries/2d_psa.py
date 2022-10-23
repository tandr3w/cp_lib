# PSAs can be 2d!
# https://usaco.guide/silver/more-prefix-sums?lang=py

matrix = [[1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1]]

rows = len(matrix)
columns = len(matrix[0])

psa = [[0 for x in range(rows)]
    for y in range(columns)]

for i in range(0, columns): # Initialize first column
    psa[0][i] = (psa[0][i - 1] + matrix[0][i])
for i in range(0, rows): # Initialize first row
    psa[i][0] = (psa[i - 1][0] + matrix[i][0])

for i in range(1, rows):
    for j in range(1, columns): # Init everything else
        psa[i][j] = (psa[i - 1][j] +
                    psa[i][j - 1] -
                    psa[i - 1][j - 1] +
                    matrix[i][j])

def find_range(psa, x1, y1, x2, y2): # Calculate sum of rectangle from (x1, y1) to (x2, y2)
        return (psa[x2][y2]
        - psa[x2][y1 - 1]
        - psa[x1 - 1][y2]
        + psa[x1 - 1][y1 - 1])

print(psa)
print(find_range(psa, 1, 1, 3, 4))



