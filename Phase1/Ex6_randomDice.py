# ทายเลขลูกเต๋า

import numbers
import random

myrandom = random.randrange(1,7)
k=0
print("คุณมีโอกาสตอบ 3 ครั้ง เลือกตัวเลข 1 - 7\n")
while True:
    number=int(input("ป้อนคำตอบขอคุณ : "))
    if number<0 or k==3:
        break
    correct=(number==myrandom)
    if not correct:
        if (number>myrandom):
            print("น้อยกว่านี้")
        if (number<myrandom):
            print("มากกว่านี้")

    if correct:
        print("ตอบถูกได้รางวัล")
        break
    k+=1

print("เฉลย = ",myrandom)
