import random
X = "1234567890"
Z = "asdfqwehjklmnbvcxzrtyuiop"
Y = "=+-_%№"
length = 8
password = " "
for a in range(length):
    password += random.choice(X+Z+Y)
print(password)

