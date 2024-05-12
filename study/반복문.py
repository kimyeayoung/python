#반복문
animals=["토끼","거북이","사마귀","나무늘보","미니돼지","말티즈"]#animals는 리스트를 나타내준다
for animal in animals:
    print(animal)

print(animal)

#많이 쓰이는 반복문
for i in range(0,6):
   print(animals[i])

#중첩 반목문
for i in range(1,3):
    for j in range(1,4):
        print("반복 i: " , i , ",  j: " , j)