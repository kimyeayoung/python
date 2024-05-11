import datetime
today=datetime.datetime.now()
#if today.weekday() == 3:
#    print("오늘은 토요일이니 학교가 쉽니다")
#if today.weekday() == 6: 
#    print("오늘은 일요일이니 학교가 쉽니다")
#else:
#    print("오늘은 학교를 가야합니다")


if today.weekday() > 3 and today.weekday() >= 3: 
    print("오늘은 휴일이니 학교가 쉽니다")

elif today.weekday() == 4:
    print("금요일은 휴강입니다.")

else:
    print("휴일이 아닙니다.")
#and= 둘다 만족시킬때 
if today.weekday() in[3,6]:
    print("오늘은 휴일이니 학교가 쉽니다")
year=int("2011")

num=input("숫자를 입력하시오")
num=int(num)
print(type(num))
