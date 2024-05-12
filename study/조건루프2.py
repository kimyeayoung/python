#입력 변수 초기화하기
userInput = ""
 
#STOP을 입력할 때까지 반복하기
while userInput != "STOP":
    userInput = input("무언가 입력하거나 멈추려면 STOP을 입력하세요:")\
        .upper().strip()
       
#사용자가 적은 동물을 리스트로 만들기 
animal=""
animal1=[]
while animal != "STOP":
    animal = input("동물을 입력하고 멈추려면 'STOP'을 입력하세요:")\
        .upper().strip()
        
    if animal == "STOP":
        break
    
    animal1.append(animal)
    print(animal1)
#반복문 끝
