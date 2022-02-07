# โครงสร้างควบคุมแบบทำซ้ำ
summation=0

for i in range(1,6,2): # (start,stop,step)
    print("รอบที่ = ",i,"Sum = ",summation)
    summation+=i

print("ผลรวม = ",summation)