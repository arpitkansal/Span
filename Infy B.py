def findSpecialProduct(inputArray):
    # Write your code here
    prod = 1
    n0 = 0
    ls = []
    for i in inputArray:
        prod *= i
        if i == 0:
            n0 += 1
    if n0 <= 1:
        for i in range(len(inputArray)):
            if inputArray[i] != 0:
                ls.append(int(prod / inputArray[i]))
            else:
                prodx = 1
                for j in range(len(inputArray)):

                    if j != i:
                        prodx *= inputArray[j]
                ls.append(prodx)
    else:
        ls = [0] * len(inputArray)
    return ls

print(findSpecialProduct([1,2,0,4,5,0]))