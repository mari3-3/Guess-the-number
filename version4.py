import random

newton = random.randint(1, 10)

print("We are going to play a game called {Guess the Number!}")
print()
print("Please guess any number from 1-10!!")
print()
guesses = []

number = int(input("Type a number!:"))
guesses.append(number)

counter = 1


while counter <= 2:
 if number == newton:
    print()
    print("You got it!")
    break
 else:
    print()
    print("Wrong;p")
    print()
    number = int(input("Try again siily:"))
    guesses.append(number)
    counter += 1
if counter == 3:
    print()
    print("YOU LOSEEEEE >:P")
    print("You guessed:",guesses)
