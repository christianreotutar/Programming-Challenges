import fileinput
import sys

def radixSort(array, maxlen):
    newarray = array
    allbuckets = [[]
    for digit in xrange(maxlen):
        buckets = [[] for i in xrange(26)]
        for i in xrange(len(newarray)):
            name = newarray[i]
            characters = list(name)

            letter = ""
            if (len(characters) - 1< digit):
                letter = "A"
            else:
                letter = characters[digit]

            print(letter)
            slot = ord(letter) - ord('A')
            print(slot)
            buckets[slot].append(name)

        newarray = []
        for i in xrange(len(buckets)):
            for j in xrange(len(buckets[i])):
                newarray.append(buckets[i][j])
            
    return newarray

names = []
maxlen = 0

names = fileinput.input()[0].strip().split(",")
for i in xrange(len(names)):
    name = names[i]
    names[i] = name.replace("\"", "")

    if (len(name) > maxlen):
        maxlen = len(name)
print(names)

sortedNames = radixSort(names, maxlen)
print(sortedNames)
