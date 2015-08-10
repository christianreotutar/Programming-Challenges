import sys
import math

# very naive

'''
for i in range(1000):
    for j in range(1000):
        for k in range(1000):
            if (i + j + k != 1000):
                continue
            if (i**2 + j**2 != k**2):
                continue
            print (i * j * k)
            sys.exit
'''

# less naive

'''
Using Dickson's method:
    r = a + b - c
    s = c - b
    t = c - a
    r**2 - 2st = a**2 + b**2 - c**2
    meaning r**2 = 2st when a**2 + b**2 = c**2
'''

for s in range(1, 1000):
    for t in range(s, 1000-s):
        r = math.sqrt(2 * s * t)
        if r%1 == 0:
            r = int(r)
            a = r + s
            b = r + t
            c = r + s + t
            if (a + b + c == 1000):
                print(a * b * c)
                sys.exit
