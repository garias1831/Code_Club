import random as r
#Variables only exist in the region they are created, which is why we create the lives variable within the start_game function
#An alternative could be to declare the lives variable outside the start_game function, and pass it in through a parameter

def start_game():
    lives = 3 
    random_number = r.randrange(1,6)

    while lives > 0:
        guess = input("Guess a number 1 to 5: ")
        #It's important we convert the guess variable to an integer, because Python considers "2" and 2 as seperate values
        #If we don't convert to an int, then the following if statement won't ever work, because the user is always supplying strings as input
        if int(guess) == random_number:
            print("You won woah!") 
            break #When we win, exit the loop (which terminates the game)
        else:
            print("You suck!")
            lives -= 1 #Subtract 1 from the total number of user attempts
    

start_game()