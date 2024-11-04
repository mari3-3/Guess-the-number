import random

newton = random.randint(1, 10)
print(newton)

print("We are going to play a game called {Guess the Number!}")
print()
print("Please guess any number from 1-10!!")
print()
guesses = []

number = int(input("Type a number!:"))
guesses.append(number)

counter = 1

while counter <= 4:
 if number == newton:
    print()
    print("YOU GOT IT {@_@}!")
    break
 else:
    print("Wrong;p")
    print()
    print("You guessed:",guesses)
    print()
    number = int(input("Try again siily:"))
    guesses.append(number)
    counter += 1
if counter == 5:
    print()
    print("WRONGG:><:YOU LOSEEEEE >:P")
    print()
    print("You guessed:",guesses)
