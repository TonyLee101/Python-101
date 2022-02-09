# ขอบตาราง
"""
number=int(input("ป้อนตัวเลข : "))

for row in range(number):
    for columm in range (number):
        if row == 0 or row == number-1 or columm == 0 or columm == number-1:
            print("x",end="")
        else:
            print(" ",end="")
    print(" ")

"""

# ตารางหมากฮอส

number = int(input("ป้อนตัวเลข : "))

for row in range(number):
    for columm in range(number):
        if (row+columm)%2==0:
            print("x",end="")
        else:
            print("o",end="")
    print(" ")