from math import sin, ceil
import random
import datetime as dt # we can assign a name

# math module
res1=sin(30)
print(res1)

res2=ceil(2.5)
print(res2)

# random module
res3=random.random() #in random module random function
print(res3)

res4=random.randint(70,90) #random int num in range
print(res4)

winner=random.choice([3,5,10,15,18,23,85]) # make a choise in given numbers like lottery
print("winner is: ",winner)

# dateTime
time=dt.datetime.now().ctime()
date=dt.datetime.now().date()
print(time,date)


