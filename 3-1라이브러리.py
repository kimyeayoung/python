#1.첫번째 문제
#import random
#주사위 세개중 하나 뽑기
#cointoss1=random.choice(choices)
#print(cointoss1,"입니다.")
#세 주사위의 값 중 랜덤으로 하나의 수
#num1 = random.randrange(1,7)#주사위는 6면체
#num2 = random.randrange(1,7)
#um3 = random.randrange(1,7)
#print("주사위 숫자",num1)
#주사위를 굴려서 나온 숫자 세개 
#choices1=[num1,num2,num3]
#cointoss2=random.choices(choices1)
#print(cointoss2,"입니다.")

#2.두번째문제
print("출력결과물")
print("운세를 알려드립니다!!!")
name = input("당신의 이름을 입력하시오")
print("당신의 운세를 알려드리겠습니다! 잠시만 기다려주세요.....")
import random
choices=["오늘은 매우 좋은 하루가 될 거에요!","오늘은 조금 피곤할 수도 있어요.휴식이 필요해요"
         ,"새로운 만남이 기다리고 있어요.열린 마음으로 임하세요","금전적인 행운이 찾아올 거에요.지출에 주의하세요."
         ,"건강에 조금 더 신경쓰세요.물 많이 마시는 것을 잊지 마세요"]
cointoss=random.choice(choices)
print(cointoss)