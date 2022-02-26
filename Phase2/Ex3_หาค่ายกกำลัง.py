#หาค่ายกกำลัง
number=[1,2,3,4,5,6,7]

print(number)

#ปกติ
for i in range(len(number)):
    number[i]=number[i]**2
print(number)    

#ลดรูป
number=[i**2 for i in number]
print(number)
