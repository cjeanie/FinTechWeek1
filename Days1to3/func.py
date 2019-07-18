chrisNumber = input("What number do you want to multiply? ")
chrisNumber = int(chrisNumber)

otherNumber = input("What do you what to multiply your number by?")
otherNumber = int(otherNumber)

def multiplyFunction(chrisNumber, otherNumber):
    return chrisNumber*otherNumber
print(multiplyFunction(chrisNumber, otherNumber))