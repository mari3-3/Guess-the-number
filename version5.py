import random

newton = random.randint(1, 100)
print(newton)

print("We are going to play a game called {Guess the Number!}")
print()
print("Please guess any number from 1-100!!")
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
        if number < newton:
            print()
            print("Number is too low. Do better")
        if number > newton:
            print()
            print("Number is too high. Do better")
        print()
        print("You guessed:",guesses)
        print()
        number = int(input("Try again siily:"))
        guesses.append(number)
        counter += 1
    
    if counter == 5 and number != newton:
        print()
        print("WRONGG:><:YOU LOSEEEEE >:P")
        print()
        print("You guessed:",guesses)
    if counter == 5 and number == newton:
        print()
        print("YOU GOT IT {@_@}!")
        break
