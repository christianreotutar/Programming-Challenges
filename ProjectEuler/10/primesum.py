import sys

primes = []

#naive
#def isPrime(x)
#    if x == 1:
#        return False
#    for i in range(2, int(x/2)+1):
#        if (x % i == 0):
#            return False
#    return True
#

# useless
def isPrime(x):
    if x == 1:
        return False
    for i in xrange(len(primes)):
        if x % primes[i] == 0:
            return False
    return True

maxNumber = int(sys.argv[1])

#naive
#if maxPrime <= 2:
#    print(summation)
#
#for i in xrange(3, maxNumber+1, 2):
#    if isPrime(i):
#        primes.append(i)       
#        #print(" + " + str(i))
#        summation += i

numbers = [x for x in xrange(2, maxNumber+1)]
crossed = {}

# fill dictionary
for num in numbers:
    crossed[num] = False

for i in xrange(len(numbers)):
    if crossed[numbers[i]] == True:
        continue
    for j in xrange(i+numbers[i], len(numbers), numbers[i]):
        crossed[numbers[j]] = True
primes = filter(lambda x: crossed[x] == False, numbers)
#print(primes)
print(sum(primes))
