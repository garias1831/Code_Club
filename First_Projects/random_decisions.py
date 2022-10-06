import random as r #python random module
from time import sleep #python time module for creating time delays

def start_game():
    print("Can't decide? Good. Welcome to decision.org!")
    #Create the categories
    category = choose_category()
    pick_item(category)
    restart()
    

def choose_category():
    foods = ["Pizza", "Cheesecake", "Snow Cone", "Turkey Leg"]
    wars = ["Napoleonic Wars", "Punic Wars", "War of the Spanish Succession"]
    people = ["Victor", "Diego", "Cameron"]
    category = ""

    print("1. Foods\n2. Wars\n3. Epic People") #"\n is a special charachter that tells the terminal to print on a new line"
    while True:
        choice = input("Type the number of the category you want to pick: ")

        #Picking a category based on what the user wants
        if choice == "1": #this violates ocp, but its fine
            category = foods
            break
        elif choice == "2":
            category = wars
            break
        elif choice == "3":
            category = people
            break
        else:
            print("Make sure you typed the desired number correctly.")
    print("\n")
    return category


def pick_item(category):
    #The * in front of a list name prints all the list elements, and the 'sep' parameter defines how to seperate each thing we print out
    #In this case, each element is separated by a comma and a space.
    #The more straightforward way is to just use a loop to print out each element, or to just not at all.
    print("Category: ")
    print(*category, sep=", ")

    #Pick a random element from the category
    #The len(list) method returns the length of the list
    decision = category[r.randrange(0,len(category))]
    print("Making decision...")
    sleep(2) #sleep() delays the program by a certain number of seconds
    print(f"The decision is: {decision}!")


def restart():
    choice = input("Play again? Type 'n' to exit.")
    if choice.lower() != "n":
        print("\n")
        start_game()


start_game()