import random as r
import os

#Ascii escape sequences for coloring console text
class Colors:
    red = "\033[91m"
    green = "\033[92m"
    yellow = "\033[93m"
    end = "\033[0m"


#All of the relevant user information
class User:
    def __init__(self):#I hate this
        #How many times the user has guessed incorrectly 
        self.mistakes = 0
        #The word the user is trying to guess
        self.word = ""
        #The field of 'blanks' that will be shown to the user, and slowly get filled in
        self.unfinished_word = ""
        #The letters the user has already guessed
        self.guessed_letters = set()


#Starts & runs the game
def start_game(user):
    set_cwd()
    get_word(user)
    while user.mistakes != 6:
        show_sprite(user.mistakes)
        get_guess(user)
    show_sprite(user.mistakes)
    end_game(user.word)

    
#Change current working directory to the Hangman folder so that the files can be read
def set_cwd():
    os.chdir(r"C:\Users\gabri\OneDrive\Desktop\Code_Club\Hangman")


#Randomly retrieves a word from a text file
def get_word(user):
    with open("Words.txt") as words:
        file_lines = words.readlines()
        random_line = file_lines[r.randrange(0,996)]

    user.word = random_line.strip()
    for letter in user.word:
        user.unfinished_word += "_"
    

#If the user gets a letter correct, update the blanks to show it
def update_unfinished_word(word, unfinished_word, guess):
    new_unfinished_word = ""
    unfinished_word_list = list(unfinished_word)

    for i in range(len(word)):
        if guess == word[i]:
            unfinished_word_list[i] = guess
    
    for letter in unfinished_word_list:
        new_unfinished_word += letter
    
    if new_unfinished_word == word:
        end_game(word, True)

    return new_unfinished_word


#Loads the visual hangman based on the user's current attempt count
def show_sprite(mistakes): 
    with open("Sprites.txt") as sprites: # This is not the best way of doing this     
        file_lines = sprites.readlines()
        for line in range(mistakes*6, (mistakes + 1 )*6): 
            print(file_lines[line], end = "")


#Get's the user's guess and checks to see if it is correct
def get_guess(user):
    print(user.unfinished_word)
    print(f"Already guessed letters: {user.guessed_letters}") #Set because i'm lazy
    guess = input("Guess a letter in the word: ")
    guess = guess.lower()

    invalid_guess = validate(guess, user.guessed_letters)
    
    if invalid_guess == True:
        return
    elif guess in user.word:
        user.guessed_letters.add(guess)
        print(f"{Colors.green} Correct guess! {Colors.end}")
        user.unfinished_word = update_unfinished_word(user.word, user.unfinished_word, guess)
    else:
        user.guessed_letters.add(guess)
        user.mistakes += 1
        print(f"{Colors.red} That guess was incorrect. {Colors.end}")
    

#Checks to see if the user has a valid guess
def validate(guess, guessed_letters):
    if len(guess) != 1:
        print(f"{Colors.yellow} Make sure your guess is one letter long. {Colors.end}")
        return True
    
    if guess.isalpha() == False:
        print(f"{Colors.yellow} Make sure to only use alphabetical characters. {Colors.end}")
        return True
    
    if guess in guessed_letters:
        print(f"{Colors.yellow} You have already guessed with that letter. {Colors.end}")
        return True
        

#Ends the game based on a win or a loss, and prompts the user to play again.
def end_game(word, win = False):
    if win:
        print(f"{Colors.green} You won! You're so cool! {Colors.end}")
    else:
        print(f"{Colors.red} You lost. The correct word was {word}. {Colors.end}")
    
    choice = input("\nEnter any key to play again. Enter 'n' to exit. ")
    if choice.lower() == 'n':
        exit()
    else:
        start_game(User())

#Begin the game, pass in a new user object
start_game(User())

