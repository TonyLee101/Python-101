# Fibonacci
# 0 , 1 , 1 , 2 , 3 , 5 , 8 ,...
# number = int(input("Fibonacci number : "))
def Fibonacci(number):
    if number <= 1:
        return number
    else:
        return Fibonacci(number-1) + Fibonacci(number-2)
        
# for i in range(number):
    # print(Fibonacci(i),"",end="")
print(Fibonacci(40))
