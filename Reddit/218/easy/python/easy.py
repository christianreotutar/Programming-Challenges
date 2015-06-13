import fileinput

"""
    Tells you if a number parameter is a palindrome
    i.e. 1331, 131, and 1 return true but 1333 returns false.

    @type num Integer
    @arg num The number to check
    @return T/F depending on whether num is a palindrome or not
"""
def isPalindrome(num):
    strnum = str(num)
    strlength = len(strnum)
    for i in range(strlength/2):
        if strnum[i] != strnum[strlength-1-i]:
            return False
    return True

"""
    Returns the reverse of a number
    i.e. 1354 reversed is 4531.

    @type num Integer
    @arg num The number to reverse
    @return The reverse of a number

"""
def reverse(num):
    return int(str(num)[::-1])


"""
Main program
"""
for line in fileinput.input():

    # get rid of new lines
    line = line.strip()

    count = 0       # number of steps to palindrome
    num = 0         # temp. number placeholder
    initialnum = 0  # number we started with for print

    try:
        num = int(line)
        initialnum = num
    except ValueError:
        raise SystemExit("Input \'%s\' is not an integer number." % line)

    # continue adding its reverse until it is a palindrome
    while (not isPalindrome(num)):
        num += reverse(num)
        count += 1

    # you may use sys.stdout.write() for print without new line
    print("%d gets palindromic after %d steps: %d" % (initialnum,
    count, num))
