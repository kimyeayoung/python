# 컴퓨터가 숫자 0에서 100 중 랜덤으로 하나를 선택해서 
# 사용자가 입력한 숫자가 그 숫자인지를 확인하는 게임 만들기
# 사용자가 입력한 숫자가 컴퓨터가 랜덤으로 정한 숫자보다 크다면 
# "숫자가 더 큽니다. 낮춰주세요" 출력
# 사용자가 입력한 숫자가 컴퓨터가 랜덤으로 정한 숫자보다 작다면
# "숫자가 더 작습니다. 키워주세요" 출력
# 사용자가 입력한 숫자가 컴퓨터가 랜덤으로 정한 숫자와 같다면
# "정답입니다." 출력
# 반복문을 통해서 사용자가 입력한 숫자가 랜덤으로 정한 숫자와 같을 때 프로그램 종료

import random
choices=(1,100)
cointoss=random.choice(choices)

answer=""
while cointoss != answer:
    answer =int(input("컴퓨터의 숫자를 맞추세요:"))
    if cointoss < answer:
        print("숫자가 더 큽니다. 낮춰주세요")
    elif cointoss > answer:
        print("숫자가 더 작습니다. 높여주세요.")
    else:
        print("컴퓨터의 숫자를 맞추셨습니다!정답입니다.")
        