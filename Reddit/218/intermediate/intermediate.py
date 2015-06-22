import sys
from polyomino import Polyomino
from node import Node

nodes = [None for i in range(n)]
polyominoes = []

def rec_poly (num_blocks_left, num_surrounding, current):

    # cannot surround with more blocks than we own
    if (num_surrounding > num_blocks_left):
        return

    # this should never happen...
    if (num_surround) > 4):
        return

    temp_node = nodes[current]
    # add all possible to surrounding
    add_to_sides(num_surrounding, temp_node)
    
    new_blocks_left = num_blocks_left - num_surrounding
    new_current = current + 1
    for i in range(1, new_blocks_left):
        rec_poly(new_blocks_left, i, new_current)
    return

def add_to_sides(num_surrounding, node):
    return

# The argument number of blocks in a polyomino
n = int(sys.argv[1])

# Create n nodes
for i in range(n):
    nodes[i] = Node()

# Create all possible permutations
for i in range(1, n):
    rec_poly(n-1, i, 0)

#nodes[0].addTop(nodes[1])
# p = Polyomino(nodes)
#print(p);
