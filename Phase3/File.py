# File Management
import os
try:
    fw=open("Phase3/Score.txt","a",encoding="utf-8") # w=>write , a=>append , utf-8=>ภาษาไทย
    name=input("ป้อนข้อความที่ต้องการ : ")
    fw.writelines(name+"\n")
    fw.close()
except FileNotFoundError :
    print("หาไฟล์ไม่เจอ")

