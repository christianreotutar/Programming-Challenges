import fileinput
import sys

'''
stableSort : sorts the array "array" on digit "digit" of every string of
    "array" and then returns a sorted array which is a stable sorted
    version of "array"

array : a list of strings
digit : an zero-index integer to represent digit we sort for

returns : a list of strings
'''
def stableSort(array, digit):
    # bucket[0] = "", bucket[1] = "A", bucket[2] = "B" ...
    buckets = [[] for i in xrange(27)]
    newarray = []
    
    # go through all strings and add to a bucket
    for i in xrange(len(array)):
        name = array[i]
        characters = list(name)

        letter = ""
        if (len(characters) - 1 < digit):
            letter = chr(ord("A")-1)
        else:
            letter = characters[digit]

        slot = ord(letter) - ord('A') + 1
        buckets[slot].append(name)

    # put all buckets into one newarray
    for i in xrange(len(buckets)):
        for j in xrange(len(buckets[i])):
            newarray.append(buckets[i][j])

    return newarray

'''
radixSort : sorts array "array" by going through all digits of all strings
    in the array in the reverse order and sorting

array : list of strings to sort
maxlen : integer length of the maximum length string in "array"

returns : list of sorted strings in "array"
'''
def radixSort(array, maxlen):
    newarray = array
    for digit in xrange(maxlen-1, -1, -1):
        newarray = stableSort(newarray, digit)
    
    return newarray

'''
findNameScore : taking the name "name", finds the value by the sum of all
    its letters' positions in the alphabet. this value is then multiplied
    by the names position in the sorted list "numberInList"

name : string name of the person
numberInList : position in list (not zero-indexed)

returns : integer name score of name "name"
'''
def findNameScore(name, numberInList):
    charList = list(name)
    score = 0
    for i in charList:
        letterScore = ord(i) - ord('A') + 1
        score += letterScore
    return score * numberInList

def main():
    names = []
    maxlen = 0

    names = fileinput.input()[0].strip().split(",")

    # remove quotation marks in each name, find maxlen
    for i in xrange(len(names)):
        name = names[i]
        names[i] = name.replace("\"", "")

        if (len(name) > maxlen):
            maxlen = len(name)

    # sort
    sortedNames = radixSort(names, maxlen)

    # find total name score
    totalScores = 0
    for i in xrange(len(sortedNames)):
        nameScore = findNameScore(sortedNames[i], i + 1)
        totalScores += nameScore

    print(totalScores)
        

if __name__ == "__main__":
    main()
