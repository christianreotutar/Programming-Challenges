import fileinput
import math
import sys

triNums = [0]

def getTriangleNumber(num):
    return num + triNums[len(triNums)-1]

def getDivisors(num):
    divisors = []
    sqrt = int(math.sqrt(num))
    for i in xrange(1, sqrt+1):
        if (num % i == 0):
            divisors.append(i)
            divisors.append(num/i)
    return list(set(divisors))

def main():
    reqDivisors = int(fileinput.input()[0])

    maxDivisors = 0
    currentNum = 1
    while (maxDivisors < reqDivisors):
        triNum = getTriangleNumber(currentNum)
        triNums.append(triNum)

        maxDivisors = len(getDivisors(triNum))
        # print(getDivisors(triNum))
        currentNum += 1

    print triNums[-1]

if __name__ == "__main__":
    main()
