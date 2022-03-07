# Exception
while True:
    try:
        name=input("ป้อนชื่อผู้ใช้โปรแกรม :")
        if name== "Oatz":
            raise Exception("มีชื่อในระบบแล้ว")
        
        number1=int(input("ป้อนตัวเลขที่1 :"))
        number2=int(input("ป้อนตัวเลขที่2 :"))
        if number1 == 0 and number2 == 0:
            break
        if number1<0 or number2<0:
            raise Exception("ไม่สามารถป้อนค่าติดลบได้")

        result=number1/number2
        print(result)
    except Exception as e:
        print(e)