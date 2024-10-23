import random

newton = random.randint(1, 10)
print(newton)

print("We are going to play a game called {Guess the Number!}")
print()
print("Please guess any number from 1-10!!")
print()
number = int(input("Type a number!:"))

if number == newton:
  print("You got it^.^")
else:
  print("No. Do better")
