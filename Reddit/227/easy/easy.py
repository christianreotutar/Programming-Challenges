import fileinput
import sys

stdinput = fileinput.input()
gridsize = int(stdinput[0])
position = stdinput[1]

maxnum = gridsize * gridsize

numStepsInDir = []

count = 0
direction = 0 # 0 right 1 up 2 left 3 down
for i in xrange(maxnum):

    if (i % 2 == 0):
        if (count < gridsize - 1):
            count = count + 1


    numStepsInDir.append((count, direction))
    direction = (direction + 1) % 4

print numStepsInDir
