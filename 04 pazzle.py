
isGuessed=False

while isGuessed!=7:
    puzzel="В вазе было 12 конфет. 5 конфет съели. Сколько конфет осталось?"

    answer=input(puzzle)

    if answer==7:
        print("Дааа,ты молодец.")
        isGuessed=7
    if answer!=7:
        print("неправильно, попробуй снова")

