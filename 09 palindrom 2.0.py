List = input("Введите слова:\t")
List = List.split(" ")
print(List)
for a in List:
    X = (a[::-1])
    if a == X:
        print("Это полидром")
    if a != X:
        print("Это не полидром")


