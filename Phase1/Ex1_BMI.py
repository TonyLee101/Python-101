# โปรแกรมคำนวนค่าดัชนีมวลกาย
# BMI = น้ำหนัก(kg) / ส่วนสูง(m) **2 

#input / Convert to integer

weight=int(input("ระบุน้ำหนัก(kg) : "))
height=int(input("ระบุส่วนสูง(cm) : "))

# height = height / 100
height/=100

BMI = weight / (height**2)

result="ไม่ทราบค่าที่ัดเจน"
if 0 < BMI < 18 :
    result="ต่ำกว่าเกณฑ์"
elif 18 <= BMI < 23:
    result="สมส่วน"
elif 23 <= BMI < 25:
    result="น้ำหนักเกิน"
elif 25 <= BMI < 29:
    result="โรคอ้วน"
elif BMI > 29:
    result="อ้วนอันตราย"

print("ค่า BMI = ",BMI, "วินิฉัยว่า ", result)
