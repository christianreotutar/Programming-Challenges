import fileinput
import sys

ones = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]

teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

tens = ["zero", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety", "hundred"]

numbersInWords = []

def getPlaceString(place, num, strOverallNum):
    if (num == 0):
        return ""

    if (place == 0):
        if (int(strOverallNum[len(strOverallNum)-2]) == 1):
            if (len(strOverallNum) != 1):
                return "";
        if (num != 0):
            return ones[num]
        else:
            return ""

    if (place == 1):
        if (num == 1):
            return teens[int(strOverallNum[len(strOverallNum)-1])]
        else:
            if (int(strOverallNum[len(strOverallNum)-1]) != 0):
                return tens[num] + "-"
            else:
                return tens[num]

    if (place == 2):
        if (int(strOverallNum[len(strOverallNum)-2]) != 0 or
            int(strOverallNum[len(strOverallNum)-1]) != 0):
            return ones[num] + " hundred and "
        else:
            return ones[num] + " hundred"

    if (place == 3):
        return ones[num] + " thousand "
        
    return ones[num]

def getEnglishOfNumber(num):
    strnum = list(str(num))
    places = len(strnum)

    numWord = ""
    tempnum = num
    for x in xrange(places):
        current = tempnum % 10
        tempnum //= 10
        numWord = getPlaceString(x, current, strnum) + numWord

    return numWord

if __name__ == "__main__":
    beginEnd = fileinput.input()
    beginning = int(beginEnd[0].strip())
    end = int(beginEnd[1].strip())

    for num in xrange(beginning, end + 1):
        word = getEnglishOfNumber(num)
        numbersInWords.append(word)

    answer = 0

    for word in numbersInWords:
        w = "".join(word.split())
        w = w.replace("-", "")
        answer += len(w)

    sys.stdout.write(str(answer) + "\n")
