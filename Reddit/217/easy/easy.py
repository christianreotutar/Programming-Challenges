import fileinput
from heapq import heappush, heappop

class Pile(object):
    def __init__(self, slot, num):
        self.num = num
        self.slot = slot
    def __cmp__(self, other):
        return cmp(self.num, other.num)

    def __repr__(self):
        return repr("[" + str(self.slot) + "," + str(self.num) + "]")

    def add(self):
        self.num += 1

lines = iter(fileinput.input())
n  = next(lines)
numLogs = int(next(lines))

minheap = []

i = 0
for line in lines:
    for num in line.split():
        heappush(minheap, Pile(i, int(num)))
        i += 1

for x in range(numLogs):
    curr = heappop(minheap)
    curr.add()
    heappush(minheap, curr)

for x in range(len(minheap)):
    print(heappop(minheap))
