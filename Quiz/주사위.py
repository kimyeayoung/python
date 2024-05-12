#1.첫번째 문제
import random
#주사위 세개중 하나 뽑기
choices=["주사위1","주사위2","주사위3"]
cointoss1=random.choice(choices)
print(cointoss1,"입니다.")
#세 주사위의 값 중 랜덤으로 하나의 수
num1 = random.randrange(1,7)#주사위는 6면체
num2 = random.randrange(1,7)
num3 = random.randrange(1,7)
print("주사위 숫자",num1)
#주사위를 굴려서 나온 숫자 세개 
choices1=[num1,num2,num3]
cointoss2=random.choices(choices1)
print(cointoss2,"입니다.")

