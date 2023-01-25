# Write a random number generator that generates random numbers between 1 and 6(simulates a dice).

import random
min = 1
max = 6
rollagain = "y"
while rollagain == "y" or rollagain =="Y":
    print("Rolling the dice...")
    val = random.randint(min,max)
    print("You get...:",val)
    rollagain = input("Roll the dice again? (y/n)..")