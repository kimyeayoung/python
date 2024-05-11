
# 가위바위보문제
# 가위 바위 보 중 하나를 입력받아서 컴퓨터가 랜덤으로 선택한 것과 비교하여서 
# 게임에서 졌는지 이겼는지를 판단하는 게임 만들어라
# 
# 출력
# 가위 바위 보 중 하나를 입력하시오: 가위
# 컴퓨터가 랜덤으로 선택한 것은 바위 입니다.
# 졌습니다.

game=input("가위 바위 보 중 하나를 입력하시오")

import random
choices=["가위","바위","보"]
cointoss=random.choice(choices)
print("컴퓨터가 랜덤을 선택한 것은",cointoss,"입니다.")

import random
if cointoss == "가위" and game == "바위":
    print("이겼습니다.")
elif cointoss=="보" and game == "가위":
    print("이겼습니다.")
elif cointoss=="바위" and game == "보":
    print("이겼습니다.")
elif cointoss=="바위" and game == "가위":
    print("졌습니다.")
elif cointoss =="가위" and game == "보":
    print("졌습니다.")
elif cointoss=="보" and game == "바위":
    print("졌습니다.")
elif cointoss==game:
    print("동점입니다.")


    




    



  