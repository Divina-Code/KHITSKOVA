import random
player1 = random.randint(2, 11)
player2 = random.randint(2, 11)

inGame1 = True # играет ли игрок 1 или уже закончил
inGame2 = True # играет ли игрок 2 или уже закончил

while inGame1:

    # Предлагаем карту первому игроку
    if inGame1:
        take_card = input("1-й игрок будет брать карту?[Да,Нет]")
        if take_card == "Да":
            player1 += random.randint(2, 11)
            print("теперь у тебя очков", player1)
        elif take_card == "Нет":
                inGame1 = False
                print("у тебя очков", player1)
        else:
            print("Я тебя не понял")
        if player1 > 24:
            inGame1 = False
            print("Игра закончена. Ты проиграл")
    else:
        inGame1 = True

while inGame2:

    # Предлагаем карту второму игроку
    if inGame2:
        take_card = input("2-й игрок будет брать карту?[Да,Нет]")
        if take_card == "Да":
            player2 += random.randint(2, 11)
            print("теперь у тебя очков", player2)
        elif take_card == "Нет":
                inGame2 = False
                print("у тебя очков", player2)
        else:
            print("Я тебя не понял")
        if player2 > 24:
            inGame2 = False
            print("Игра закончена. Ты проиграл")
    else:
        inGame2 = True

if player2 > player1:
    print("2-й игрок победил")
elif player2 < player1:
    print("1-й игрок победил")
else:
    print("Ничья")


print("Спасибо за игру")
