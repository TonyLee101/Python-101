# แปลงอุณหภูมิ

from math import degrees


temp = input("ป้อนอุณหภูมิ(องศา) : ")  #45C

degree = int(temp[:-1])  #45
unit = temp[-1].upper() #C

if unit=="C":
    result=(9*degree)/5+32
    unit_result="องศาฟาเรนไฮน์"
    #แปลงเป็นฟาเรนไฮน์
if unit=="F":
    result=(degree-32)*5/9
    unit_result="องศาเซลเซียส"

print("แปลงตัวเลข = ",temp,"เป็น",int(result),unit_result)

