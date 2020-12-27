pazzle="В вазе было 12 конфет. 5 конфет съели.Сколько конфет осталось?"
print(pazzle)
isGuessed=False
answer = int(input())

while isGuessed!=True:
    if    answer==7:
          print("правильно, ты молодец")
          isGuessed = True
    else:
          print("Неправильно, попробуй снова")
          answer=int(input())
          isGuessed = False
print("спасибо за ответ.")




