
def simplify(numer, denom):

    # find greatest common factor
    gcf = 1
    for i in xrange(numer, 1, -1):
        if numer % i == 0 and denom % i == 0:
            gcf = i
            break

    # divide by gcf
    return numer / gcf, denom / gcf

answersetnumer = []
answersetdenom = []
for numer in range(10, 99):
    for denom in range(10, 99):
        # must be less than 1
        if denom <= numer:
            continue

        if denom % 10 == 0 and numer % 10 == 0:
            continue

        charArrayNumer = list(str(numer))
        charArrayDenom = list(str(denom))
        
        for i in xrange(2):
            for j in xrange(2):
                removenumer = int(charArrayNumer[i])
                removedenom = int(charArrayDenom[j])

                # have to be the same number
                if (removenumer != removedenom):
                    continue

                newnumer = int(charArrayNumer[int(not i)])
                newdenom = int(charArrayDenom[int(not j)])

                #print (numer, denom, removenumer, newnumer, newdenom)

                oldnum = simplify(numer, denom);
                newnum = simplify(newnumer, newdenom);
                if oldnum == newnum:
                    answersetnumer.append(numer)
                    answersetdenom.append(denom)

answernumer = reduce(lambda x, y: x*y, answersetnumer)
answerdenom = reduce(lambda x, y: x*y, answersetdenom)
print(simplify(answernumer, answerdenom))
