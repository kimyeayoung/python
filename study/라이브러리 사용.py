import datetime
today = datetime.datetime.now()
print(today,"입니다.")
print(type(today))
print("지금은",today.year,"년입니다.")
print("지금은",today.month,"월입니다.")
print("지금은",today.day,"일입니다.")

#클래스는 변수와 함수의 조합
#today 타입 == 클래스
#today 안에는 변수와 함수
#today.year .을 통해서 변수에 접근
#today weekday() 메소드
#today.weekday()

print("지금은",today.weekday(),"주입니다.")