# แม่สูตรคูณ แบบที่ 1

i=2
while i<=4:   #แสดงแม่ 2,3,4
    print("สูตรคูณแม่ ",i)
    j=1
    while j<=12:
        result=(i*j)
        print(i," x ",j,"=",result)
        j+=1
    i+=1


# แม่สูตรคูณ แบบที่ 2

for x in range(2,4):  #แสดงแม่ 2,3
    print("แม่ = ",x)
    for y in range(1,13):
        print(x," x ",y,"=",(x*y))