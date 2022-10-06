import random as r
#Variables only exist in the region they are created, which is why we create the lives variable within the start_game function
#An alternative could be to declare the lives variable outside the start_game function, and pass it in through a parameter

def start_game():
    lives = 3 
    players = ["KD", "Chris Paul", "Giannis"]
    random_player = players[r.randrange(len(players))]

    while lives > 0:
        guess = input("Guess a basketball player")
        #It's important we convert the guess variable to an integer, because Python considers "2" and 2 as seperate values
        #If we don't convert to an int, then the following if statement won't ever work, because the user is always supplying strings as input
        if guess == random_player:
            print("You won woah!") 
            break #When we win, exit the loop (which terminates the game)
        else:
            print("You suck!")
            lives -= 1 #Subtract 1 from the total number of user attempts
    
    prompt = input("I love the national basketball association. Type 'n' to exit. Press any other key to run it back. ")

    #Making sure the prompt variable is lowecase, in case they had caps lock on or something "N" and "n" are two different things!
    if prompt.lower() != "n":
        start_game()
    

start_game()