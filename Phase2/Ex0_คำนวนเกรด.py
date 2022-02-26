score=int(input("กรอกคะแนน : "))

def gradeV1(score):
    gradeLable="FFFFFDCBAAA"
    print((score < 0 or score > 100) and "Error" or gradeLable[score//10])

def gradeV2(score):
    print((score < 0 or score > 100) and "Error" or "FFFFFDCBAAA"[score//10])

gradeV2(score)