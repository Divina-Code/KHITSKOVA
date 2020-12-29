inlist = False
productlist = []
while inlist != True:
    answer = int(input("добавить продукт в список:[1], удалить продукт из списка:[2], посмотреть весь список продуктов:[3]"))
    if answer == 1:
        product = input("что вы хотите добавить? ")
        productlist.append(product)
    elif answer == 2:
        delete = int(input("что вы хотите удалить из списка?"))
        productlist.pop(delete)
    elif answer == 3:
        print(productlist)
    else:
        print("выберите 1, 2 или 3")
