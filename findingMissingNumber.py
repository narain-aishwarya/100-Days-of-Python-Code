def findMissingNumbers(n):
    numbers = set(n)
    length = len(n)
    output = []
    for i in range(1, n[-1]):
        if i not in numbers:
            output.append(i)
    return output



listOfNumber = [1, 2, 4, 5, 8, 9, 10, 11, 13, 14, 16 ]  
print(findMissingNumbers(listOfNumber))
