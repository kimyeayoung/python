#사용할 아스키 범위 - 이 범위를 벗어나면 오류가 발생할 수 있습니다.
asciiMin=32 # 공백 문자를 나타냄 - ""
asciiMax =126 # 물결표 문자를 나타냄 - "~"
# 암호화 키
key=314159
key=str(key)
#암호화할 메시지 입력받기
message= input("암호화할 메시지를 입력하세요:")
#암호화 메시지용 변수 초기화하기
messEncr=""
#메시지 루프
for index in range(0,len(message)):
    #해당 문자의 아스키값 가져오기
    char=ord(message[index])
#이 문자가 범위 밖인가요?
    if char < asciiMin or char > asciiMax:
    #예, 암호화에 적당하지 않으므로 그대로 둡니다.
        messEncr += message[index]
    # messEncr = messEncr + message[index]
    else:
    #이 문자는 암호화해도 안전합니다.
    #키만큼 값을 더하여 암호화합니다.
        ascNum = char + int(key[index % len(key)])
    #더한 값이 범위를 벗어난다면 범위 처음으로 되돌립니다.
    if ascNum > asciiMax:
        ascNum -= (asciiMax-asciiMin)
    #문자로 변환하고 출력할 내용에 추가합니다.
    messEncr=messEncr+chr(ascNum)
#결과 출력하기
print("암호화한 메시지:",messEncr)

#solution 함수 두 수의 차를 구하는 함수
def solution(num1, num2):
    answer = num1 - num2
    return answer

num = solution(3, 1)

x = 3 - 1
y = solution(3, 1)

#HELLO 말을 출력하는 함수
def printHello():
    x = 10-1
    y = 10-1
    print(x + y)
    
    
printHello()