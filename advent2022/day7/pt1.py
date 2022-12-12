from os import chdir
chdir(r'C:\Users\gabri\OneDrive\Desktop\Python\advent2022\day7')

class Directory:
    def __init__(self):
        self.value = 0
        self.parent_directory = None
        self.path_to_main = list()
        self.subdirectories = dict()

#Sets up the folder structure as a series of Directory classes
def open_drive():
    with open('drive.txt') as d:
        drive = d.read().split('\n')

    current_directory = main
    total = 0
    for cmd in drive:
        cmd = cmd.split(' ')

        if 'cd' in cmd:
            current_directory = change_directory(cmd, current_directory)
        elif cmd[0].isdigit():
            value = int(cmd[0])
            total += value
            current_directory.value += value
            
        elif 'dir' in cmd:
            new_directory = cmd[-1]
            current_directory.subdirectories[new_directory] = initialize_directory(current_directory)            

def update_parent_value(directory):
    if directory.parent_directory != None:
        for parent_directory in directory.path_to_main:
            parent_directory.value += directory.value

def initialize_directory(current_directory):
    new_directory = Directory()
    new_directory.parent_directory = current_directory
    #Path to directory is path to the parent dir plus the parent dir
    #List comprehension to create a copy
    new_directory.path_to_main = [x for x in current_directory.path_to_main]
    new_directory.path_to_main.append(new_directory.parent_directory)

    return new_directory


def change_directory(cmd, current_directory):
    if '/' in cmd:
        return main
    elif '..' in cmd:
        return current_directory.parent_directory
    #Get a string value for the desired directory 
    new_directory = cmd[-1]
    return current_directory.subdirectories[new_directory]

#Creates a list of the subdirectories belonging to the parent directory
def extract_subdirectory_values(directory):
    subdirectories = list(directory.subdirectories.values())

    for subdirectory in subdirectories:
        update_parent_value(subdirectory)
        extract_subdirectory_values(subdirectory)
        get_small_directories(subdirectory)
    
def get_small_directories(directory):
    if directory.value <= 100000:
        small_directories.append(directory.value)

main = Directory()
small_directories = []
open_drive()
extract_subdirectory_values(main)

total = sum(small_directories)
print(f'The sum of the directories less than 100000 bytes is: {total}')