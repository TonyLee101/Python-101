# แลกเงิน และหาจำนวนแบงค์

# 2000 => 1000 = 2 ใบ
# 1500 => 1000 = 1 ใบ , 500 = 1 ใบ

number = int(input("ป้อนจำนวนเงินของคุณ : "))

if number>=1000:
    print("1000 บาท =", number//1000,"ใบ")
    number%=1000                            # number = number%1000

if number>=500:
    print("500 บาท =", number//500,"ใบ")
    number%=500

if number>=100:
    print("100 บาท =", number//100,"ใบ")
    number%=100

if number>=50:
    print("50 บาท =", number//50,"ใบ")
    number%=50

if number>=20:
    print("20 บาท =", number//20,"ใบ")
    number%=20

if number>=10:
    print("10 บาท =", number//10,"เหรียญ")
    number%=10

if number>=5:
    print("5 บาท =", number//5,"เหรียญ")
    number%=5

if number>=1:
    print("1 บาท =", number//1,"เหรียญ")
    