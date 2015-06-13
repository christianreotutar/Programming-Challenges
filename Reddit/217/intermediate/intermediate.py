'''
Solution by adrian17. I was just trying to learn it
'''

import fileinput

planets = ["Omicron", "Hoth", "Ryza", "Htrae"]

# lambda takes the sum of the number of alphabet/space characters in
# the text
rate_text = lambda text: sum(c.isalpha() or c.isspace() for c in text)

lines = fileinput.input()
try: 
    for lines in fileinput.input():
        line = lines.split()

        # we must remove the quotation marks at the beginning and end
        line.pop(0)
        line.pop()

        # find results for all possible languages
        # note: chr(x) gives us the unicode of bits
        # join concatenates lists of characters
        # 1) input xor 0001 0000, because must invert 5th bit
        # 2) input - 10
        # 3) input + 1
        # 4) reverse order of inputs
        results = [
            "".join(chr(int(c) ^ 0b10000) for c in line),
            "".join(chr(int(c) - 10) for c in line),
            "".join(chr(int(c) + 1) for c in line),
            "".join(chr(int(c)) for c in reversed(line))
        ]
        best = max(results, key=rate_text)
        planet=planets[results.index(best)]
        print("{:>7} | {}".format(planet, best))
except IOError:
    print("Usage: ./run.sh <inputfile>")
    raise SystemExit(0)

