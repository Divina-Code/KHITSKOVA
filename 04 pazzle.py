
isGuessed=False

while isGuessed!=True:
    puzzel="В вазе было 12 конфет. 5 конфет съели. Сколько конфет осталось?"

    answer=input(puzzle)

    if answer==7:
        print("Дааа,ты молодец.")
        isGuessed=True
    if answer!=7:
        print("неправильно, попробуй снова")

