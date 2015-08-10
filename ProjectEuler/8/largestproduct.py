import fileinput

numbers = []

for line in fileinput.input():
    line = line[:-1]
    linesplit = list(line)
    for num in linesplit:
        x = int(num)
        numbers.append(x)

greatestProduct = 0
numAdjacentDigits = 13

for i in range(len(numbers) - numAdjacentDigits):
    currentProduct = 1
    for j in range(13):
        currentProduct *= numbers[i+j]
    if currentProduct > greatestProduct:
        greatestProduct = currentProduct

print(greatestProduct)  
