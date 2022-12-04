from os import chdir
chdir(r'C:\Users\Gabriel\Downloads\Python\advent2022\day3')

#Finds the element that is common between the two compartments of the sack
def find_duplicate(sack):
    compartment1  = sack[0:(int(0.5*len(sack)))]
    compartment2 = sack[int((0.5*len(sack))):int(len(sack))]
    duplicate = [i for i in compartment1 if i in compartment2]
    return duplicate[0]

#Finds the priority value associated with each item
def get_priority_value(item):
    items = (
        'a', 'b', 'c', 'd', 'e', 'f', 'g',
        'h', 'i', 'j', 'k', 'l', 'm', 'n', 
        'o', 'p', 'q', 'r', 's', 't', 'u', 
        'v', 'w', 'x', 'y', 'z'
        )
    score = items.index(item.lower()) + 1
    if item.lower() != item:
        score += 26

    return score

priority_sum = 0
with open('contents.txt') as f:
    lines = f.read().split('\n')

sacks = [list(line) for line in lines]
for sack in sacks:
    duplicate = find_duplicate(sack)
    priority_value = get_priority_value(duplicate)
    priority_sum += priority_value
print(f'The sum of the priorities is: {priority_sum}')
