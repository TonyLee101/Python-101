""" 
1.การเข้าถึงตัวอักษรใน string []
2. len function (name.len())
3. ลบช่องว่่างซ้ายขวา (name.strip), ลบซ้าย(lstrip)
4. แปลง case ของ string (name.upper()), (name.lower()), (name.capitalize())
5. การแทนที่ (name.replace())
6. การเช็คข้อความ ==> true , false
"""
name = "kongruksiam"
print(name.replace("k","B",2))


name = "ไปซื้อข้าวและอาหารที่ตลาด"
x = "ข้าว" in name

if x:
    name = name.replace("ข้าว","ไข่")
print(name)