import random

number1= random.randint(1,6)

if number1== 6:
    number2= random.randint(1,6)
    number3= random.randint(1,6)
    print("You've got a 6! Your second attempt is", number2, "and your third attempt is", number3)

else:
    print("You've got a",number1)
        