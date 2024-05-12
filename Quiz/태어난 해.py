#태어난 해와 태어난 달과 태어난 날을 입력받아서 태어난 날의 요일을 출력하도록 만들자.

year=int(input("태어난해를 입력하시오."))
month=int(input("태어난 월을 입력하시오"))
day=int(input("태어난 날을 입력하시오"))

import datetime
date=datetime.datetime(year, month, day)

if date.weekday() == 0:
    print("월요일 입니다")
if date.weekday() == 1:
    print("화요일 입니다")
if date.weekday() == 2:
    print("수요일 입니다.")
if date.weekday() == 3:
    print("목요일 입니다")
if date.weekday() == 4:
    print("금요일 입니다.")
if date.weekday() == 5:
    print("토요일 입니다.")
if date.weekday() == 6:
    print("일요일 입니다.")


 
 
 