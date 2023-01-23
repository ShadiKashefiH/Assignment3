import random

randomlist= []
n= int(input("Enter n:"))

for i in range(n):
    number= random.randint(1,30)
    randomlist.append(number)

print(randomlist)