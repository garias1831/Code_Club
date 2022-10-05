import random as r


def start_game():
    random_number = r.randrange(1,6)

    guess = input("Guess a number 1 to 5: ")
    #It's important we convert the guess variable to an integer, because Python considers "2" and 2 as seperate values
    #If we don't convert to an int, then the following if statement won't ever work, because the user is always supplying strings as input
    if int(guess) == random_number:
        print("You won woah!") 
    else:
        print("You suck!")


start_game()