puzzle = "Компьютер загадал число от 1 до 100, попробуйте угадать."

print(puzzle)

Answer: int = 30

print("Введите число")

isGuessed = int(input())

while Answer != True:

    if isGuessed > Answer:
            print('Ваше число больше загаданного, попробуйте ещё раз')
            isGuessed = int(input())
    elif isGuessed < Answer:
            print("Ваше число меньше загаданного, попробуйте ещё раз")
            isGuessed = int(input())
    else:
            print("Угадал, ты молодец")
            Answer = True

print("спасибо за игру")
