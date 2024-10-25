import random
from typing import Counter

newton = random.randint(1, 10)
print(newton)

print("We are going to play a game called {Guess the Number!}")
print()
print("Please guess any number from 1-10!!")
print()
number = int(input("Type a number!:"))


while True:
 if number == newton:
    print()
    print("You got it!")
    break
 else:
    print()
    print("Wrong;p")
    print()
    number = int(input("Try again siily:"))
