def multiplyAll(inString):
    numbers = inString.split()

    for i in range(len(numbers)):
        numbers[i] = int(numbers[i])
    
    product = 1 
    for num in numbers:
        product = product * num

    productString = str(product)
    
    return productString