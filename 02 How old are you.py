print("Hello,user")

user_name = input("What is your name?   ")
print('Hello',user_name, "in your name ",len(user_name), 'letters')


user_year = int(input("When you was born?  "))
if len(str(user_year))==4:
    print("nice year,", user_year)
    print(2020-user_year)
else:
    print("You make a little mistake")

