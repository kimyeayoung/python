animal=["개","고양이","박쥐","개미"]
print(animal)
print(len(animal)) #동물의 길이를 나타내줌-len
print(animal[0]) #리스트는 원소접근시 0부터 시작
print(animal[1:3])#두개 하고싶을땐 -1감안해서 1:3

print(animal[-1])#마이너스는 뒤에부터 시작/괄호안은 인덱스라고 부름
animal[2]="참새"
print(animal[2])

#항목 추가하기
animal.append("개구리") #덧붙이는 함수
print(animal)

#항목 삭제하기
animal.pop(-2)  #pop은 꼭 인덱스 써야함
print(animal)

animal.remove("개구리") #remove는 항목이름 써도 됨
print(animal)

#항목 확장하기
pizza=["도미노","피자마루","피자헛"]
animal.extend(pizza) #문자열 확장함수 익스텐드 (extend)
print(animal)

#항목이 리스트에 존재하는지, 안하는지
if "고양이" in animal:
    print("고양이가 존재합니다")
else:
    print("고양이가 존재하지 않습니다")
    
if "고양이" not in animal:
    print("고양이가 존재하지 않습니다")
else:
    print("고양이가 존재합니다 ")
    

#리스트 정렬 -문자열은 가나다순 정렬/숫자는 오름차순
animal.sort()
print(animal)
