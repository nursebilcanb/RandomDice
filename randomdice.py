import random
from time import sleep

timesDice = int (input("How many times do you want to roll the dice?\n"))
dice =[1,2,3,4,5,6]

for i in range(timesDice):
 print(random.choice(dice))
 sleep(1)
