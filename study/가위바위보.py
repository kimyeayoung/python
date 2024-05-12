#코드가 무슨 타입인지 보기
name="Ben"
print(type(name))

#매소드 확인
name="Ben"
name=name.upper() #upper 함수는 모두 대문자로 바꿈
name=name.lower() #lower 함수는 모두 소문자로 바꿈
name=name.strip() #strip 함수는 앞뒤 공백을 없앰
print(name)
#불필요한 공백 없애는 함수
#rstrip() : 오른쪽,즉 문자열 뒤에 있는 불필요한 공백을 없앰
#lsrtri() : 왼쪽, 즉 문자열 앞에 있는 불필요한 공백을 없앰
#strip() : 위 함수 두개를 합친 것으로, 앞뒤 공백을 모두 없앰

#2개 사용하기
name="Ben"
name=name.upper().strip()
print(name)