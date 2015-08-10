import fileinput

grid = []
maxProduct = 1
maxfour = (0, 0, 0, 0)

for line in fileinput.input():
    # remove \n
    line = line[:-1]

    # create list for row
    line = line.split()

    # typecast
    for i in xrange(len(line)):
        line[i] = int(line[i])

    grid.append(line)

def printGrid(grid):
    for i in xrange(len(grid)):
        print (grid[i])

def findProduct(line):
    global maxfour
    global maxProduct
    if len(line) < 4:
        return 0

    currentprod = 1
    for i in xrange(len(line)-3):
        currentprod = line[i] * line[i+1] * line[i+2] * line[i+3]
        currentfour = (line[i], line[i+1], line[i+2], line[i+3])
        if currentprod > maxProduct:
            maxProduct = currentprod
            maxfour = currentfour

def findRows():
    for i in grid:
        findProduct(i)

def findColumns():
    transpose = zip(*grid)
    for i in transpose:
        findProduct(i)

def findDiagonals():

    # bottom left half going right
    for row in xrange(len(grid)):
        line = []
        tempcol, temprow = 0, row
        while (tempcol < 20 and temprow < 20):
            line.append(grid[temprow][tempcol])
            temprow += 1
            tempcol += 1
        findProduct(line)

    # bottom left half going right
    for row in xrange(len(grid)):
        line = []
        tempcol, temprow = 19, row
        while (tempcol > -1 and temprow < 20):
            line.append(grid[temprow][tempcol])
            temprow += 1
            tempcol -= 1
        findProduct(line)

    for col in xrange(0, len(grid[0])):
        line = []  
        tempcol, temprow = col, 0
        # top right half going right
        while (tempcol < 20 and temprow < 20):
            line.append(grid[temprow][tempcol])
            temprow += 1
            tempcol += 1

        findProduct(line)

        # top right half going left
        line2 = []
        tempcol, temprow = col, 0
        while (tempcol > -1 and temprow < 20):
            line2.append(grid[temprow][tempcol])
            temprow += 1
            tempcol -= 1

        findProduct(line2)
        

findRows()
findColumns()
findDiagonals()
print(maxProduct, maxfour)
