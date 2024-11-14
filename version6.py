import random
import os as clear

game = True
played = 0
won = 0

while game: 
    newton = random.randint(1, 100)
    print("==Score Board==")
    print(f"You Played:{played}")
    print(f"You Won:{won}")
    print()
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
            print()
            print(f"You used {counter}/5 guesses,you guessed:",guesses)
            print()
            played += 1
            counter += 1
            won += 1
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
            print(f"You have {counter}/5 guesses left")
            print()
            number = int(input("Try again siily:"))
            guesses.append(number)
            counter += 1
        
        if counter == 5 and number != newton:
            print()
            print("WRONGG:><:YOU LOSEEEEE >:P")
            print()
            print("You guessed:",guesses)
            print()
            print(f"You used {counter}/5 guesses,you guessed:",guesses)
            print()
            played += 1
        if counter <= 5 and number == newton:
            print()
            print("YOU GOT IT {@_@}!")
            print()
            won += 1
            played += 1
            break
    again = input("Another round? (y/n): ")
    if again == "y":
        print()
        print("Yay! Let's have more fun ><!")
        print()
        print(">=< Your Score >=<")
        print(f"You Played:{played}")
        print(f"You Won:{won}")
        clear.system('clear')
        game = True
        continue
    elif again == "n":
        print()
        print("Quitter >:c")
        print()
        print(">=< Your Score >=<")
        print(f"You Played:{played}")
        print(f"You Won:{won}")
        print()
        game = False 
    break
