""" 
7. การต่อ string (Concatinate) +
8. การจัดรูปแบบการแสดงผล {}
9. นับจำนวนประโยค (count)
10. เช็คคำขึ้นต้น
"""
from os import name


fname = "Tanongsak"
lname = "Kanya"
age = "28"
#7
print("ชื่อ :"+fname+"\tนามสกุล :"+lname+"\tอายุ :"+age)

#8
text = "ชื่อ :{}\tนามสกุล :{}\tอายุ :{}"
print(text.format(fname,lname,age))

#9 
fruit="ไปซื้อผลไม้ มีทุเรียน มุงคุด ข้าวเหนียวทุเรียน ที่ตลาดทุเรียน"
print(fruit.count("ทุเรียน"))

#10 
name="นายกอไก่ ใจดี"
print(name.startswith("นาย"))
print(name.endswith("ดี"))