import fileinput
import sys

def main():
    sums = [0 for i in xrange(50)]

    for line in fileinput.input():
        line = line.strip() # remove \n
        nums = [int(i) for i in list(line)]
        for i in xrange(len(nums)-1, -1, -1):
            sums[i] += nums[i]

    for i in xrange(len(nums)-1, -1, -1):
        # mod for the last digit
        # get everything else and bring to next digit
        # except for last digit

if __name__ == "__main__":
    main()

