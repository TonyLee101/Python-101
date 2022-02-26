# Factorial

number = int(input("Factorial : "))
def Factorial(number):
    if number == 1:
        return number
    else:
        return number * Factorial(number-1)

    

print(number,"! = ",Factorial(number))
